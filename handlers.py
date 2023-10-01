# Основной файл с кодом 

from aiogram import types, F, Router
from aiogram.types import Message, User
from aiogram.filters import Command
from aiogram import flags
from aiogram.fsm.context import FSMContext
from states import Gen
from datetime import datetime, date, time

import kb
import db
import text
import utils
import admin

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.step1)

@router.message(Command("statistics"))
async def statistics_command(msg: Message, state: FSMContext):
    await msg.answer(text.admin_password_message.format(name=msg.from_user.full_name))
    await state.set_state(Gen.static_pass_promt)
    
    #Добавить проверку пароля, чтобы обычные пользователи не смогли получить доступ при случае если узнают команду
@router.message(Gen.static_pass_promt)
async def statistics_pass(msg: Message, state: FSMContext):
    password = msg.text
    if (password == admin.ADMIN_PASSWORD):
        return await msg.answer(text.statistics_text_question.format(name=msg.from_user.full_name), reply_markup=kb.statistics_menu)
    else: 
        await msg.answer(text.admin_password_error.format(name=msg.from_user.full_name))
    
@router.callback_query(F.data == "statistics_day")
async def print_statistics_day(clbck: router.callback_query):
    await clbck.message.answer(text.statistics_text_answer + "\n" + f"Людей перешедших в приложение без подарка: {db.getting_over_date(1)[0]}" "\n" 
                               + f"Людей дошедших до получения подарка: {db.getting_over_date(1)[1]}")
@router.callback_query(F.data == "statistics_week")
async def print_statistics_week(clbck: router.callback_query):
    await clbck.message.answer(text.statistics_text_answer + "\n" + f"Людей перешедших в приложение без подарка: {db.getting_over_date(7)[0]}" "\n" 
                               + f"Людей дошедших до получения подарка: {db.getting_over_date(7)[1]}")
@router.callback_query(F.data == "statistics_month")
async def print_statistics_month(clbck: router.callback_query):
    await clbck.message.answer(text.statistics_text_answer + "\n" + f"Людей перешедших в приложение без подарка: {db.getting_over_date(30)[0]}" "\n" 
                               + f"Людей дошедших до получения подарка: {db.getting_over_date(30)[1]}")
    

@router.callback_query(F.data == "step_to_2")
async def step_to_2(clbck: router.callback_query, state: FSMContext):
    await clbck.message.answer(text.step_text1, reply_markup=kb.step2)

@router.callback_query(F.data == "step_to_3")
async def step_to_3(clbck: router.callback_query, state: FSMContext):
    await clbck.message.answer(text.step_text2, reply_markup=kb.step3)

@router.callback_query(F.data == "step_to_4")
async def step_to_4(clbck: router.callback_query, state: FSMContext):
    await clbck.message.answer(text.step_text3, reply_markup=kb.step4)

@router.callback_query(F.data == "link_app")
async def link_app(clbck: router.callback_query):
    db.insert_stroke(clbck.message.chat.id, True, False, "app") 
    # Передаем chat id вместо конкрентного user id, т.к. в сообщении нет возможности получить user id, 
    # но т.к. бота расчитан на работу с личными сообщения, то chat id будет совпадать с user id
    await clbck.message.answer(text.link_app_text, reply_markup=kb.iexit_kb)

@router.callback_query(F.data == "step_to_finished")
async def step_to_finished(clbck: router.callback_query, state: FSMContext):
    db.insert_stroke(clbck.message.chat.id, False, True, "gift")
    await clbck.message.answer(text.step_text4, reply_markup=kb.step_finished)

@router.callback_query(F.data == "step_finished")
async def step_finished(clbck: router.callback_query, state: FSMContext):
    await clbck.message.answer(text.link_app_text, reply_markup=kb.step_finished)

@router.callback_query(F.data == "info_company")
async def info_company(clbck: router.callback_query, state: FSMContext):
    await clbck.message.answer(text.info_company_text, reply_markup=kb.step_finished)
    
@router.callback_query(F.data == "step_to_1")
async def step_to_1(clbck: router.callback_query, state: FSMContext):
    await clbck.message.answer(text.greet, reply_markup=kb.step1)