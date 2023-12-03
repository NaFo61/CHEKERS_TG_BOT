import os
import dotenv

if not dotenv.find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
