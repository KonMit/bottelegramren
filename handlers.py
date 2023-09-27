# Основной файл с кодом 

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import flags
from aiogram.fsm.context import FSMContext
from states import Gen

import kb
import text
import utils


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.step1)
# @router.message(F.data == "step_to_2")
# async def step_to_2(msg: Message):
#     await msg.answer(text.step_text1, reply_markup=kb.step2)
# @router.message(F.data == "link_to_app")
# @router.message(F.data == "step_to_3")
# async def step_to_3(msg: Message):
#     await msg.answer(text.step_text2, reply_markup=kb.step3)
# @router.message(F.data == "step_to_4")
# async def step_to_4(msg: Message):
#     await msg.answer(text.step_text3, reply_markup=kb.step4)
# @router.message(F.data == "step_to_finished")
# async def step_to_finished(msg: Message):
#     await msg.answer(text.step_text4, reply_markup=kb.step_finished)
# @router.message(F.data == "step_finished")
# async def step_finished(msg: Message):
#     await msg.answer(text.menu)
# @router.message(F.data == "info_company")
# async def info_company(msg: Message):
#     await msg.answer(text.menu)

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
async def link_app(clbck: router.callback_query, state: FSMContext):
    await clbck.message.answer(text.link_app_text, reply_markup=kb.iexit_kb)

@router.callback_query(F.data == "step_to_finished")
async def step_to_finished(clbck: router.callback_query, state: FSMContext):
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