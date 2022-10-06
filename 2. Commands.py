from discord.ext import commands
import discord

# // Whenever you want to create a new command, add @commands.command()
# // above the function. The function name is the command name.
# //
# // Example, this command will be used as '!ping' in the discord chat
# // 
# // Since this command has an alias, the user can also
# // send '!pong' into the chat and the same function will be called
@commands.command(aliases=["pong"])
async def ping(ctx: commands.Context):
    
    # // Send a message back to the user
    await ctx.send("pong!")
    
    

# // The below function allows you to ping an user when
# // the command is sent. The command would be run as follows:
# 
# !hello @tristan
#
# // You can add as much users as you want:
# // Example:
# async def hello(ctx: commands.Context, user1: discord.Member, user2: discord.Member):
@commands.command()
async def hello(ctx: commands.Context, user: discord.Member):
    
    # // Send a message back to the user
    await ctx.send(f"hello {user.mention}!")
    