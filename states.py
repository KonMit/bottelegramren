from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    text_prompt = State()
    img_prompt = State()
    step_promt1 = State()
    step_promt2 = State()
    step_promt3 = State()
    step_promt4 = State()
    static_pass_promt = State()