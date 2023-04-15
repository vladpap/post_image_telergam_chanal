import os
import telegram
from dotenv import load_dotenv


load_dotenv()
bot = telegram.Bot(token=os.environ['TOKEN_BOT'])

chat_id='@SpaceX_NASA_photo'
bot.send_message(chat_id=chat_id, text="Hi Vladimir in chanal!!!")
