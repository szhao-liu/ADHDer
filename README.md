# ADHDer

How reddit users with ADHD talk about social media use and time management

## Resources

- Data source: [Reddit: ADHDer](https://www.reddit.com/r/ADHD/)
- Reddit scraping tools
  - [PRAW](https://praw.readthedocs.io/en/stable/index.html)
  - [Arctic Shift](https://github.com/ArthurHeitmann/arctic_shift)

Additional resources:
- [Python Reddit API Wrapper (PRAW) Documentation](https://praw.readthedocs.io/en/stable/)
- [Reddit API Documentation](https://www.reddit.com/dev/api)
- [How to Get Reddit API Key: Finally, a Guide That Works](https://data365.co/blog/how-to-get-reddit-api-key)

## Set up & run

1. API set up
   1. Set up [Reddit API credentials](https://praw.readthedocs.io/en/stable/getting_started/authentication.html#password-flow): Get your Reddit API keys ([How to Get Your API Keys in 2024](https://www.youtube.com/watch?v=0mGpBxuYmpU)) 
   2. Create a `.env` file in the root directory `ADHDer/` and add your credentials in it.

   ```
   # ADHDer/env
   # Reddit API credentials
   CLIENT_ID=YOUR_CLIENT_ID
   CLIENT_SECRET=YOUR_CLIENT_SECRET
   USER_AGENT=ADHD_reddit_scraper
   ```

2. Run the following command lines to scrape reddit data:

```bash
# Clone repository and navigate to the directory
git clone https://github.com/szhao-liu/ADHDer.git
cd ADHDer

# Install dependencies
poetry install --no-root

# Run the scraping script with default arguments
# defaults: --subreddit ADHD --limit 2 --start-date 2020-03-01 --end-date 2025-08-01
# The default arguments means it will scrape the top 2 posts from the ADHD subreddit within the date range from 2020-03-01 to 2025-08-01
poetry run python main.py

# Run with command-line arguments
# example: this command will scrape the top 100 posts from the ADHD subreddit then filter posts within the time frame from 2020-03-01 to 2025-08-01
poetry run python main.py --subreddit ADHD --limit 100 --start-date 2020-03-01 --end-date 2025-08-01
```

Other usage:

- Subreddit -> top post within a time frame
- top posts -> all comments

```bash
# Edit the script to control the scraping process
# Subreddit -> top post within a time frame
poetry run python -m src.scrape_top_posts

# top posts -> all comments 
poetry run python -m src.scrape_all_comments
```

## Pipeline

1. Data Collection
   - Use the scraping tools to collect data from r/ADHD.
   - PRAW -> Top 1000 posts' IDs -> select 100 posts -> all comments from the 100 posts
   - Store the raw data in csv files.

2. Data Processing
   - Distribution of the lengths of comments
   - Preprocessing text
     - English only

3. Analysis
   - xxx
