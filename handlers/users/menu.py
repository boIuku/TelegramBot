from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.types import ReplyKeyboardRemove

from emails.emails import sendemail
from keyboards.default.menu import *
from loader import dp

media = types.MediaGroup()

@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Wybierz pozycje z listy", reply_markup=menu)


@dp.message_handler(Text(equals=["Capricosa", "Margherita", "Peperorni"]))
async def get_pizza(message: types.Message):
    await message.answer(f"Wybrano: {message.text}", reply_markup=ReplyKeyboardRemove())
    if message.text == "Margherita":
        await message.answer("Czy potwierdzasz wybór?", reply_markup=taknie)


@dp.message_handler(Text(equals=["Tak"]))
async def send():
    await sendemail()


