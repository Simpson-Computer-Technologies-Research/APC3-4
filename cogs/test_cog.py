from datetime import datetime as datetime
from discord.ext import commands
import discord

# // Do not change this
class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    # ////////////////////////////////////////////////
    # // Anything below this point you can change.. //
    # ////////////////////////////////////////////////
    
    @commands.command()
    async def test(self, ctx: commands.Context, user: discord.Member):
        await ctx.send(f"{user.mention} called the Test Cog!")
        


# // DO NOT CHANGE THIS!
def setup(client):
    client.add_cog(Test(client))