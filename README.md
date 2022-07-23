# .gh.py - an Asynchronous GitHub API wrapper made in Python

At the moment I aim to wrap all of things that dont require authentication token.

# Example Usage
```py
import asyncio
from orgs import Organization
from rest import Client
from users import User

async def main():
    client = Client()

    intervinn: User = await client.get_user_by_username("intervinn")
    print(intervinn.login)
    org: Organization = await client.get_organization_by_name("babvin-software")
    print(org.login)
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
```

## API routes that are done:
    * /users/{user}
    * /orgs/{org}
## API routes that I aim to get done:
    * soonTM

# Repository plans
    * switch to aiohttp