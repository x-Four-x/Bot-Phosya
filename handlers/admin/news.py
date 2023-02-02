from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery
from states import news_bot
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from sql_func import *
from keyboards.inline.inline_kb_adm import ikb_adm

markup_conf = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Отменить', callback_data='quit')
                                    ]
                                ])

markup_admin = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Да', callback_data='confirm'),
                                        InlineKeyboardButton(text='Отменить', callback_data='quit')
                                    ]
                                ])



@dp.callback_query_handler(text='Адм нов')
async def advertising(call: CallbackQuery):
    await news_bot.text.set()
    await call.message.answer("📢 Пришлите сообщение для рассылки новостей", reply_markup=markup_conf)

@dp.message_handler(state=news_bot.text, content_types=types.ContentType.TEXT)
async def news_public(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("Теперь пришли фото для новости\nИли пришли: - | Если новость без фото")
    await news_bot.next()

@dp.message_handler(state=news_bot.text)
async def no_text(message: types.Message, state: FSMContext):
    await message.answer("Это не текст | Пришли сообщение текстом", reply_markup=markup_conf)

@dp.message_handler(lambda message: message.text=='-', state=news_bot.preview)
async def no_previews(message: types.Message, state: FSMContext):
    await state.update_data(preview=None)
    await message.answer("📢 Сообщение готово запускать рассылку?", reply_markup=markup_admin)

@dp.message_handler(state=news_bot.preview, content_types=types.ContentType.PHOTO)
async def previews(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(preview=photo_id)
    await message.answer("📢 Сообщение готово запускать рассылку?", reply_markup=markup_admin)

@dp.callback_query_handler(text='confirm', state=news_bot.preview)
async def news_confirm(call: CallbackQuery, state = FSMContext):
    sent = 0
    successful = 0
    not_successful = 0
    data = await state.get_data()
    text = data.get('text')
    preview = data.get('preview')
    if preview == None:
        for user in check_all_users():
            sent += 1
            try:
                await dp.bot.send_message(chat_id=user, text=f"<b>[📢 Администрация]</b>{text}")
                successful += 1
            except Exception as err:
                not_successful +=1
        await call.message.edit_text("📢 Рассылка завершена!\n"
        f"📢 Всего отправленно: {sent}\n"
        f"✅ Успешных отправок: {successful}\n"
        f"⚠️ Не успешных: {not_successful}")
    else:
        for user in check_all_users():
            sent += 1
            try:
                await dp.bot.send_photo(chat_id=user, caption=text, photo=preview)
                successful += 1
            except Exception as err:
                print(err)
                not_successful +=1
        await call.message.edit_text("📢 Рассылка завершена!\n"
        f"|📢 Всего отправленно: {sent}\n"
        f"|✅ Успешных отправок: {successful}\n"
        f"|⚠️ Не успешных: {not_successful}")
    await state.finish()
    await bot.answer_callback_query(call.id)

@dp.callback_query_handler(text='quit', state=news_bot.preview)
async def news_no_confirm(call: CallbackQuery, state = FSMContext):
    await call.message.delete()
    await call.message.answer("Публикация отменена!", reply_markup=ikb_adm)
    await state.finish()
    await bot.answer_callback_query(call.id)

