""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""

import random
import Maps
import Scoreupdate
import FN
import generateorder
import generateteam
import noequalzero
import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks


class ResultView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = 0

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='Team 1', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Team 2', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 2
        self.stop()
    
    @discord.ui.button(label='end scrim', style=discord.ButtonStyle.blurple)
    async def blue(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 3
        self.stop()

class Fun(commands.Cog, name="fun"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="start", description="Play Teamsplitter scrim by stating the 8 players names.",
    )
    @checks.not_blacklisted()
    @app_commands.describe(
        p1="First player on team 1",
        p2="Second player on team 1",
        p3="Third player on team 1",
        p4="Fourth player on team 1",
        p5="First player on team 2",
        p6="Second player on team 2",
        p7="Third player on team 2",
        p8="Fourth player on team 2",
    )

    async def start(self, context: Context, p1: discord.User, p2: discord.User, p3: discord.User, p4: discord.User, p5: discord.User, p6: discord.User, p7: discord.User, p8: discord.User) -> None:
        player1 = context.guild.get_member(p1.id) or await context.guild.fetch_member(p1.id)
        player2 = context.guild.get_member(p2.id) or await context.guild.fetch_member(p2.id)
        player3 = context.guild.get_member(p3.id) or await context.guild.fetch_member(p3.id)
        player4 = context.guild.get_member(p4.id) or await context.guild.fetch_member(p4.id)
        player5 = context.guild.get_member(p5.id) or await context.guild.fetch_member(p5.id)
        player6 = context.guild.get_member(p6.id) or await context.guild.fetch_member(p6.id)
        player7 = context.guild.get_member(p7.id) or await context.guild.fetch_member(p7.id)
        player8 = context.guild.get_member(p8.id) or await context.guild.fetch_member(p8.id)
        players = [player1, player2, player3, player4, player5, player6, player7, player8]
        scores = [0] * 8
        win = [0] * 8
        lose = [0] * 8
        team1 = [0, 1, 2, 3]
        team2 = [4, 5, 6, 7]
        ss = [0, 1, 2, 3, 4, 5, 6, 7]
        bufteams = [0] * 8
        teams = players
        y = 0
        wt = 0
        counter = 1
        while(y == 0):
            map = Maps.Randommap(counter)
            counter += 1
            x = 0
            while(x == 0):
                view = ResultView()
                await context.send(f"{map} \nTeam 1 is **{teams[0]}** **{teams[1]}** **{teams[2]}** **{teams[3]}** \n Team 2 is **{teams[4]}** **{teams[5]}** **{teams[6]}** **{teams[7]}** \nPlease fill in which team won", view=view, delete_after=180.0)
                await view.wait()
                if(view.value == 0):
                    await context.send('Timed out', delete_after=3.0)
                elif(view.value == 1):
                    wt = 1
                    x = 1
                elif(view.value == 2):
                    wt = 2
                    x = 1
                else:
                    y = 1
                    x = 1
            if(y == 1):
                y = 1
            else:
                scores = Scoreupdate.scoreupdt(scores, wt, ss)
                await context.send(f"{players[0]}: {scores[0]} \n{players[1]}: {scores[1]} \n{players[2]}: {scores[2]} \n{players[3]}: {scores[3]} \n{players[4]}: {scores[4]} \n{players[5]}: {scores[5]} \n{players[6]}: {scores[6]} \n{players[7]}: {scores[7]}")
                ah = FN.FNN(scores, players)
                if not ah:
                    re = noequalzero.FN(scores)
                else:
                    lre = len(ah)
                    randomIndex = random.randint(0,lre)
                    re = ah[randomIndex]
                teams = generateteam.gt(scores, players, re)
                ss = generateorder.gso(scores, players, re)

async def setup(bot):
    await bot.add_cog(Fun(bot))
