from os import getenv

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery

from bot.dispatcher import dp

PAYMENT_CLICK_TOKEN = "398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065"
@dp.message(Command('invoice'))
async def invoice(message: Message):
    products = [
        {
            "id" : 1,
            "name" : "Iphone 15 pro",
            "price" : 2000,
        },
        {
            "id": 2,
            "name": "Iphone 14 pro",
            "price": 1000,
        },
        {
            "id": 3,
            "name": "Iphone 13 pro",
            "price": 500,
        }
        ]
    prices = []
    for product in products:
        prices.append(LabeledPrice(label=product.get('name'), amount=product.get('price')))
    await message.answer_invoice('Products', "Jami 3 product order qilindi", '1',"UZS",prices, PAYMENT_CLICK_TOKEN)

@dp.pre_checkout_query()
async def success_handler(pre_checkout_query: PreCheckoutQuery) -> None:
    await pre_checkout_query.answer(True)

@dp.message(lambda message: bool(message.successful_payment))
async def confirm_handler(message: Message, state: FSMContext):
    if message.successful_payment:
        total_amount = message.successful_payment.total_amount//100
        order_id = int(message.successful_payment.invoice_payload)
        # await Order.update(id_=order_id, status=Order.OrderStatusEnum.APPROVED , total_amount = total_amount)
        await message.answer(text=f"To'lo'vingiz uchun raxmat 😊 \n{total_amount}\n{order_id}")
