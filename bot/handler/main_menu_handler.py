from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup
from aiogram import html, F
from aiogram.utils.i18n import gettext as _, lazy_gettext as __
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.buttons.reply import build_reply_button
from bot.dispatcher import dp
from bot.states import SectorState



@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    ikb = InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
        InlineKeyboardButton(text="🇩🇪 Deutsch", callback_data="lang_de"),
        InlineKeyboardButton(text="🇺🇿 O'zbek" , callback_data="lang_uz")
    )
    ikb.adjust(2,2)
    await state.set_state(SectorState.language)
    await message.answer(text=f"Choose the language.", reply_markup=ikb.as_markup())

@dp.callback_query(F.data.startswith("lang"))
async def lang_selected_handler(callback: CallbackQuery, state: FSMContext, i18n):
    map_lang = {
        "lang_en" : 'en',
        "lang_ru" : 'ru',
        "lang_de" : 'de',
        "lang_uz" : 'uz'
    }
    code = map_lang.get(callback.data)
    await state.update_data({"locale" : code})
    i18n.current_locale = code
    ikb = InlineKeyboardBuilder()
    ikb.add(InlineKeyboardButton(text=_("🏠 Main menu"), callback_data='main'))
    ikb.adjust(1)
    await callback.message.edit_text(text=f"{_('Welcome')}, {html.bold(callback.from_user.full_name)}!\n\n{_("I will help you to find the movies")}!", reply_markup=ikb.as_markup())


@dp.callback_query(SectorState.contact, F.data == "back")
@dp.message(SectorState.movies_section, F.text == __("⬅️ Back"))
@dp.callback_query(F.data == "main")
async def main_menu_handler(event: Message | CallbackQuery, state: FSMContext):
    lang = await state.get_value('locale')
    await state.clear()
    await state.update_data({"locale" : lang})
    texts = [_("🎥 Movies section"), _("📞 Contact us")]
    markup = build_reply_button(texts, (2,))
    await state.set_state(SectorState.main_menu)

    if isinstance(event, CallbackQuery):
        await event.message.delete()
        await event.message.answer(_("🏠 Main menu"), reply_markup=markup)

    else:
        await event.delete()
        await event.answer(_("🏠 Main menu"), reply_markup=markup)


@dp.message(SectorState.action_section, F.text == __("⬅️ Back"))
@dp.message(SectorState.dramas_section, F.text == __("⬅️ Back"))
@dp.message(SectorState.comedy_section, F.text == __("⬅️ Back"))
@dp.message(SectorState.main_menu , F.text == __("🎥 Movies section"))
async def movies_section_handler(message: Message, state: FSMContext):
    texts = [_("🎭 Drama"), _("😂 Comedy"), _("🎬 Action"), _("☠️ Horror"), _("⬅️ Back")]
    markup = build_reply_button(texts, (2,2,1))
    await state.set_state(SectorState.movies_section)
    await message.answer(_("🎥 Movies section"), reply_markup=markup)


@dp.message(SectorState.main_menu , F.text == __("📞 Contact us"))
async def movies_section_handler(message: Message, state: FSMContext):
    phone_number = "998887718871"
    call_link = f"https://api.whatsapp.com/send?phone={phone_number}"
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=_("📞 Call"), url=call_link)],
            [InlineKeyboardButton(text=_("⬅️ Back"), callback_data='back')]
        ]
    )
    await state.set_state(SectorState.contact)
    await message.answer(_("To contact with us: +998887718871 or click the button below 👇🏿"), reply_markup=ikb)



