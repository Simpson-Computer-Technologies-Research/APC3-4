from discord.ext import commands

# // Whenever an user types your command, a context object is
# // passed to the function. This context object can be used
# // for finding what server the user is in, what channel the
# // user sent the message in, etc.

# // Getting the guild object
@commands.command()
async def guild_object(ctx: commands.Context):
    server = ctx.author.guild
    
    # // Access the server id
    server_id = server.id
    
    # // Access the server name
    server_name = server.name
    
    # // More can be found on the discord api website
    # https://discord.com/developers/docs/resources/guild
    
    # // Send a message to the current chat
    await ctx.send(f"The Server Name is: {server_name}")
    

# // Getting the author object
@commands.command()
async def user_object(ctx: commands.Context):
    user = ctx.author
    
    # // Access the authors id
    user_id: int = user.id
    
    # // Access the authors name
    user_name: str = user.name
    
    # // More can be found on the discord api website
    # https://discord.com/developers/docs/resources/user
    
    # // Send a message to the current chat
    await ctx.send(f"The Authors Name is: {user_name}")


# // Getting the channel object
@commands.command()
async def channel_object(ctx: commands.Context):
    channel = ctx.channel
    
    # // Access the authors id
    channel_id: int = channel.id
    
    # // Access the authors name
    channel_name: str = channel.name
    
    # // More can be found on the discord api website
    # https://discord.com/developers/docs/resources/channel
    
    # // Send a message to the current chat
    await ctx.send(f"The Channel Name is: {channel_name}")
