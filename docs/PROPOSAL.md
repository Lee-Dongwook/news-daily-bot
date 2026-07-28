# Proposal: Reliability & Maintainability Improvements

> **Status:** Draft for discussion · **Type:** Planning / RFC · **Author:** @Lee-Dongwook
>
> This is a proposal document, not an implementation. Nothing here changes behavior
> until we agree on scope. I'd love your feedback before I open any code PRs.

## 1. Motivation

First off, thank you for building and maintaining `news-daily-bot` — the idea of a
self-updating, multi-source news feed driven entirely by GitHub Actions is genuinely
fun, and it was easy to get up and running.

While reading through the workflow I noticed a few things that I believe affect the
bot's **reliability** (are we actually collecting what we think we are?) and its
**maintainability** (how easy is it to change and test safely?). I'd like to propose
a small, incremental plan to address them, entirely at your discretion.

Everything below is a suggestion. I'm happy to adjust the scope, split it up, or drop
any part you'd rather keep as-is.

## 2. Observations

These are grounded in the current `main` and the committed output under `news/` and
`stats/`, not assumptions.

### 2.1 Some configured sources appear to silently produce zero items

The workflow configures **7 sources**:

`NewsAPI`, `Hacker News`, `Reuters`, `BBC`, `Al Jazeera`, `CoinGecko`, `NASA`

However, across every committed run, only **4** ever appear in `sources_used`:

`Hacker News`, `BBC`, `Al Jazeera`, `NASA`

The three that never show up:

| Source    | Likely cause                                                                                     |
| --------- | ------------------------------------------------------------------------------------------------ |
| Reuters   | `https://feeds.reuters.com/Reuters/worldNews` was retired by Reuters and no longer serves items. |
| CoinGecko | The `/api/v3/news` endpoint has been deprecated/removed from the public API.                     |
| NewsAPI   | Requires the `NEWS_API_KEY` secret; the code no-ops cleanly when it is unset.                    |

Because each source is wrapped in `try/except` that only `print`s the error, these
failures are invisible in the run summary — the job stays green and the README still
looks healthy. That's great for uptime, but it hides the fact that ~40% of the
configured sources contribute nothing.

### 2.2 All application logic lives inside a YAML heredoc

The entire fetch/render/stats pipeline (~200 lines of Python) is embedded in the
workflow file as a `python << 'EOF'` heredoc. This makes it:

- **Untestable** — there's no way to run or unit-test the logic without triggering CI.
- **Hard to lint/format** — editors and tools treat it as an opaque YAML string.
- **Hard to review** — logic and CI configuration are tangled in one file.

### 2.3 No de-duplication across runs

The bot runs twice an hour and stores each snapshot independently. The same headline
(e.g. an HN front-page story) is re-recorded across consecutive runs, so `stats`
counts and `total_news` reflect duplicates rather than distinct stories.

### 2.4 Minor correctness nits

- Hacker News items are hard-coded to `category: "technology"`, even when the story
  is clearly something else (e.g. an earthquake report currently on the front page).
- `description` fields carry raw HTML from feeds straight into the README.
- The timezone is hard-coded to `Asia/Tehran`, which is surprising and not obviously
  intentional. Making it configurable would be low-risk.

## 3. Proposed plan

I'd suggest tackling this in small, independently reviewable steps rather than one
large change. Each step is optional and can ship on its own.

### Phase 1 — Reliability (highest value, lowest risk)

1. **Fix or retire dead sources.** Replace the Reuters endpoint with a working feed
   (or drop it), remove/replace the deprecated CoinGecko endpoint, and document that
   NewsAPI needs `NEWS_API_KEY`.
2. **Make failures visible.** Collect per-source success/failure into a small summary
   printed via `$GITHUB_STEP_SUMMARY`, so a broken feed is obvious without failing the
   whole job.
3. **Add a per-source item count** to `sources_used` (e.g. `{"BBC": 3, "NASA": 3}`) so
   silent zero-yield sources surface in the data itself.

### Phase 2 — Maintainability

4. **Extract the Python into a `scripts/` module** (e.g. `scripts/fetch_news.py`) and
   have the workflow call `python scripts/fetch_news.py`. Behavior stays identical.
5. **Add a `requirements.txt`** with pinned versions instead of an inline
   `pip install requests feedparser`.
6. **Add a minimal test** (e.g. feed parsing against a saved fixture) plus a lightweight
   lint step, so future changes are safe to review.

### Phase 3 — Quality nits (optional)

7. De-duplicate stories across runs by URL/title.
8. Derive categories per source instead of hard-coding, and strip HTML from descriptions.
9. Make the timezone configurable via an env var / workflow input.

## 4. Non-goals

To be explicit about what I'm **not** proposing:

- No change to the core concept (frequent commits / self-updating README).
- No new heavy dependencies or external services.
- No change to the commit cadence or the Actions schedule.

## 5. Suggested first step

If this direction sounds reasonable, I'd like to start with **Phase 1, step 1–2**
(fix/retire dead sources + a visible run summary) as a single small PR, so we can
validate the workflow before touching anything else.

## 6. Questions for the maintainer

1. Are Reuters/CoinGecko intended to be live, or leftovers you're fine dropping?
2. Is `Asia/Tehran` intentional, or should it be configurable?
3. Would you prefer the logic extracted into `scripts/`, or kept inline in the workflow?
4. Any preference on how many sources / items per run you want to keep?

Thanks again for the project, and for considering this. Happy to take it in whatever
direction works best for you.
