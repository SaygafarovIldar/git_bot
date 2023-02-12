from telebot.types import Message

from data.loader import bot


@bot.message_handler(commands=["start"])
def handle_command_start(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    bot.send_message(chat_id, f"Hello, {first_name}")
