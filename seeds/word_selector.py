import asyncio
from urllib.request import urlopen

SEED_SITE = "https://www.mit.edu/~ecprice/wordlist.10000"


async def fetch_words(site: str):
    with urlopen(site) as response:
        body = response.read().decode()
    body.splitlines()


async def main():
    await fetch_words(SEED_SITE)
    print("Waiting on main")

asyncio.run(main())
