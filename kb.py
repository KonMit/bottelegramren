from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image")],
    [InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
    InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
    InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]

step1 = [
    [InlineKeyboardButton(text="Да, готов!", callback_data="step_to_2"),
    InlineKeyboardButton(text="Заказать сейчас", callback_data="link_app")],
]
step2 = [
    [InlineKeyboardButton(text="c 8 до 10", callback_data="step_to_3"),
    InlineKeyboardButton(text="c 10 до 13", callback_data="step_to_3")],
    [InlineKeyboardButton(text="c 13 до 16", callback_data="step_to_3"),
    InlineKeyboardButton(text="c 16 до 20", callback_data="step_to_3")],
]
step3 = [
    [InlineKeyboardButton(text="Наличными", callback_data="step_to_4"),
    InlineKeyboardButton(text="Безналичный", callback_data="step_to_4")],
]
step4 = [
    [InlineKeyboardButton(text="Обожаю", callback_data="step_to_finished"),],
]
step_finished = [
    [InlineKeyboardButton(text="Выбрать дату и заказать сейчас", callback_data="step_finished", inline_keyboard_markup=1),],
    [InlineKeyboardButton(text="О нас", callback_data="info_company",),]
]

statistics_menu = [
    [InlineKeyboardButton(text="За день", callback_data="statistics_day", inline_keyboard_markup=1),],
    [InlineKeyboardButton(text="За неделю", callback_data="statistics_week",),],
    [InlineKeyboardButton(text="За месяц", callback_data="statistics_month",),]
]

step1 = InlineKeyboardMarkup(inline_keyboard=step1)
step2 = InlineKeyboardMarkup(inline_keyboard=step2)
step3 = InlineKeyboardMarkup(inline_keyboard=step3)
step4 = InlineKeyboardMarkup(inline_keyboard=step4)
step_finished = InlineKeyboardMarkup(inline_keyboard=step_finished)
statistics_menu = InlineKeyboardMarkup(inline_keyboard=statistics_menu)

# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Начать сначала")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Начать сначала", callback_data="step_to_1")]])
# menu = InlineKeyboardMarkup(inline_keyboard=menu)
# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])