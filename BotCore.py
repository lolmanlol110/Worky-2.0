import asyncio
import discord
import plugins
import config

import Views.PluginsView as plugView

from Utils.Paginator import Paginator
from discord import option

bot = discord.Bot(intents=discord.Intents.all())
asyncio.run(plugins.LoadPlugins(bot))
@bot.event
async def on_message(message):
    for plugin in plugins.Plugins.values():
        await plugin.onMessage(message=message)
@bot.slash_command(name="plugins", description="Вызывает панель управления плагинами")
async def _plugins(ctx):
    arr = [
        ["## Плагины ##", [plugView.UpdatePlugins(plugins, bot)]]
    ]
    for Name, plugin in plugins.Plugins.items():

        arr[0][0] = f"{arr[0][0]}\n1. {plugin.Name}"
        arr.append(
            [f"## {plugin.Name} ##\n{plugin.Discription}",
            [plugView.UpdatePlugins(plugins, bot), plugView.RemovePlugin(plugins, Name, bot)]])

    await Paginator(arr).send(ctx.interaction.response)


bot.run(config.TOKEN)