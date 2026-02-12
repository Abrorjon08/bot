
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import Command
from aiogram.enums import ChatMemberStatus
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token="8273257385:AAGB81o6cwURMSScbhQ_qsCt2LvcN-CiccY")
dp = Dispatcher()
CHANNEL_ID = -1002319774990


async def check_member(user_id):
    member = await bot.get_chat_member(CHANNEL_ID, user_id)
    return member.status != ChatMemberStatus.LEFT

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='1-kanal', url="https://t.me/Menga_anime")],
        [InlineKeyboardButton(text='✅ Tasdiqlash', callback_data='check')]
    ]
)

@dp.message(Command('start'))
async def start(message: types.Message):
    user_id = message.from_user.id
    if not await check_member(user_id):
        await message.answer(
            'Siz obuna emassiz ❌',
            reply_markup=keyboard
        )
    else:
        await message.answer('Siz obuna bolgansiz ✅')


@dp.callback_query(F.data == 'check')
async def checked_member(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if not await check_member(user_id):
        await callback.answer('Siz hali obuna emassiz ❌', show_alert=True)
    await callback.answer("Siz obuna bo'ldingiz ✅")


async def start_bot():
    print('Bot starting...')
    await dp.start_polling(bot)


asyncio.run(start_bot())
