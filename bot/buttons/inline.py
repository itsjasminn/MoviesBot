# from aiogram import F
# from aiogram.types import InlineKeyboardButton, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, \
#     CallbackQuery
# from aiogram.utils.keyboard import InlineKeyboardBuilder
#
# from bot.dispatcher import dp
#
# books = [
#     {
#         "id" : 1,
#         "image" : "https://hilolnashr.uz/image/cache/catalog/bolalar/yulduzli_tunlar-500x750.jpg",
#         "price" : 20000,
#         "title" : "Oq kema",
#
#         "description" : "Yaxshi kitob"
#     },
# {
#     "id": 2,
#     "image" : "https://hilolnashr.uz/image/cache/catalog/bolalar/yulduzli_tunlar-500x750.jpg",
#         "price" : 30000,
#         "title" : "Shumbola",
#         "description" : "Yaxshi kitob"
#     },
# {
#     "id": 3,
#
#     "image" : "https://hilolnashr.uz/image/cache/catalog/bolalar/yulduzli_tunlar-500x750.jpg",
#         "price" : 100000,
#         "title" : "Yulduzli tunlar",
#         "description" : "Yaxshi kitob"
#     },
# ]
#
# @dp.callback_query(F.data == "search")
# async def search_handler(callback: CallbackQuery):
#     ikb = InlineKeyboardBuilder()
#     ikb.add(InlineKeyboardButton(text="Search", callback_data="search"))
#     ikb = ikb.as_markup()
#     await callback.message.edit_reply_markup( reply_markup=ikb)
#
#
#
# @dp.inline_query()
# async def inline_query(inline: InlineQuery):
#     query = inline.query
#     result = []
#     for book in books:
#         if query in book.get("title") or query in book.get("description"):
#             i = InlineQueryResultArticle(
#                 id=str(book.get("id")),
#                 title=book.get("title"),
#                 description=str(f"P27 books\n💴 Narxi: {book.get("price")} so'm"),
#                 thumbnail_url=book.get("image"),
#                 input_message_content=InputTextMessageContent(message_text=str(book.get("id"))),
#             )
#             result.append(i)
#     await inline.answer(result, cache_time=5, is_personal=True)