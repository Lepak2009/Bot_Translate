from aiogram import types, Rovter
rovter = Rovter()

@rovter.message(lambda message: message.text == "Test")

async def test_handler(message: types.Message):
          print("dfsdfsdfsddfs")
          await message.answer("""It's test message!""")


