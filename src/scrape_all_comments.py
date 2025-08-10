from pathlib import Path
from datetime import datetime
import praw
import csv

from tqdm import tqdm
from .utils import connect_to_reddit


def get_all_comments_for_posts(reddit: praw.Reddit, post_ids: list[str], output_file: str):
    """
    Given a list of post IDs, fetch all comments for each post and save to a CSV file.
    """
    # Fetch comments for each post
    comments_data = []
    for post_id in tqdm(post_ids, desc=f"Fetching comments for {len(post_ids)} posts"):
        # Update the comment forest by resolving instances of MoreComments.
        submission = reddit.submission(id=post_id)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            # link_id
            comments_data.append({
                "post_id": post_id,
                "comment_id": comment.id,
                "author": str(comment.author),
                "created": datetime.fromtimestamp(comment.created_utc).strftime("%Y-%m-%d %H:%M:%S"),
                "body": comment.body,
                "score": comment.score,
                "parent_id": comment.parent_id,
                "is_submitter": getattr(comment, "is_submitter", False),
                "permalink": comment.permalink,
                "url": f"https://www.reddit.com{comment.permalink}",
                "link_id": comment.link_id
            })

    # Save comments to CSV
    assert len(comments_data) > 0, "No comments found."
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=comments_data[0].keys())
        writer.writeheader()
        writer.writerows(comments_data)
    print(
        f"✅ Saved {len(comments_data)} comments to {Path(output_file).resolve()}")


def scrape_all_comments_run(posts_csv: str) -> str:
    print(f"🔍 Scraping all comments for posts listed in {posts_csv}")
    # Connect to Reddit
    reddit = connect_to_reddit()

    # Read post IDs from the posts CSV
    with open(posts_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        post_ids = [row["post_id"] for row in reader if row.get("post_id")]

    # Generate output file name by inserting "comment" before the file extension
    posts_path = Path(posts_csv)
    output_file = posts_path.with_name(posts_path.stem + "_comments" + posts_path.suffix)

    get_all_comments_for_posts(reddit, post_ids, str(output_file))

    return str(output_file)


if __name__ == "__main__":
    # Example usage:
    posts_csv = "./ADHD_top2posts_all_time.csv"
    scrape_all_comments_run(posts_csv)
