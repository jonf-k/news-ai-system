import os
import feedparser
from huggingface_hub import InferenceClient

RSS_URL = "https://news.google.com/rss?hl=ja&gl=JP&ceid=JP:ja"

# ニュース取得
feed = feedparser.parse(RSS_URL)

print("取得したニュース数:", len(feed.entries))

# 最初の10件を表示
for i, entry in enumerate(feed.entries[:10], 1):
    print(f"{i}. {entry.title}")
    print(entry.link)
    print()

# Hugging Face AI
client = InferenceClient(
    token=os.environ["HF_TOKEN"],
    model="openai/gpt-oss-20b"
)

prompt = """
あなたはニュース選別AIです。

以下のニュース一覧から、
日本への影響、経済への影響、企業への影響、
社会的な重要性、今後の展開の大きさを考慮して、
特に重要なニュースを3件選んでください。

各ニュースについて、
「順位」「ニュースタイトル」「重要な理由」
を簡潔に出してください。

ニュース一覧:
"""

for i, entry in enumerate(feed.entries[:10], 1):
    prompt += f"{i}. {entry.title}\n"

response = client.chat_completion(
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    max_tokens=500,
    temperature=0.2
)

print("===== AIによる重要ニュース選別 =====")
print(response.choices[0].message.content)
