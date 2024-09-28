from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv


load_dotenv()

TOKEN: str | None = os.getenv("BOT_TOKEN")
if TOKEN is None:
	print("Please set BOT_TOKEN env")
	exit(1)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await update.message.reply_text(f'Hello, {update.effective_user.first_name}!')


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", hello))

print("Starting bot...")
app.run_polling()
