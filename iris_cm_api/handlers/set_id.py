from vkbottle import BotBlueprint
from vkbottle.bot import Message
from iris_cm_api import utils

bot = BotBlueprint()
bot.labeler.vbml_ignore_case = True


@bot.on.chat_message(text=["установить ид <chat_id>", "🗓 Код беседы: <chat_id>"])
@utils.admin_only
async def set_iris_id_wrapper(m: Message, chat_id: str):
    if len(chat_id) > 8:
        return "⚠ Слишком большой ID"
    if len(chat_id) < 8:
        return "⚠ Слишком короткий ID"

    chat = await utils.get_chat(m.peer_id)
    chat.iris_id = chat_id
    await chat.save()
    return "✅ ID чата установлен"
