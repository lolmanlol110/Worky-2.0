import discord
from Utils.Paginator import Paginator


class UpdatePlugins(discord.ui.Button):
    def __init__(self, plugins, bot: discord.Bot) -> None:
        super().__init__(label=f"Обновить плагины", style=discord.ButtonStyle.green, row=2)
        self.plugins = plugins
        self.bot = bot
    async def callback(self, interaction):
        await self.plugins.LoadPlugins(self.bot)
        await interaction.message.delete()
        arr = [
            ["## Плагины ##", [UpdatePlugins(self.plugins, self.bot)]]
        ]
        if len(self.plugins.Plugins.items()) == 0:
            arr[0][0] = f"{arr[0][0]}\nПлагины не найдены"
        else:
            for Name, plugin in self.plugins.Plugins.items():
                arr[0][0] = f"{arr[0][0]}\n1. {plugin.Name}"
                arr.append(
                    [f"## {plugin.Name} ##\n{plugin.Discription}",
                     [UpdatePlugins(self.plugins, self.bot), RemovePlugin(self.plugins, Name, self.bot)]])

        await Paginator(arr).send(interaction.response)

class RemovePlugin(discord.ui.Button):
    def __init__(self, plugins, pluginName, bot: discord.Bot) -> None:
        super().__init__(label=f"Отключть плагин", style=discord.ButtonStyle.red, row=2)
        self.plugins = plugins
        self.pluginName = pluginName
        self.bot = bot
    async def callback(self, interaction):
        await self.plugins.PlaginRemove(self.pluginName)
        await interaction.message.delete()
        arr = [
            ["## Плагины ##", [UpdatePlugins(self.plugins, self.bot)]]
        ]
        if len(self.plugins.Plugins.items()) == 0:
            arr[0][0] = f"{arr[0][0]}\nПлагины не найдены"
        else:
            for Name, plugin in self.plugins.Plugins.items():
                arr[0][0] = f"{arr[0][0]}\n1. {plugin.Name}"
                arr.append(
                    [f"## {plugin.Name} ##\n{plugin.Discription}",
                     [UpdatePlugins(self.plugins, self.bot), RemovePlugin(self.plugins, Name, self.bot)]])

        await Paginator(arr).send(interaction.response)
        # await interaction.response.defer()