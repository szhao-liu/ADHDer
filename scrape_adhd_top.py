import csv
import time
from datetime import datetime, timezone
import praw

# --- PRAW client (use your own creds) ---
reddit = praw.Reddit(
    client_id="5MeWJU0dZaqsoLVSLou7eg",
    client_secret="01UiYKpR8UIGoyPFWtsIbAPbkQ_6IA",
    user_agent="ADHD-TopScraper/0.1 by /u/lawliu"
)

# --- Date range: March 1, 2020 (UTC) to now ---
start_ts = int(datetime(2020, 3, 1, tzinfo=timezone.utc).timestamp())
end_ts = int(time.time())

subreddit = reddit.subreddit("ADHD")

# Use Reddit search with a timestamp range and sort=top.
# Note: We rank by score; Reddit doesn't expose "upvotes" directly.
query = f"timestamp:{start_ts}..{end_ts}"

posts = []
for s in subreddit.search(query=query, sort="top", syntax="cloudsearch", limit=100):
    posts.append({
        "Title": s.title,
        "Author": str(s.author),
        "Score": int(s.score),
        "Created_UTC": s.created_utc,
        "Created": datetime.utcfromtimestamp(s.created_utc).strftime("%Y-%m-%d %H:%M:%S"),
        "Num_Comments": int(s.num_comments),
        "Permalink": f"https://www.reddit.com{s.permalink}",
        "URL": s.url,
        "ID": s.id
    })

# Just in case: sort again by score desc (highest first)
posts.sort(key=lambda x: x["Score"], reverse=True)

# Save to CSV
out_file = "adhd_top_2020toNow.csv"
with open(out_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["Title","Author","Score","Created","Created_UTC","Num_Comments","Permalink","URL","ID"]
    )
    writer.writeheader()
    writer.writerows(posts)

print(f"✅ Saved {len(posts)} posts to {out_file}")