from telegram.ext import Updater, CommandHandler
import logging
from help_function import read_the_file, record_to_file
from random import choice

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    ,level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    update.message.reply_text('Hi!')
    update.message.reply_text('/help - показывает доступные функции')


def help(bot, update):
    update.message.reply_text('/python_news - Выдает случайную новость из vk.com')

def get_news():
    news_list = read_the_file('News.json')
    if news_list:
        news = choice(news_list)
        news_list.remove(news)
        record_to_file(news_list, 'News.json')
        text = news['text']
        url = '\nvk.com/wall%s_%s' % (news['owner_id'], news['id'])
        news = text + url
    else:
        news = 'Нет актуальных новостй'
    return news
    
def news(bot, update):
    news = get_news()
    update.message.reply_text(news)

def count_of_news(bot, update):
    news_list = read_the_file('News.json')
    text = 'Количество актуальных новостей : %s' % str(len(news_list))
    update.message.reply_text(text)


def main():
    updater = Updater("TOKEN")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("python_news", news))
    dp.add_handler(CommandHandler("python_count", count_of_news))
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
