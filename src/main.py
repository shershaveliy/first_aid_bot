import os
from dotenv import load_dotenv
from bot import MyBot
import config

if __name__ == '__main__':
    load_dotenv()

    TOKEN: str | None = os.getenv("BOT_TOKEN")
    if TOKEN is None:
        print("Please set BOT_TOKEN env")
        exit(1)
    
    config.configure_locale()
    
    bot = MyBot(TOKEN)
    bot.run()
