from database import user
import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from database import db

load_dotenv(override=True)

um = user.UserManager()

class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        print(f"databases: {db.tables.items()}")
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f'Loaded {filename[:-3]} cog successfully')
                except Exception as e:
                    print(f'Failed to load {filename[:-3]} cog. Error: {e}')
        
        try:
            synced = await self.tree.sync()
            print(f'Successfully synced commands: {synced}')
        except Exception as e:
            print(f'Failed to sync commands: {e}')

intents = discord.Intents.default()
intents.message_content = True

bot = Bot(command_prefix='!', intents=intents)

async def main() -> None:
    async with db.conn(os.getenv("DB_BOT_TOKEN")):
        try:
            await bot.start(os.getenv("BOT_TOKEN"))
        finally:
            await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
