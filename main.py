import feedparser
from datetime import date
import os

def fetch_entries(rss_urls, max_per_feed=3):
    """Fetch recent entries from multiple RSS feeds."""
    entries = []
    for url in rss_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_per_feed]:
            entries.append({
                'title': entry.get('title', ''),
                'link': entry.get('link', ''),
                'published': entry.get('published', '')
            })
    return entries

def summarize_with_llm(entries, api_key=None):
    """Simple LLM call to generate a daily digest summary (mock if no key)."""
    if not api_key:
        # Mock summary: just list titles
        return "\n".join(f"- {e['title']} ({e['published']})" for e in entries)
    # In real use, call OpenAI/Anthropic here
    return "Generated digest via LLM"

def generate_daily_digest():
    rss_urls = [
        "https://hnrss.org/frontpage",
        "https://feeds.bbci.co.uk/news/technology/rss.xml"
    ]
    entries = fetch_entries(rss_urls)
    api_key = os.getenv("OPENAI_API_KEY")  # optional
    digest = summarize_with_llm(entries, api_key)
    today = date.today().isoformat()
    report = f"# Daily Digest {today}\n\n{digest}"
    # Write to file
    with open(f"digest_{today}.md", "w") as f:
        f.write(report)
    print(f"Generated digest_{today}.md with {len(entries)} items")

if __name__ == "__main__":
    # Add feedparser: pip install feedparser
    generate_daily_digest()
