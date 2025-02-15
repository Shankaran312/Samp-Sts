import discord
import requests
from bs4 import BeautifulSoup
import asyncio
from config import BOT_TOKEN, WEBSITE_URL

# Define intents
intents = discord.Intents.default()
intents.messages = True  # Enable message events

# Initialize the Discord client with intents
client = discord.Client(intents=intents)


async def set_player_count_status():
    await client.wait_until_ready()
    while not client.is_closed():
        player_count = get_player_count()
        if player_count is not None:
            activity = discord.Activity(type=discord.ActivityType.watching,name=f'{player_count} Players')
            await client.change_presence(activity=activity)
        await asyncio.sleep(300)  # Update every 5 minutes


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(set_player_count_status())  # Start status updating task


def get_player_count():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(WEBSITE_URL, headers=headers)
        response.raise_for_status()  # Raise an error for bad response status
        soup = BeautifulSoup(response.content, 'html.parser')
        players_online = soup.find('b', itemprop='playersOnline').text.strip()
        return players_online
    except requests.exceptions.RequestException as e:
        print(f'Error fetching player count: {e}')
        return None
    except (AttributeError, KeyError) as e:
        print(f'Error parsing HTML: {e}')
        return None


client.run(BOT_TOKEN)
