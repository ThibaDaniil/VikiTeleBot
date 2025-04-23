# Импортируем необходимые классы.
import logging
import fandom
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import BOT_TOKEN

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


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


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("random_state", random_state))

    application.run_polling()


if __name__ == '__main__':
    main()
