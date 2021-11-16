import asyncio
from pytenor import Tenor

api = Tenor(key="api key here")


async def main():
    # Search for gifs. This returns a GIF object.
    gifs = await api.search("l00WNIBW6N35C")

    print("Here are the gifs I found")
    for gif in gifs:
        print(
            f"URL: {gif.url} | Title: {gif.title} | Available Formats: {gif.available_formats}")


if __name__ == "__main__":
    asyncio.run(main())
