from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard()->ReplyKeyboardMarkup:
          Keyboard = ReplyKeyboardMarkup(
                    Keyboard=[
                          [KeyboardButton(text="Test")]
                           
                  
                    
                         ],
                    resize_keyboard=True
                     
                  
          )
          return Keyboard