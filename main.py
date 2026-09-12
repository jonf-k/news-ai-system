import feedparser

RSS_URL = "https://news.google.com/rss?hl=ja&gl=JP&ceid=JP:ja"

feed = feedparser.parse(RSS_URL)

print("取得したニュース数:", len(feed.entries))

for i, entry in enumerate(feed.entries[:10], 1):
    print(f"{i}. {entry.title}")
    print(entry.link)
    print()
