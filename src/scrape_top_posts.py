from datetime import datetime
from pathlib import Path
import praw

from tqdm import tqdm
from typing import Any, List, Dict
from .utils import connect_to_reddit


def get_top_posts(reddit: praw.Reddit, display_name: str, limit: int = 1000, start_ts: datetime = None, end_ts: datetime = None) -> List[Dict[str, Any]]:
    """Fetches the top posts from a specified subreddit with optional time filtering, and saves the posts to a CSV file.

    Args:
        reddit (praw.Reddit): Reddit API client.
        display_name (str): Subreddit display name.
        limit (int, optional): Number of posts to fetch. Defaults to 1000. Max 1000 based on the limit of the Reddit API.

    Returns:
        List[Dict[str, Any]]: List of top posts.
    """

    subreddit = reddit.subreddit(display_name)

    posts_data = []
    for submission in tqdm(subreddit.top(time_filter="all", limit=limit), total=limit, desc=f"Fetching top {limit} posts"):
        # Filter by timestamp
        if start_ts and submission.created_utc < start_ts.timestamp(): continue
        if end_ts and submission.created_utc > end_ts.timestamp(): continue
        posts_data.append({
            "post_id": submission.id,
            "title": submission.title,
            "author": str(submission.author),
            "upvotes": submission.score,
            "created": datetime.fromtimestamp(submission.created_utc).strftime("%Y-%m-%d %H:%M:%S"),
            "num_comments": submission.num_comments,
            "post_text": submission.selftext,
            "upvote_ratio": submission.upvote_ratio,
            "url": submission.url,
            "archived": submission.archived,
            "locked": submission.locked
        })
        
    return posts_data


def scrape_top_posts_run(subreddit_display_name: str = "ADHD", limit: int = 1000, start_ts: datetime = None, end_ts: datetime = None) -> str:
    """Connects to the Reddit API, fetches the top posts from a specified subreddit with
    optional time filtering, and saves the posts to a CSV file.

    Args:
        subreddit_display_name (str, optional): Subreddit display name. Defaults to "ADHD".
        limit (int, optional): Number of posts to fetch. Defaults to 1000.
        start_ts (datetime, optional): Start timestamp for filtering posts. Defaults to None.
        end_ts (datetime, optional): End timestamp for filtering posts. Defaults to None.
    """
    print(f"🔍 Scraping top {limit} posts from r/{subreddit_display_name} with time filtering: {start_ts} to {end_ts}")
    reddit = connect_to_reddit()
    posts = get_top_posts(reddit, subreddit_display_name, limit=limit, start_ts=start_ts, end_ts=end_ts)
    
    assert len(posts) > 0, "No posts found."

    # Write posts into a CSV
    import csv
    time_filter = f"{start_ts.strftime('%Y-%m-%d')}_{end_ts.strftime('%Y-%m-%d')}" if start_ts and end_ts else "all_time"
    output_file = f"{subreddit_display_name}_top{limit}posts_{time_filter}.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=posts[0].keys())
        writer.writeheader()
        writer.writerows(posts)

    print(f"✅ Saved {len(posts)} posts to {Path(output_file).resolve()} \n")
    
    return str(Path(output_file).resolve())


if __name__ == "__main__":
    # Example usage:
    # format as y-m-d
    start_ts = datetime.strptime("2020-03-01", "%Y-%m-%d")
    end_ts = datetime.strptime("2025-08-01", "%Y-%m-%d")

    # Scrape posts with time filtering
    scrape_top_posts_run(subreddit_display_name="ADHD", limit=2, start_ts=start_ts, end_ts=end_ts)

    # No time filtering
    # scrape_top_posts_run(subreddit_display_name="ADHD", limit=2)
