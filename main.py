# Импортируем необходимые классы.
import logging
from random import choice
from config import BOT_TOKEN, games
from telegram.ext import Application, MessageHandler, filters, CommandHandler, CallbackQueryHandler, \
    ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_TOKEN
import fandom

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
fandom.set_lang('ru')

ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN = range(10)
START_ROTES, END_ROUTES = range(2)


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


def find_func(game_name):
    try:
        fandom.set_wiki(game_name.lower())
        page = fandom.page(pageid=fandom.search(game_name, results=1)[0][1])
        try:
            return page.content['content']
        except Exception:
            return f'Мы не смогли вытащить данные с сайта вот ссылка на источник: {page.url}'
    except Exception:
        return f'Мы не смогли найти сайт по вашему запросу, проверте правильно ли вы написали название (англискими ' \
               f'буквами и через - если название состоит из нескольких слов) или наша поисковая система' \
               f' не смогла найти ее'


async def find(update, context):
    await update.message.reply_text(find_func(context.args[0]))


async def top10(update, context):
    keyboard = [
        [InlineKeyboardButton("Elden Ring", callback_data=str(ONE))],
        [InlineKeyboardButton("The Witcher 3: Wild Hunt", callback_data=str(TWO))],
        [InlineKeyboardButton("Red Dead Redemption 2", callback_data=str(THREE))],
        [InlineKeyboardButton("Baldur's Gate 3", callback_data=str(FOUR))],
        [InlineKeyboardButton("Mass Effect 2", callback_data=str(FIVE))],
        [InlineKeyboardButton("Portal 2", callback_data=str(SIX))],
        [InlineKeyboardButton("Resident Evil 4", callback_data=str(SEVEN))],
        [InlineKeyboardButton("The Elder Scrolls 5: Skyrim", callback_data=str(EIGHT))],
        [InlineKeyboardButton("God of War (2018)", callback_data=str(NINE))],
        [InlineKeyboardButton("Minecraft", callback_data=str(TEN))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Топ 10 игр по нашему мнению", reply_markup=reply_markup)
    return START_ROTES


async def TW3(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton('☚ Вернутся', callback_data=str(ONE)),
         InlineKeyboardButton('Закончить', callback_data=str(TWO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = 'https://vedmak.fandom.com/wiki/%D0%92%D0%B5%D0%B4%D1%8C%D0%BC%D0%B0%D0%BA_3:' \
           '_%D0%94%D0%B8%D0%BA%D0%B0%D1%8F_%D0%9E%D1%85%D0%BE%D1%82%D0%B0'
    await query.edit_message_text(text=f"{text}", reply_markup=reply_markup)
    return END_ROUTES


async def Portl2(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton('☚ Вернутся', callback_data=str(ONE)),
         InlineKeyboardButton('Закончить', callback_data=str(TWO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = 'https://portal.fandom.com/ru/wiki/Portal_2'
    await query.edit_message_text(text=f"{text}", reply_markup=reply_markup)
    return END_ROUTES


async def RDR2(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton('☚ Вернутся', callback_data=str(ONE)),
         InlineKeyboardButton('Закончить', callback_data=str(TWO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = 'https://reddead.fandom.com/ru/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F' \
           '_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    await query.edit_message_text(text=f"{text}", reply_markup=reply_markup)
    return END_ROUTES


async def BaldGate3(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton('☚ Вернутся', callback_data=str(ONE)),
         InlineKeyboardButton('Закончить', callback_data=str(TWO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "https://baldursgate.fandom.com/ru/wiki/Baldur%27s_Gate_III"
    await query.edit_message_text(text=f"{text}", reply_markup=reply_markup)
    return END_ROUTES


async def MassEffec2(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton('☚ Вернутся', callback_data=str(ONE)),
         InlineKeyboardButton('Закончить', callback_data=str(TWO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = 'https://masseffect.fandom.com/ru/wiki/Mass_Effect_2'
    await query.edit_message_text(text=f"{text}", reply_markup=reply_markup)
    return END_ROUTES


async def EldenRing(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton('☚ Вернутся', callback_data=str(ONE)),
         InlineKeyboardButton('Закончить', callback_data=str(TWO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = 'https://eldenring.fandom.com/ru/wiki/Elden_Ring_%D0%92%D0%B8%D0%BA%D0%B8'
    await query.edit_message_text(text=f"{text}", reply_markup=reply_markup)
    return END_ROUTES


async def ResEv4(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton('☚ Вернутся', callback_data=str(ONE)),
         InlineKeyboardButton('Закончить', callback_data=str(TWO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = 'https://residentevil.fandom.com/ru/wiki/Resident_Evil_4'
    await query.edit_message_text(text=f"{text}", reply_markup=reply_markup)
    return END_ROUTES


async def Skirim(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton('☚ Вернутся', callback_data=str(ONE)),
         InlineKeyboardButton('Закончить', callback_data=str(TWO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = 'https://elderscrolls.fandom.com/ru/wiki/The_Elder_Scrolls_V:_Skyrim'
    await query.edit_message_text(text=f"{text}", reply_markup=reply_markup)
    return END_ROUTES


async def GodOfWar(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton('☚ Вернутся', callback_data=str(ONE)),
         InlineKeyboardButton('Закончить', callback_data=str(TWO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = 'https://godofwar.fandom.com/ru/wiki/God_of_War_(2018)'
    await query.edit_message_text(text=f"{text}", reply_markup=reply_markup)
    return END_ROUTES


async def Minecraft(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton('☚ Вернутся', callback_data=str(ONE)),
         InlineKeyboardButton('Закончить', callback_data=str(TWO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = 'https://minecraft.fandom.com/ru/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F' \
           '_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    await query.edit_message_text(text=f"{text}", reply_markup=reply_markup)
    return END_ROUTES


async def back(update, context):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Elden Ring", callback_data=str(ONE))],
        [InlineKeyboardButton("The Witcher 3: Wild Hunt", callback_data=str(TWO))],
        [InlineKeyboardButton("Red Dead Redemption 2", callback_data=str(THREE))],
        [InlineKeyboardButton("Baldur's Gate 3", callback_data=str(FOUR))],
        [InlineKeyboardButton("Mass Effect 2", callback_data=str(FIVE))],
        [InlineKeyboardButton("Portal 2", callback_data=str(SIX))],
        [InlineKeyboardButton("Resident Evil 4", callback_data=str(SEVEN))],
        [InlineKeyboardButton("The Elder Scrolls 5: Skyrim", callback_data=str(EIGHT))],
        [InlineKeyboardButton("God of War (2018)", callback_data=str(NINE))],
        [InlineKeyboardButton("Minecraft", callback_data=str(TEN))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Топ 10 игр по нашему мнению", reply_markup=reply_markup)
    return START_ROTES


async def endTop10(update, context):
    pass


async def end(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="GG")
    return ConversationHandler.END


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("top10", top10)],
        states={
            START_ROTES: [
                CallbackQueryHandler(EldenRing, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(TW3, pattern="^" + str(TWO) + "$"),
                CallbackQueryHandler(RDR2, pattern="^" + str(THREE) + "$"),
                CallbackQueryHandler(BaldGate3, pattern="^" + str(FOUR) + "$"),
                CallbackQueryHandler(MassEffec2, pattern="^" + str(FIVE) + "$"),
                CallbackQueryHandler(Portl2, pattern="^" + str(SIX) + "$"),
                CallbackQueryHandler(ResEv4, pattern="^" + str(SEVEN) + "$"),
                CallbackQueryHandler(Skirim, pattern="^" + str(EIGHT) + "$"),
                CallbackQueryHandler(GodOfWar, pattern="^" + str(NINE) + "$"),
                CallbackQueryHandler(Minecraft, pattern="^" + str(TEN) + "$")
            ],
            END_ROUTES: [
                CallbackQueryHandler(back, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(end, pattern="^" + str(TWO) + "$")
            ],
        },
        fallbacks=[CommandHandler("closeTop10", endTop10)],
    )
    application.add_handler(conv_handler)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("random_state", random_state))
    application.add_handler(CommandHandler("random_game", random_game))
    application.add_handler(CommandHandler("short_find", short_find))
    application.add_handler(CommandHandler("find_info_about", find_info_about))
    application.add_handler(CommandHandler("find", find))

    application.run_polling()


if __name__ == '__main__':
    main()
