import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import feedparser

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import fetch_news  # noqa: E402

FIXTURE = Path(__file__).parent / "fixtures" / "sample_rss.xml"
NOW = datetime(2026, 7, 28, 12, 0, 0, tzinfo=ZoneInfo("Asia/Tehran"))


def _parse_fixture():
    return feedparser.parse(FIXTURE.read_text(encoding="utf8"))


def test_rss_items_maps_fields():
    parsed = _parse_fixture()
    items = fetch_news.rss_items(parsed, "BBC", "world", NOW)

    assert len(items) == 3  # limit=3 applied
    first = items[0]
    assert first["source"] == "BBC"
    assert first["category"] == "world"
    assert first["title"] == "First headline"
    assert first["description"] == "Summary of the first story."
    assert first["url"] == "https://example.com/first"
    assert first["published"] == "Mon, 28 Jul 2026 09:00:00 GMT"
    assert first["fetched"] == "2026-07-28T12:00:00+03:30"


def test_rss_items_respects_limit():
    parsed = _parse_fixture()
    assert len(fetch_news.rss_items(parsed, "BBC", "world", NOW, limit=2)) == 2


def test_rss_items_defaults_on_empty_feed():
    empty = feedparser.parse("<rss version='2.0'><channel></channel></rss>")
    assert fetch_news.rss_items(empty, "BBC", "world", NOW) == []


def test_build_news_data_shape():
    items = fetch_news.rss_items(_parse_fixture(), "BBC", "world", NOW)
    data = fetch_news.build_news_data(items, NOW)

    assert data["timezone"] == "Asia/Tehran"
    assert data["total_news"] == 3
    assert data["sources_used"] == ["BBC"]
    assert data["news"] == items


def test_fetch_newsapi_no_key_is_noop():
    assert fetch_news.fetch_newsapi("", NOW) == []


def test_render_readme_contains_titles_and_header():
    items = fetch_news.rss_items(_parse_fixture(), "BBC", "world", NOW)
    readme = fetch_news.render_readme(items, NOW)

    assert readme.startswith("# 📰 Daily News Bot - 48+ Commits Daily")
    assert "**Total News:** 3" in readme
    assert "### 1. First headline" in readme
    assert "**Source:** BBC" in readme
    assert readme.rstrip().endswith("**Built with ❤️ by GitHub Actions**")


def test_update_stats_creates_and_appends():
    items = fetch_news.rss_items(_parse_fixture(), "BBC", "world", NOW)

    created = fetch_news.update_stats("does-not-exist.json", "2026-07-28", "12-00", items)
    assert created["date"] == "2026-07-28"
    assert created["total_news"] == 3
    assert len(created["commits"]) == 1
    assert created["commits"][0]["time"] == "12-00"
    assert created["commits"][0]["news_count"] == 3
