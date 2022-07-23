from datetime import datetime
from enum import Enum
from dateutil.parser import parse
from typing import Union

# {
#   "login": "intervinn",
#   "id": 69168328,
#   "node_id": "MDQ6VXNlcjY5MTY4MzI4",
#   "avatar_url": "https://avatars.githubusercontent.com/u/69168328?v=4",
#   "gravatar_id": "",
#   "url": "https://api.github.com/users/intervinn",
#   "html_url": "https://github.com/intervinn",
#   "followers_url": "https://api.github.com/users/intervinn/followers",
#   "following_url": "https://api.github.com/users/intervinn/following{/other_user}",
#   "gists_url": "https://api.github.com/users/intervinn/gists{/gist_id}",
#   "starred_url": "https://api.github.com/users/intervinn/starred{/owner}{/repo}",
#   "subscriptions_url": "https://api.github.com/users/intervinn/subscriptions",
#   "organizations_url": "https://api.github.com/users/intervinn/orgs",
#   "repos_url": "https://api.github.com/users/intervinn/repos",
#   "events_url": "https://api.github.com/users/intervinn/events{/privacy}",
#   "received_events_url": "https://api.github.com/users/intervinn/received_events",
#   "type": "User",
#   "site_admin": false,
#   "name": null,
#   "company": null,
#   "blog": "",
#   "location": "Podolsk, Russia",
#   "email": null,
#   "hireable": null,
#   "bio": "hi\r\n",
#   "twitter_username": null,
#   "public_repos": 10,
#   "public_gists": 0,
#   "followers": 2,
#   "following": 2,
#   "created_at": "2020-08-03T19:32:14Z",
#   "updated_at": "2022-07-07T15:17:22Z"
# }

class User:
    
    def __init__(self, login: str =None, id: Union[str, int]=None, node_id: str=None, avatar_url: str=None, url: str=None, html_url: str=None,
    followers_url: str=None, following_url: str=None, gists_url: str=None, starred_url: str=None, subscriptions_url: str=None,
    organizations_url: str=None, repos_url: str=None, events_url: str=None, received_events_url: str=None, type: Enum=None, site_admin: Union[str, bool]=None,
    name: str=None, company: str=None, blog: str=None, location: str=None, email: str=None, hireable: Union[str, bool]=None, bio: str=None, twitter_username: str=None, public_repos:Union[str, int]=None,
    public_gists:Union[str, int]=None, followers:Union[str, int]=None, following:Union[str, int]=None, created_at:datetime=None, updated_at:datetime=None, dict: dict = None):
        self.login = login
        self.id = id
        self.node_id = node_id
        self.avatar_url = avatar_url
        self.url = url
        self.html_url = html_url
        self.followers_url = followers_url
        self.following_url = following_url
        self.gists_url = gists_url
        self.starred_url = starred_url
        self.subscriptions_url = subscriptions_url
        self.organizations_url = organizations_url
        self.repos_url = repos_url
        self.events_url = events_url
        self.received_events_url = received_events_url
        self.type = type
        self.site_admin = site_admin
        self.name = name
        self.company = company
        self.blog = blog
        self.location = location
        self.email = email
        self.hireable = hireable
        self.bio = bio
        self.twitter_username = twitter_username
        self.public_repos = public_repos
        self.public_gists = public_gists
        self.followers = followers
        self.following = following
        self.created_at = parse(created_at)
        self.updated_at = parse(updated_at)
        self.dict = dict

