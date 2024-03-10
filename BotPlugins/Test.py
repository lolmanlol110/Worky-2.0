from plugins import Plugin
import discord
from discord.ext import commands

# import discord.commands

class Test(Plugin):  # производим наш плагин от родительского класса
    Name = 'Test v0.1'
    Discription = "Вызываеь панель с кнопкой\nкоманды: \n1. /kapi"
    # global client
    # client = None

    class Button(discord.ui.View):
        def __init__(self, data):
            super().__init__(timeout=0)

        @discord.ui.button(label="...", style=discord.ButtonStyle.green)
        async def button_callback(self, button, interaction):
            interaction.response.send_message("КАПИБАР!!!")

    class Greetings(commands.Cog):
        @discord.slash_command(name="kapi", description="Вызывает панель управления плагинами")
        async def _hui(self, ctx):
            await ctx.response.send_message("Я люблю...")

    # При загрузке
    async def OnLoad(self):
        # global client

        # await self.bot.register_command(self._hui)
        self.bot.add_cog(self.Greetings(self.bot))
        # print(self.bot)
        print('Плагин Test v0.1 Зпущен!')
    # при выключении
    async def onDisable(self):
        print("'Test v0.1' был отключен!")
