import praw
import json
# Reddit API credentials
client_id = '649AXJYYAsZsR-YVS22dRw'
client_secret = 'TOL-0tZQ3l63z30HW3VrCiV9nz75hQ'
user_agent = 'DataCollectionScript by /u/Disaqx'
# Initialize Reddit API
reddit = praw.Reddit(client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent)
# Define search parameters
query = 'Elon or Trump or Hand'
subreddit_name = 'teslamotors' # You can specify a subreddit like 'technology'
max_posts = 1000 # Adjust as needed
# Collect submissions
posts = []
for submission in reddit.subreddit(subreddit_name).search(query, sort='new', 
limit=max_posts):
    posts.append({
    'title': submission.title,
    'selftext': submission.selftext,
    'author': str(submission.author),
    'created_utc': submission.created_utc,
    'score': submission.score,
    'url': submission.url,
    'num_comments': submission.num_comments,
    'subreddit': str(submission.subreddit),
    'id': submission.id
})
# Save data to a JSON file
with open('reddit_posts.json', 'w') as f:
    json.dump(posts, f, indent=2)