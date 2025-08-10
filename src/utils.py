import os
from pathlib import Path
from dotenv import load_dotenv
import praw
    
def connect_to_reddit() -> praw.Reddit:
    load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    user_agent = os.getenv("USER_AGENT")
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    try:
        reddit.user.me()
        print("Connected to Reddit!")
    except Exception as e:
        print(f"Reddit connection failed: {e}")
        return None

    return reddit