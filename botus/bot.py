import logging
import os
from telegram.ext import Updater, CommandHandler
from bot_helpers import (
    get_courses,
    has_course,
    get_query_from_user_input
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def show_courses(bot, update):
    query = get_query_from_user_input(update.message.text)
    if query is None:
        update.message.reply_text('Запрос неверный. Повторите.')
    courses = get_courses(os.environ['OTUS_API_COURSE'])
    has_one_course = False
    for course in courses:
        title = course['title']
        description = course['description']
        if has_course(query, title, description):
            has_one_course = True
            update.message.reply_text(
                f"""Найден курс "{title}" стоимостью {course['price']} руб.\n""" \
                f"""Подробная информация по ссылке: {course['link']}"""
            )
    if not has_one_course:
        update.message.reply_text(f'По запросу {query} курсов не найдено.')

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    updater = Updater(os.environ['TELEGRAM_TOKEN'])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("courses", show_courses))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()