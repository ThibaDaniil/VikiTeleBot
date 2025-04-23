# Импортируем необходимые классы.
import logging
import fandom
from random import choice
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import BOT_TOKEN, games

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
fandom.set_lang('ru')

async def start(update, context):
    await update.message.reply_text("Привет, я бот помошник по Viki")


async def random_state(update, context):
    try:
        fandom.set_wiki(context.args[0].lower())

        rand_sate = fandom.random(pages=1)
        page = fandom.page(pageid=rand_sate[1])
        await update.message.reply_text(page.url)
    except Exception:
        await update.message.reply_text(f'Мы не смогли найти сайт по вашему запросу,'
                                        f' проверте правильно ли вы написали название (англискими буквами и через '
                                        f'- если название состоит из нескольких слов)')


async def random_game(update, context):
    await update.message.reply_text(choice(games))


async def short_find(update, context):
    try:
        fandom.set_wiki(context.args[0].lower())
        page = fandom.page(pageid=fandom.search(context.args[0], results=1)[0][1])
        try:
            await update.message.reply_text(page.summary)
        except Exception:
            await update.message.reply_text(f'Мы не смогли вытащить данные с сайта вот ссылка на источник: {page.url}')
    except Exception:
        await update.message.reply_text(f'Мы не смогли найти сайт по вашему запросу,'
                                        f' проверте правильно ли вы написали название (англискими буквами и через '
                                        f'- если название состоит из нескольких слов)')


async def find_info_about(update, context):
    try:
        fandom.set_wiki(context.args[0].lower())
        page = fandom.page(pageid=(fandom.search(context.args[1], results=1)[0][1]))
        try:
            await update.message.reply_text(page.content['content'])
        except Exception:
            await update.message.reply_text(f'Мы не смогли вытащить данные с сайта вот ссылка на источник: {page.url}')
    except Exception:
        await update.message.reply_text(f'Мы не смогли найти сайт по вашему запросу,'
                                        f' проверте правильно ли вы написали название (англискими буквами и через '
                                        f'- если название состоит из нескольких слов)')


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("random_state", random_state))
    application.add_handler(CommandHandler("random_game", random_game))
    application.add_handler(CommandHandler("short_find", short_find))
    application.add_handler(CommandHandler("find_info_about", find_info_about))

    application.run_polling()


if __name__ == '__main__':
    main()
