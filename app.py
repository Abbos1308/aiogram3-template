from aiogram import Bot,Dispatcher , types
from asyncio import run
from handlers import  start_handler
dp = Dispatcher()

async def start():
    bot = Bot("yfyufutff46385363865")
    dp.message.register(start_handler)
    dp.start_polling(bots=bot,polling_timeout=1)

run(start())
