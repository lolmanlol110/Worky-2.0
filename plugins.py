import os
import sys
import discord

# Экземпляры загруженных плагинов
Plugins = {}
PNames = []
# Базовый класс плагина
class Plugin(object):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    Name = "NONE"
    Discription = "NONE"
    # При подключении
    async def OnLoad(self) -> None:
        pass
    # При сообщении
    async def onMessage(self, message: discord.message) -> None:
        pass
    # при отключении
    async def onDisable(self) -> None:
        pass


async def LoadPlugins(bot: discord.Bot):
    FileNames = os.listdir('BotPlugins')  # Получаем список плагинов в /plugins
    sys.path.insert(0, 'BotPlugins')  # Добавляем папку плагинов в $PATH, чтобы __import__ мог их загрузить
    for FileName in FileNames:
        if FileName == '__pycache__' or FileName.split(".")[-1].lower() != "py":
            continue
        if os.path.splitext(FileName)[0] in sys.modules:
            print("Плагин", os.path.splitext(FileName)[0], "уже присутствует. Пропуск")
            continue

        print ('Найден ноавй плагин: ', FileName)
        # Импорт пакета и занесение его названия в массив
        __import__(os.path.splitext(FileName)[0], None, None, [''])  # Импортируем исходник плагина
        # Создание экземпляра класса, занесение в ключный массив и вызов его метода загрузки
        # print(Plugin.__subclasses__()[-1](bot))
        plugin = Plugin.__subclasses__()[-1](bot)

        Plugins[os.path.splitext(FileName)[0]] = plugin
        await plugin.OnLoad()

    return
async def PlaginRemove(Name):
    if Name not in sys.modules:
        print(f"Плагин {Name} не найден!")
        # if Name in PNames:
        #     PNames.remove(Name)
        #     print(f"Название {Name} без плагина было Удалено!")
        return

    for plugin in list(Plugins.values()):
        if Name not in plugin.__module__:
            continue
        await plugin.onDisable()
        del Plugins[Name]
        del sys.modules[Name]
        print("Плагин успешно отключён!")


