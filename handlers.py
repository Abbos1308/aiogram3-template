from aiogram import types, Bot

async def start_handler(message:types.Message, bot:Bot):
    await message.answer("Assalomu alaykum")