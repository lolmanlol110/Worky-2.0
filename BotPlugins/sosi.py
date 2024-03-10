from plugins import Plugin
import discord


class Sosi(Plugin):  # производим наш плагин от родительского класса
    Name = 'sosi v0.0.0.1'
    Discription = "Отвечает в чат на текст **соси**"
    # При загрузке
    async def OnLoad(self):
        print('Плагин **sosi v0.0.0.1** Зпущен!')
    # Присообщении
    async def onMessage(self, message: discord.message):
        if "соси" in message.content.lower():
            await message.channel.send("ХУЙ!")
    # при выключении
    async def onDisable(self):
        print("Я ЕЩЁ ВЕРНУСЬ!!!")
