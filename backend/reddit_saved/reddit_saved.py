import praw
import smtplib, ssl
import random
from uuid import uuid4
from reddit_saved.models import userinfo, savedposts
import os

'https://github.com/reddit-archive/reddit/wiki/OAuth2-Python-Example'
#code flow is the auth I think I want and the redirect URI 
#If you are running a website you will want to enter the appropriate callback
# URL and configure that endpoint to complete the code flow.
# session['CLIENT_ID'] = 'MPmqNHM5wTbnzA'
# session['CLIENT_SECRET'] = ''

class reddit_saved:
    def __init__(self, refresh_token = None):
        self.app_secret = 'XMJljCPdnA21Go0aolRedD4o7HIbSw'
        self.app_id = 'MPmqNHM5wTbnzA'
        self.app_agent = ("reddit-saved-web-app 1.0 by /u/arun1995plus1")
        self.REDIRECT_URI = "http://127.0.0.1:65010/reddit_callback"
        self.refresh_token = refresh_token
        
        self.reddit = praw.Reddit(client_id = self.app_id,
                    client_secret = self.app_secret,
                    user_agent = self.app_agent,
                     redirect_uri=self.REDIRECT_URI,
                     refresh_token = self.refresh_token
        )
        
        self.scopes = {"creddits": {"description": "Spend my reddit gold creddits on giving gold to other users.", "id": "creddits", "name": "Spend reddit gold creddits"}, "modcontributors": {"description": "Add/remove users to approved user lists and ban/unban or mute/unmute users from subreddits I moderate.", "id": "modcontributors", "name": "Approve and ban users"}, "modmail": {"description": "Access and manage modmail via mod.reddit.com.", "id": "modmail", "name": "New Modmail"}, "modconfig": {"description": "Manage the configuration, sidebar, and CSS of subreddits I moderate.", "id": "modconfig", "name": "Moderate Subreddit Configuration"}, "subscribe": {"description": "Manage my subreddit subscriptions. Manage \"friends\" - users whose content I follow.", "id": "subscribe", "name": "Edit My Subscriptions"}, "structuredstyles": {"description": "Edit structured styles for a subreddit I moderate.", "id": "structuredstyles", "name": "Edit structured styles"}, "vote": {"description": "Submit and change my votes on comments and submissions.", "id": "vote", "name": "Vote"}, "wikiedit": {"description": "Edit wiki pages on my behalf", "id": "wiki", "name": "Wiki Editing"}, "mysubreddits": {"description": "Access the list of subreddits I moderate, contribute to, and subscribe to.", "id": "mysubreddits", "name": "My Subreddits"}, "submit": {"description": "Submit links and comments from my account.", "id": "submit", "name": "Submit Content"}, "modlog": {"description": "Access the moderation log in subreddits I moderate.", "id": "modlog", "name": "Moderation Log"}, "modposts": {"description": "Approve, remove, mark nsfw, and distinguish content in subreddits I moderate.", "id": "modposts", "name": "Moderate Posts"}, "modflair": {"description": "Manage and assign flair in subreddits I moderate.", "id": "modflair", "name": "Moderate Flair"}, "save": {"description": "Save and unsave comments and submissions.", "id": "save", "name": "Save Content"}, "modothers": {"description": "Invite or remove other moderators from subreddits I moderate.", "id": "modothers", "name": "Invite or remove other moderators"}, "read": {"description": "Access posts and comments through my account.", "id": "read", "name": "Read Content"}, "privatemessages": {"description": "Access my inbox and send private messages to other users.", "id": "privatemessages", "name": "Private Messages"}, "report": {"description": "Report content for rules violations. Hide & show individual submissions.", "id": "report", "name": "Report content"}, "identity": {"description": "Access my reddit username and signup date.", "id": "identity", "name": "My Identity"}, "livemanage": {"description": "Manage settings and contributors of live threads I contribute to.", "id": "livemanage", "name": "Manage live threads"}, "account": {"description": "Update preferences and related account information. Will not have access to your email or password.", "id": "account", "name": "Update account information"}, "modtraffic": {"description": "Access traffic stats in subreddits I moderate.", "id": "modtraffic", "name": "Subreddit Traffic"}, "wikiread": {"description": "Read wiki pages through my account", "id": "wikiread", "name": "Read Wiki Pages"}, "edit": {"description": "Edit and delete my comments and submissions.", "id": "edit", "name": "Edit Posts"}, "modwiki": {"description": "Change editors and visibility of wiki pages in subreddits I moderate.", "id": "modwiki", "name": "Moderate Wiki"}, "modself": {"description": "Accept invitations to moderate a subreddit. Remove myself as a moderator or contributor of subreddits I moderate or contribute to.", "id": "modself", "name": "Make changes to your subreddit moderator and contributor status"}, "history": {"description": "Access my voting history and comments or submissions I've saved or hidden.", "id": "history", "name": "History"}, "flair": {"description": "Select my subreddit flair. Change link flair on my submissions.", "id": "flair", "name": "Manage My Flair"}}
        self.sender_email = os.environ.get('SENDER_EMAIL')
        self._sender_email_password = os.environ.get('SENDER_EMAIL_PASSWORD')
        

    def make_authorization_url(self):
        # Generate a random string for the state parameter
        # Save it for use later to prevent xsrf attacks
        stateValue = str(uuid4()) 
        redditScopes= [
            'identity', 'save',
            'mysubreddits', 'read',
            'account', 'history'
            ]
        url= self.reddit.auth.url(redditScopes, stateValue, 'permanent')
        return url
        

    def get_saved_posts(self, username):
        saved=[]
        for i, item in enumerate(self.reddit.user.me().saved(limit=None)):
            saved_obj = savedposts(
                id = f'{username}-{i+1}',
                username = username,
                email = '',
                post_id = item.id,
                score = item.score,
                permalink = item.permalink
                )
            saved.append(saved_obj)

        return saved
        
    def email_user(self, user_email, posts, port = 465):
        sender_email = self.sender_email
        password = self._sender_email_password
        context = ssl.create_default_context()
        posts = [f'https://reddit.com{posts[k]}' for k in range(len(posts))]

        message = f"""\
        Subject: Hi there its your reddit saved posts emailing you!
        check this out!

        {posts[0]}
        {posts[1]}
        {posts[2]}
        {posts[3]}
        {posts[4]}

        This message is sent from Python."""

        with smtplib.SMTP_SSL("smtp.gmail.com", 
                            port, 
                            context = context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, user_email, message)

        return 'Email Sent'
