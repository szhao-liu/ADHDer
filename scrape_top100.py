import csv
from datetime import datetime
import praw

# --- Connect to Reddit API ---
reddit = praw.Reddit(
    client_id="5MeWJU0dZaqsoLVSLou7eg",
    client_secret="01UiYKpR8UIGoyPFWtsIbAPbkQ_6IA",
    user_agent="ADHD-TopScraper/0.1 by /u/lawliu",
    check_for_async=False
)

# --- Choose subreddit ---
subreddit = reddit.subreddit("ADHD")

# --- Collect top 100 posts (all-time) ---
posts = []
for submission in subreddit.top(time_filter="all", limit=100):
    posts.append({
        "Post_ID": submission.id,  # <-- this is the '1hf8k5t'
        "Title": submission.title,
        "Author": str(submission.author),
        "Score": submission.score,
        "Created": datetime.utcfromtimestamp(submission.created_utc).strftime("%Y-%m-%d %H:%M:%S"),
        "Comments": submission.num_comments,
        "Permalink": f"https://www.reddit.com{submission.permalink}",
        "URL": submission.url
    })

# --- Save to CSV ---
output_file = "adhd_top100_with_id.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["Post_ID", "Title", "Author", "Score", "Created", "Comments", "Permalink", "URL"]
    )
    writer.writeheader()
    writer.writerows(posts)

print(f"✅ Saved {len(posts)} posts to {output_file}")