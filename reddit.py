import os
import praw
from dotenv import load_dotenv

load_dotenv()


reddit = praw.Reddit(
    client_id=os.environ.get('client_id'),
    client_secret=os.environ.get('client_secret'),
    password=os.environ.get('password'),
    user_agent=os.environ.get('user_agent'),
    username=os.environ.get('username'),
)


def get_post_texts(post):
    """
        returning dictionary with id: post id,texts: all texts in post with upvotes and dates
    """
    post_info = { 'id' : post.id, 'texts' : [] }
    
    post_info['texts'].append({
        'date': post.created_utc,
        'text': text, 
        'upvotes': post.score,
        'main': True
    })
    post.comments.replace_more(limit=None)
    comments = post.comments.list()
    for comment in comments:
        com_text = comment.body
        post_info['texts'].append({
            'date': comment.created_utc,
            'text': com_text,
            'upvotes': comment.score
        })
        
    return post_info