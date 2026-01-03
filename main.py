import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from datetime import datetime

TOKEN = TOKEN = "YOUR_BOT_TOKEN" 

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Данные бота
subjects = [
    "Программирование",
    "Информатика",
    "Экономика"
]

notes = {}


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет!\n"
        "Я — Student Helper Bot 📚\n\n"
        "Команды:\n"
        "/subjects — предметы\n"
        "/exam — подготовка к сессии\n"
        "/notes — заметки\n"
        "/time — текущее время\n"
        "/about — о боте"
    )


@dp.message(Command("subjects"))
async def show_subjects(message: types.Message):
    text = "📘 Предметы:\n"
    for s in subjects:
        text += f"- {s}\n"
    await message.answer(text)


@dp.message(Command("exam"))
async def exam_help(message: types.Message):
    await message.answer(
        "🧠 Подготовка к сессии:\n"
        "• Повторяй теорию\n"
        "• Практикуй Python\n"
        "• Разбирай билеты\n"
        "• Делай перерывы"
    )


@dp.message(Command("notes"))
async def user_notes(message: types.Message):
    user_id = message.from_user.id
    if user_id in notes:
        await message.answer(f"📝 Твоя заметка:\n{notes[user_id]}")
    else:
        await message.answer(
            "У тебя нет заметок.\n"
            "Напиши: /note текст"
        )


@dp.message(Command("note"))
async def add_note(message: types.Message):
    user_id = message.from_user.id
    text = message.text.replace("/note", "").strip()

    if not text:
        await message.answer("❌ Напиши текст заметки")
        return

    notes[user_id] = text
    await message.answer("✅ Заметка сохранена")


@dp.message(Command("time"))
async def time_now(message: types.Message):
    now = datetime.now().strftime("%H:%M:%S")
    await message.answer(f"⏰ Текущее время: {now}")


@dp.message(Command("about"))
async def about_bot(message: types.Message):
    await message.answer(
        "🤖 Student Helper Bot\n"
        "Помогает студенту в учёбе\n"
        "Проект для защиты\n"
        "Язык: Python + aiogram"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
