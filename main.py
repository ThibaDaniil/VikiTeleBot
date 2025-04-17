# Импортируем необходимые классы.
import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import BOT_TOKEN
import fandom

# Запускаем логгирование
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
# )

logger = logging.getLogger(__name__)


async def start(update, context):
    await update.message.reply_text("Привет, я бот помошник по Viki")


async def find(update, context):
    try:
        fandom.set_wiki(context.args[0].lower())
        page = fandom.page(pageid=fandom.search(context.args[0], results=1)[0][1])
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
    application.add_handler(CommandHandler("find", find))

    application.run_polling()


if __name__ == '__main__':
    fandom.set_lang("ru")
    main()
