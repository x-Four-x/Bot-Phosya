import validators
from sql_func import *
from aiogram import types
from loader import dp, bot
from data.config import *
from aiogram.dispatcher import FSMContext
from states import mail_list
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery
from keyboards.inline.inline_kb_adm import ikb_adm

markup_conf = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Отменить', callback_data='quit')
                                    ]
                                ])

@dp.callback_query_handler(lambda call: call.data.startswith("Адм") and call.data.endswith("рек"))
async def advertising(call: CallbackQuery):
    await call.message.answer("<b>📝 Пришли название и ссылку для инлайн кнопки</b>\n"
    "В формате: (Текст|Cсылка)",
    reply_markup=markup_conf)
    await mail_list.link.set()
    await bot.answer_callback_query(call.id)

@dp.message_handler(lambda message: validators.url(message.text.partition('|')[2].strip()), state=mail_list.link)
async def link_group(message: types.Message, state: FSMContext):
    await state.update_data(link = message.text.partition('|')[2].strip())
    await state.update_data(text = message.text.partition('|')[0].strip())
    await message.answer("<b>Отправь фото к рекламе</b>", reply_markup=markup_conf)
    await mail_list.next()

@dp.message_handler(state=mail_list.link)
async def link_group(message: types.Message, state: FSMContext):
    await message.answer("Это ссылка имеет не поддерживаемый формат/Или это не ссылка\n"
    "Введите корр-ю ссылку формата - http:// | https://", reply_markup=markup_conf)

@dp.message_handler(state=mail_list.preview, content_types=types.ContentType.PHOTO)
async def preview_ads(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(preview = photo_id)
    await message.answer("<b>Отправь описание рекламы</b>", reply_markup=markup_conf)
    await mail_list.next()

@dp.message_handler(state=mail_list.preview)
async def preview_ads(message: types.Message, state: FSMContext):
    await message.answer("Это не фото | Пришли фото", reply_markup=markup_conf)

@dp.message_handler(state=mail_list.descript)
async def quest_ads(message: types.Message, state: FSMContext):
    await state.update_data(descript = message.text)
    data = await state.get_data()
    description = data.get('descript')
    photo = data.get('preview')
    link = data.get('link')
    text = data.get('text')
    markup_admin = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Да', callback_data='confirm'),
                                        InlineKeyboardButton(text='Отменить', callback_data='quit')
                                    ]
                                ])
    markup_user = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=text, url=link),
                                    ]
                                ])

    await message.answer_photo(photo=photo, caption=description, reply_markup=markup_user)
    await message.answer("Начинать рассылку?", reply_markup=markup_admin)
    await mail_list.next()

@dp.callback_query_handler(text="confirm", state=mail_list.finish_ads)
async def ads_confirm(call: CallbackQuery, state = FSMContext):
    data = await state.get_data()
    description = data.get('descript')
    photo = data.get('preview')
    link = data.get('link')
    text = data.get('text')
    markup_user = InlineKeyboardMarkup(row_width=2,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(text=text, url=link),
                                ]
                            ])
    sent = 0
    successful = 0
    not_successful = 0
    for user in check_all_users():
        sent += 1
        try:
            await dp.bot.send_photo(chat_id=user, photo=photo, caption=description, reply_markup=markup_user)
            successful += 1
        except:
            not_successful +=1
    await call.message.answer("Рассылка завершена!\n"
    f"Всего отправленно: {sent}\n"
    f"Успешных отправок: {successful}\n"
    f"Не успешных: {not_successful}")
    await state.finish()
    await bot.answer_callback_query(call.id)

@dp.callback_query_handler(text='quit', state=[mail_list.link, mail_list.descript, mail_list.preview])
async def ads_confirm(call: CallbackQuery, state = FSMContext):
    await call.message.delete()
    await call.message.answer("Рассылка отменена!", reply_markup=ikb_adm)
    await state.finish()
    await bot.answer_callback_query(call.id)