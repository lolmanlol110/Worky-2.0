from plugins import Plugin
import discord


class Karabiner(Plugin):  # производим наш плагин от родительского класса
    Name = 'Karabiner v0.1'
    Discription = "Отвечает в чат на текст **я люблю**"

    # При загрузке
    async def OnLoad(self):
        print(f'Плагин {self.Name} Зпущен!')

    # Присообщении
    async def onMessage(self, message: discord.message):
        if "я люблю" in message.content.lower():
            await message.channel.send("КАПИБАР!")

    # при выключении
    async def onDisable(self):
        print(f"{self.Name} - Отключён!")
