import aiohttp
from orgs import Organization
from users import User
from dateutil.parser import parse

class Client:

    def __init__(self) -> None:
        pass

        # self.login = login
        # self.id = id
        # self.node_id = node_id
        # self.url = url
        # self.repos_url = repos_url
        # self.events_url = events_url
        # self.hooks_url = hooks_url
        # self.issues_url = issues_url
        # self.members_url = members_url
        # self.public_members_url = public_members_url
        # self.avatar_url = avatar_url
        # self.description = description
        # self.name = name
        # self.company = company
        # self.blog = blog
        # self.location = location
        # self.email = email
        # self.twitter_username = twitter_username
        # self.is_verified = is_verified
        # self.has_organization_projects = has_organization_projects
        # self.has_repository_projects = has_repository_projects
        # self.public_repos = public_repos
        # self.public_gists = public_gists
        # self.followers = followers
        # self.following = following
        # self.html_url = html_url
        # self.created_at = created_at
        # self.updated_at = updated_at
        # self.type = type

    async def get_organization_by_name(self, orgName: str) -> Organization:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url=f"https://api.github.com/orgs/{orgName}") as r:
                r: dict = await r.json()
                return Organization(
                    login=r["login"],
                    id=r["id"],
                    node_id=r["node_id"],
                    url=r["url"],
                    repos_url=r["repos_url"],
                    events_url=r["events_url"],
                    hooks_url=r["hooks_url"],
                    issues_url=r["issues_url"],
                    members_url=r["members_url"],
                    public_members_url=r.get("public_members_url"),
                    avatar_url=r.get("avatar_url"),
                    description=r.get("description"),
                    name = r.get("name", r["login"]),
                    company=r.get("company"),
                    blog=r.get("blog"),
                    location=r.get("location"),
                    email=r.get("email"),
                    twitter_username=r.get("twitter_username"),
                    is_verified=r.get("is_verified"),
                    has_organization_projects=r["has_organization_projects"],
                    has_repository_projects=r["has_repository_projects"],
                    public_repos=r["public_repos"],
                    public_gists=r["public_gists"],
                    followers=r["followers"],
                    following=r["following"],
                    html_url=r["html_url"],
                    created_at=r["created_at"],
                    updated_at=r["updated_at"],
                    type=r["type"]
                )


    async def get_user_by_username(self, name: str) -> User:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url=f"https://api.github.com/users/{name}") as r:
                r = await r.json()
                return User(
                    login=r["login"],
                    id=r["id"],
                    node_id=r["node_id"],
                    avatar_url=r["avatar_url"],
                    url=r["url"],
                    html_url=r["html_url"],
                    followers_url=r["followers_url"],
                    following_url=r["following_url"],
                    gists_url=r["gists_url"],
                    starred_url=["starred_url"],
                    subscriptions_url=r["subscriptions_url"],
                    organizations_url=r["organizations_url"],
                    repos_url=r["events_url"],
                    events_url=r["repos_url"],
                    received_events_url=r["received_events_url"],
                    type=r["type"],
                    site_admin=r["site_admin"],
                    name=r["name"],
                    company=r["company"],
                    blog=r["blog"],
                    location=r["location"],
                    email=r["email"],
                    hireable=r["hireable"],
                    bio=r["bio"],
                    twitter_username=r["twitter_username"],
                    public_repos=r["public_repos"],
                    public_gists=r["public_gists"],
                    followers=r["followers"],
                    following=r["following"],
                    created_at=r["created_at"],
                    updated_at=r["updated_at"],
                    dict=r
                )
        

