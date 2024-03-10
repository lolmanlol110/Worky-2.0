import discord
class Paginator():
    def __init__(self, pages):
        self.startPage = pages[0]

        self.view = self.myView(pages)
    class myView(discord.ui.View):
        def __init__(self, pages) -> None:
            super().__init__(timeout=0)
            self.page = 1
            self.max = len(pages)
            self.pages = pages

            PageIntButton = self.PageIntButton(self)
            leftButton = self.MoveButton(PageIntButton, self, "<", -1)
            rightButton = self.MoveButton(PageIntButton, self, ">", 1)

            discord.ActionRow

            self.add_item(leftButton)
            self.add_item(PageIntButton)
            self.add_item(rightButton)

        def plusPage(self, plusInt: int):
            self.page = self.page + plusInt

        def getPage(self):
            return self.page

        def getPages(self):
            return self.pages

        def getMax(self):
            return self.max

        def setPage(self, int: int):
            page = i

        class PageIntButton(discord.ui.Button):
            def __init__(self, v) -> None:
                super().__init__(label=f"1/{v.getMax()}", style=discord.ButtonStyle.grey)

            async def callback(self, interaction):
                await interaction.response.defer()

        class MoveButton(discord.ui.Button):
            def __init__(self, button: discord.ui.Button, v, text, i: int) -> None:
                super().__init__(label=text, style=discord.ButtonStyle.primary)
                self.button = button
                self.v = v
                self.i = i

            async def callback(self, interaction):
                for component in self.v.getPages()[self.v.getPage()-1][1]:
                    self.view.remove_item(component)
                if self.i < 0:
                    if self.v.getPage() + self.i == 0:
                        self.v.plusPage(self.v.getMax() + self.i)
                    else:
                        self.v.plusPage(self.i)
                else:
                    if self.v.getPage() + self.i > self.v.getMax():
                        self.v.plusPage(self.i - self.v.getMax())
                    else:
                        self.v.plusPage(self.i)

                self.button.label = f"{self.v.getPage()}/{self.v.getMax()}"
                embed = interaction.message.embeds[0]
                embed.description = self.v.getPages()[self.v.getPage() - 1][0]

                print()
                for component in self.v.getPages()[self.v.getPage()-1][1]:
                    self.view.add_item(component)

                await interaction.message.edit(view=self.view, embed=embed)
                await interaction.response.defer()

    async def send(self, iteraction):
        for component in self.startPage[1]:
            self.view.add_item(component)
        await iteraction.send_message(embed=discord.Embed(description=self.startPage[0]), view=self.view)