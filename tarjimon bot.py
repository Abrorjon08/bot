
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile
import asyncio
from googletrans import Translator
from gtts import gTTS


bot = Bot(token="8273257385:AAGB81o6cwURMSScbhQ_qsCt2LvcN-CiccY")
dp = Dispatcher()
translator = Translator()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Assalomu alaykum. Tarjimon botimizga Xush kelibsiz')


@dp.message()
async def translate_word(message: types.Message):
    word = message.text
    result = await translator.translate(word, src='uz', dest='en')
    eng_word = result.text
    ovoz = gTTS(eng_word, lang='en')
    nom = 'ovoz.mp3'
    ovoz.save(nom)
    await message.answer(f'{word} - {eng_word}')
    await message.answer_audio(FSInputFile(nom))


async def start_bot():
    print('Bot starting...')
    await dp.start_polling(bot)


asyncio.run(start_bot())
