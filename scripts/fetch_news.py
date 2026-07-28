"""Fetch news from multiple sources and render the repo's README / stats.

This module is a straight extraction of the Python that previously lived inside
`.github/workflows/news-bot.yml` as a heredoc. The behavior is intentionally
identical: same sources, same order, same field mappings, same output files.

The logic is split into small, pure functions (``rss_items``, ``render_readme``,
...) so it can be unit-tested against fixtures without hitting the network, while
``main()`` performs the actual I/O exactly as the workflow used to.
"""

import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

import feedparser
import requests

TIMEZONE = "Asia/Tehran"

CATEGORIES = [
    "technology",
    "science",
    "health",
    "business",
    "entertainment",
    "sports",
]

RSS_SOURCES = [
    ("Hacker News", "https://hnrss.org/frontpage?count=5", "technology"),
    ("Reuters", "https://feeds.reuters.com/Reuters/worldNews", "world"),
    ("BBC", "http://feeds.bbci.co.uk/news/rss.xml", "world"),
    ("Al Jazeera", "https://www.aljazeera.com/xml/rss/all.xml", "world"),
]


def _fetched_stamp(now):
    return now.isoformat(timespec="seconds")


def rss_items(parsed, source, category, now, limit=3):
    """Map a parsed feed (feedparser result) into news items.

    Pure function: no network, no globals. Mirrors the original heredoc mapping.
    """
    items = []
    for entry in parsed.entries[:limit]:
        items.append({
            "source": source,
            "category": category,
            "title": entry.get("title", "No title"),
            "description": entry.get("summary", ""),
            "url": entry.get("link", "#"),
            "published": entry.get("published", ""),
            "fetched": _fetched_stamp(now),
        })
    return items


def fetch_rss(source, url, category, now, limit=3):
    """Fetch and parse a single RSS source, swallowing errors like the original."""
    try:
        parsed = feedparser.parse(url)
        return rss_items(parsed, source, category, now, limit=limit)
    except Exception as e:  # noqa: BLE001 - preserve original best-effort behavior
        print(f"{source} error: {e}")
        return []


def fetch_newsapi(api_key, now):
    """Fetch NewsAPI top-headlines per category (no-op when key is unset)."""
    items = []
    if not api_key:
        return items
    for category in CATEGORIES:
        try:
            url = (
                "https://newsapi.org/v2/top-headlines?country=us"
                f"&category={category}&apiKey={api_key}&pageSize=2"
            )
            response = requests.get(url, timeout=10)
            data = response.json()
            if data.get("status") == "ok":
                for article in data.get("articles", []):
                    items.append({
                        "source": "NewsAPI",
                        "category": category,
                        "title": article.get("title", "No title"),
                        "description": article.get("description", ""),
                        "url": article.get("url", "#"),
                        "published": article.get("publishedAt", ""),
                        "fetched": _fetched_stamp(now),
                    })
        except Exception as e:  # noqa: BLE001
            print(f"NewsAPI {category} error: {e}")
    return items


def fetch_coingecko(now):
    items = []
    try:
        crypto_response = requests.get(
            "https://api.coingecko.com/api/v3/news", timeout=10
        )
        crypto_data = crypto_response.json()
        for article in crypto_data.get("data", [])[:3]:
            items.append({
                "source": "CoinGecko",
                "category": "crypto",
                "title": article.get("title", "No title"),
                "description": article.get("description", ""),
                "url": article.get("url", "#"),
                "published": article.get("created_at", ""),
                "fetched": _fetched_stamp(now),
            })
    except Exception as e:  # noqa: BLE001
        print(f"CoinGecko error: {e}")
    return items


def fetch_nasa(now):
    items = []
    try:
        nasa_response = requests.get(
            "https://eonet.gsfc.nasa.gov/api/v3/events?limit=5", timeout=10
        )
        nasa_data = nasa_response.json()
        for event in nasa_data.get("events", [])[:3]:
            items.append({
                "source": "NASA",
                "category": "nature",
                "title": event.get("title", "No title"),
                "description": "Natural event: "
                + str(event.get("categories", [{}])[0].get("title", "Unknown")),
                "url": event.get("link", "#"),
                "published": event.get("geometry", [{}])[0].get("date", ""),
                "fetched": _fetched_stamp(now),
            })
    except Exception as e:  # noqa: BLE001
        print(f"NASA error: {e}")
    return items


def collect_news(now, api_key):
    """Gather items from every source in the original workflow order."""
    all_news = []
    all_news.extend(fetch_newsapi(api_key, now))
    for source, url, category in RSS_SOURCES:
        all_news.extend(fetch_rss(source, url, category, now))
    all_news.extend(fetch_coingecko(now))
    all_news.extend(fetch_nasa(now))
    return all_news


def build_news_data(all_news, now):
    return {
        "update_time": now.isoformat(timespec="seconds"),
        "timezone": TIMEZONE,
        "total_news": len(all_news),
        "sources_used": list(set([n["source"] for n in all_news])),
        "news": all_news,
    }


def render_readme(all_news, now):
    """Render the README markdown. Pure function, byte-identical to the original."""
    readme_lines = []
    readme_lines.append("# 📰 Daily News Bot - 48+ Commits Daily")
    readme_lines.append("")
    readme_lines.append("**Last Update:** " + now.strftime("%Y-%m-%d %H:%M:%S"))
    readme_lines.append("")
    readme_lines.append("**Total News:** " + str(len(all_news)))
    readme_lines.append("")
    readme_lines.append("**Sources:** " + ", ".join(set([n["source"] for n in all_news])))
    readme_lines.append("")
    readme_lines.append("---")
    readme_lines.append("")
    readme_lines.append("## 📰 Latest News")
    readme_lines.append("")

    for i, news in enumerate(all_news, 1):
        readme_lines.append("### " + str(i) + ". " + news["title"])
        readme_lines.append("")
        readme_lines.append("**Source:** " + news["source"])
        readme_lines.append("")
        readme_lines.append("**Category:** " + news["category"])
        readme_lines.append("")
        if news["description"] and news["description"] != "":
            readme_lines.append("**Description:**")
            readme_lines.append(news["description"])
            readme_lines.append("")
        readme_lines.append("🔗 **Read more:** [" + news["url"] + "](" + news["url"] + ")")
        readme_lines.append("")
        readme_lines.append("---")
        readme_lines.append("")

    readme_lines.append("")
    readme_lines.append("**Built with ❤️ by GitHub Actions**")

    return "\n".join(readme_lines)


def update_stats(stats_file, date_str, time_str, all_news):
    """Append this run to the daily stats file, creating it if needed."""
    try:
        with open(stats_file, encoding="utf8") as f:
            stats = json.load(f)
    except FileNotFoundError:
        stats = {"date": date_str, "commits": [], "total_news": 0}

    stats["commits"].append({
        "time": time_str,
        "news_count": len(all_news),
        "sources": list(set([n["source"] for n in all_news])),
    })
    stats["total_news"] += len(all_news)
    return stats


def main():
    tz = ZoneInfo(TIMEZONE)
    now = datetime.now(tz)
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M")

    api_key = os.environ.get("NEWS_API_KEY", "")
    all_news = collect_news(now, api_key)

    os.makedirs(f"news/{date_str}", exist_ok=True)
    filename = f"news/{date_str}/{time_str}.json"

    news_data = build_news_data(all_news, now)
    with open(filename, "w", encoding="utf8") as f:
        json.dump(news_data, f, indent=4, ensure_ascii=False)

    readme_text = render_readme(all_news, now)
    with open("README.md", "w", encoding="utf8") as f:
        f.write(readme_text)

    log_entry = now.isoformat(timespec="seconds") + " | " + str(len(all_news)) + " news"
    with open("commit-log.txt", "a", encoding="utf8") as f:
        f.write(log_entry + "\n")

    os.makedirs("stats", exist_ok=True)
    stats_file = "stats/" + date_str + ".json"
    stats = update_stats(stats_file, date_str, time_str, all_news)
    with open(stats_file, "w", encoding="utf8") as f:
        json.dump(stats, f, indent=4, ensure_ascii=False)

    print("Saved " + str(len(all_news)) + " news items")


if __name__ == "__main__":
    main()
