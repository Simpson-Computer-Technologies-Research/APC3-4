from discord_components import DiscordComponents
from discord.ext import commands
import discord

# ////////////////////////////////////////////////////////////////////
# //                                                                //
# //        Add the below to every discord bot you create.          //
# //                                                                //
# ////////////////////////////////////////////////////////////////////
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(
    # // You can set your own prefix to whatever you want.
    # // The prefix is how the user activates your bot's commands
    # //
    # // Example: User sends: !ping
    # // The 'ping' command is activated.
    command_prefix = '!',
    
    # // Bot Intents
    intents = discord.Intents(
        messages=True, 
        guilds=True, 
        reactions=True, 
        members=True
    )
)

# // The on_ready() event is called when you launch the bot.
@client.event
async def on_ready():
    # // Discord Components. These are used in Lesson #6
    # // If you're not using components (aka: buttons, dropdowns, etc.)
    # // You can remove this
    DiscordComponents(client)
    
    # // Notify that the bot has been launched
    print(f"Successfully Launched {client.user.name}")


# // Launch the discord bot
if __name__ == "__main__":
    client.run("YOUR DISCORD BOT TOKEN")
    