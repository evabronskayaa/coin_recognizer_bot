
from utils.db_functions.requset_functions import change_request
from utils.functions.authentication import authentication


async def get_image(call, bot, context):
    t_id = call.from_user.id
    chat_id = call.message.chat.id
    user = authentication(context, t_id, chat_id)
    file_info = await bot.get_file(call.message.photo[-1].file_id)
    path = "assets/images/" + file_info.file_path.split('photos/')[1]
    await call.message.photo[-1].download(path)
    file = open(path, 'rb')
    image = file.read()
    file.close()
    return image, user


async def change_value(call, value, text, bot, context):
    image, user = await get_image(call, bot, context)
    if change_request(image, user, value):
        await call.message.answer(text)
