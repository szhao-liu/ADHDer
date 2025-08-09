# ADHDer

How reddit users with ADHD talk about social media use and time management

## Resources

- Data source: [Reddit: ADHDer](https://www.reddit.com/r/ADHD/)
- Scraping tools
  - [Arctic Shift](https://github.com/ArthurHeitmann/arctic_shift)
  - [PRAW](https://praw.readthedocs.io/en/stable/index.html)

## Set up

1. Clone the repository
2. Set up [Reddit API credentials](https://praw.readthedocs.io/en/stable/getting_started/authentication.html#password-flow): Get your Reddit API keys ([How to Get Your API Keys in 2024](https://www.youtube.com/watch?v=0mGpBxuYmpU)) and add your credentials to a `.env` file in the root directory.

```bash
# Clone repository and navigate to the directory
git clone https://github.com/szhao-liu/ADHDer.git
cd ADHDer

# Run the application
```

## Pipeline

1. Data Collection
   - Use the scraping tools to collect data from r/ADHD.
   - PRAW -> Top 1000 posts' IDs
   - Arctic Shift -> all comments from the top 1000 posts
   - Store the raw data in the `data/raw` directory.

2. Data Processing
   - Distribution of the lengths of comments
   - xxx

3. Analysis
   - xxx
