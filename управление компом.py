import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InputFile
import os
import pyautogui
import time
import subprocess
import webbrowser
from pynput.mouse import Controller
mouse = Controller()

logging.basicConfig(level=logging.INFO)
bot = Bot(token="YOUR-BOT-TOKEN")
dp = Dispatcher()

async def send_menu(chat_id):
    builder = InlineKeyboardBuilder()
    button1 = types.InlineKeyboardButton(text = "🌐 telegram", callback_data = "telegram")
    button2 = types.InlineKeyboardButton(text = "🎮 Steam", callback_data = "steam")
    button3 = types.InlineKeyboardButton(text = "🎥 YouTube", callback_data = "youtube")
    button4 = types.InlineKeyboardButton(text = "🔉 Music", callback_data = "music")
    button5 = types.InlineKeyboardButton(text = "📸 Screenshot", callback_data = "screenshot")
    button6 = types.InlineKeyboardButton(text = "🌙Выключение компьютера", callback_data= "pcoff")
    button7 = types.InlineKeyboardButton(text="🔒Блокировка экрана", callback_data="lock")
    button8 = types.InlineKeyboardButton(text="Скачать игру(бета)", callback_data="downoald")
    button9 = types.InlineKeyboardButton(text="❌Ошибки", callback_data="no")
    builder.row(button1, button2)
    builder.row(button3, button4)
    builder.row(button5,button6)
    builder.row(button7,button8)
    builder.row(button9)
    await bot.send_animation(chat_id, animation = "https://i.pinimg.com/originals/08/e4/1c/08e41c2059323fad9b46ea6a18d1b8ef.gif", caption = "Панель управления ПК", reply_markup = builder.as_markup())

async def menu_button(text, chat_id):
    builder = InlineKeyboardBuilder()
    button1 = types.InlineKeyboardButton(text = "Menu", callback_data = "menu")
    builder.row(button1)
    await bot.send_message(chat_id, text, reply_markup = builder.as_markup())



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    chat_id = message.chat.id
    await send_menu(chat_id)

@dp.callback_query(F.data == "telegram")
async def cmd_price(callback: types.CallbackQuery):
    webbrowser.open('https://web.telegram.org/k/')
    chat_id = callback.from_user.id
    text = "telegram запущен ✅"
    await menu_button(text, chat_id)
    await callback.answer()

@dp.callback_query(F.data == "no")
async def cmd_price(callback: types.CallbackQuery):
    chat_id = callback.from_user.id
    builder = InlineKeyboardBuilder()
    button10 = types.InlineKeyboardButton(text="Перезапустить код", callback_data="restart",)
    builder.row(button10)


    await bot.send_message(chat_id, "✔️Обработчик ошибок",reply_markup = builder.as_markup())
    await callback.answer()


@dp.callback_query(F.data == "restart")
async def cmd_price(callback: types.CallbackQuery):

    subprocess.call(['C:\\Program Files (x86)\\Steam\\steam.exe'])
    chat_id = callback.from_user.id



@dp.callback_query(F.data == "downoald")
async def cmd_download(callback: types.CallbackQuery):

    chat_id = callback.from_user.id
    await bot.send_message(chat_id, "Введите название игры, которую хотите скачать:")
    await callback.answer()

@dp.message()
async def process_game_name(message: types.Message):

    game_name = message.text
    chat_id = message.chat.id
    pyautogui.click(x=326, y=51)
    time.sleep(2)
    pyautogui.click(x=135, y=229)
    time.sleep(1)
    pyautogui.write(game_name)
    time.sleep(1)
    pyautogui.click(x=121, y=308)
    time.sleep(1)
    pyautogui.click(x=470, y=531)
    time.sleep(0.5)
    pyautogui.click(x=858, y=735)


@dp.callback_query(F.data == "steam")
async def cmd_price(callback: types.CallbackQuery):
    subprocess.call(['C:\\Program Files (x86)\\Steam\\steam.exe'])
    chat_id = callback.from_user.id
    text = "Steam запущен ✅"
    await menu_button(text, chat_id)
    await callback.answer()

@dp.callback_query(F.data == "youtube")
async def cmd_price(callback: types.CallbackQuery):
    webbrowser.open('https://www.youtube.com')
    chat_id = callback.from_user.id
    text = "YouTube запущен ✅"
    await menu_button(text, chat_id)
    await callback.answer()

@dp.callback_query(F.data == "music")
async def cmd_price(callback: types.CallbackQuery):
    webbrowser.open('https://music.yandex.ru/home')
    time.sleep(7)
    pyautogui.press('space')
    chat_id = callback.from_user.id
    text = "Музыка включена ✅"
    await menu_button(text, chat_id)
    await callback.answer()

@dp.callback_query(F.data == "screenshot")
async def cmd_price(callback: types.CallbackQuery):
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    builder = InlineKeyboardBuilder()
    button1 = types.InlineKeyboardButton(text = "Menu", callback_data = "menu")
    builder.row(button1)
    await bot.send_photo(chat_id = callback.from_user.id, photo=types.FSInputFile("screenshot.png"), caption = "На экране прямо сейчас:", reply_markup = builder.as_markup(), show_caption_above_media = True)
    await callback.answer()

@dp.callback_query(F.data == "pcoff")
async def cmd_price(callback: types.CallbackQuery):
    os.system("shutdown /h")
    chat_id = callback.from_user.id
    text = "Компьютер выключен✅"


@dp.callback_query(F.data == "lock")
async def cmd_lock(callback: types.CallbackQuery):
    os.system("rundll32.exe user32.dll,LockWorkStation")
    await callback.answer("Компьютер заблокирован")

@dp.callback_query(F.data == "menu")
async def cmd_price(callback: types.CallbackQuery):
    chat_id = callback.from_user.id
    await send_menu(chat_id)
    await callback.answer()



async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

while True:
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Критическая ошибка: {e}, перезапуск...")