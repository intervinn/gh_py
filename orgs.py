from datetime import datetime
from typing import Union
from dateutil.parser import parse
import aiohttp

class Organization:
    
    def __init__(self, login: str = None, id: Union[str, int] = None, node_id: str = None, url: str = None, repos_url: str = None, events_url: str = None,
    hooks_url: str = None, issues_url: str = None, members_url: str = None, public_members_url: str = None, avatar_url: str = None,
    description: str = None, name: str = None, company: str = None, blog: str = None, location: str = None, email: str = None, twitter_username: str = None,
    is_verified: Union[str, bool] = None, has_organization_projects: Union[str, bool] = None, has_repository_projects: Union[str, bool] = None, public_repos: Union[str, int] = None,
    public_gists: Union[str, int] = None, followers: Union[str, int] = None, following: Union[str, int] = None, html_url: str = None, created_at: datetime = None, updated_at: datetime = None, type: str = None) -> None:
        self.login = login
        self.id = id
        self.node_id = node_id
        self.url = url
        self.repos_url = repos_url
        self.events_url = events_url
        self.hooks_url = hooks_url
        self.issues_url = issues_url
        self.members_url = members_url
        self.public_members_url = public_members_url
        self.avatar_url = avatar_url
        self.description = description
        self.name = name
        self.company = company
        self.blog = blog
        self.location = location
        self.email = email
        self.twitter_username = twitter_username
        self.is_verified = is_verified
        self.has_organization_projects = has_organization_projects
        self.has_repository_projects = has_repository_projects
        self.public_repos = public_repos
        self.public_gists = public_gists
        self.followers = followers
        self.following = following
        self.html_url = html_url
        self.created_at = parse(created_at)
        self.updated_at = parse(updated_at)
        self.type = type


# l = {
#   "login": "checkit-dev",
#   "id": 102682454,
#   "node_id": "O_kgDOBh7PVg",
#   "url": "https://api.github.com/orgs/checkit-dev",
#   "repos_url": "https://api.github.com/orgs/checkit-dev/repos",
#   "events_url": "https://api.github.com/orgs/checkit-dev/events",
#   "hooks_url": "https://api.github.com/orgs/checkit-dev/hooks",
#   "issues_url": "https://api.github.com/orgs/checkit-dev/issues",
#   "members_url": "https://api.github.com/orgs/checkit-dev/members{/member}",
#   "public_members_url": "https://api.github.com/orgs/checkit-dev/public_members{/member}",
#   "avatar_url": "https://avatars.githubusercontent.com/u/102682454?v=4",
#   "description": "",
#   "name": "Check it",
#   "company": null,
#   "blog": null,
#   "location": null,
#   "email": null,
#   "twitter_username": null,
#   "is_verified": false,
#   "has_organization_projects": true,
#   "has_repository_projects": true,
#   "public_repos": 0,
#   "public_gists": 0,
#   "followers": 0,
#   "following": 0,
#   "html_url": "https://github.com/checkit-dev",
#   "created_at": "2022-03-30T15:36:50Z",
#   "updated_at": "2022-03-30T17:13:08Z",
#   "type": "Organization"