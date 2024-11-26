import praw
from decouple import config

reddit = praw.Reddit(
    client_id=config('REDDIT_CLIENT_ID'),
    client_secret=config('REDDIT_CLIENT_SECRET'),
    user_agent=config('REDDIT_USER_AGENT')
)

def get_popular_posts(subreddit="memes", limit=10):
    print('Getting posts of reddit', subreddit)
    subreddit = reddit.subreddit(subreddit)
    posts = []
    for submission in subreddit.hot(limit=limit):
        if not submission.stickied:  # Skip pinned posts
            posts.append({
                "title": submission.title,
                "url": submission.url,
                "score": submission.score,
                "num_comments": submission.num_comments
            })
    return posts
