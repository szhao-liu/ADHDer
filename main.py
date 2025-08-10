from datetime import datetime
import argparse

from src.scrape_top_posts import scrape_top_posts_run
from src.scrape_all_comments import scrape_all_comments_run


def parse_cmd():
    # Parse command line arguments for scraping
    parser = argparse.ArgumentParser(description="Scrape Reddit posts and comments.")
    parser.add_argument("--subreddit", type=str, default="ADHD", help="Subreddit display name")
    parser.add_argument("--limit", type=int, default=2, help="Number of posts to scrape. Maximum is 1000.")
    parser.add_argument("--start-date", type=str, default="2020-03-01", help="Start date (YYYY-MM-DD) of post creation")
    parser.add_argument("--end-date", type=str, default="2025-08-01", help="End date (YYYY-MM-DD) of post creation")

    args = parser.parse_args()
    
    return args

def main():
    # Parse command line arguments for scraping
    args = parse_cmd()  
    
    # Scrape top posts
    posts_csv = scrape_top_posts_run(
        subreddit_display_name=args.subreddit,
        limit=args.limit,
        start_ts=datetime.strptime(args.start_date, "%Y-%m-%d"),  # Format as year-m-d
        end_ts=datetime.strptime(args.end_date, "%Y-%m-%d")
    )

    # Scrape top posts w/o time filtering
    # scrape_top_posts_run(subreddit_display_name=args.subreddit, limit=args.limit)

    # Scrape all comments
    comments_csv = scrape_all_comments_run(posts_csv=posts_csv)

if __name__ == "__main__":
    main()