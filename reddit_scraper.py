import praw
import csv

reddit = praw.Reddit(
    client_id="5MeWJU0dZaqsoLVSLou7eg",
    client_secret="01UiYKpR8UIGoyPFWtsIbAPbkQ_6IA",  # <-- replace this
    user_agent="SICSS-Stanford Project by /u/lawliu"  # <-- replace this
)

# Step 2: Choose the subreddit
subreddit = reddit.subreddit("ADHD")

# Step 3: Create the CSV file
with open("askreddit_posts.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Author", "Score", "Created_UTC", "Num_Comments", "URL"])

    # Step 4: Scrape up to ~1,000 recent posts
    for post in subreddit.new(limit=None):  # limit=None gets max allowed (~1000)
        writer.writerow([
            post.title,
            str(post.author),
            post.score,
            post.created_utc,
            post.num_comments,
            post.url
        ])

print("✅ Scraping complete! File saved as 'askreddit_posts.csv'")