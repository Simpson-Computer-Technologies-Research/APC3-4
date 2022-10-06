from discord_components import DiscordComponents
from discord.ext import commands
import discord, os

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
    # // Load the cogs. If you are not using a cogs folder, you
    # // can remove this.
    for file_name in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cogs')):
        if file_name.endswith('.py'):
            client.load_extension(f'cogs.{file_name[:-3]}')
            print(f'Loaded: cog.{file_name[:-3]}')
    
    
    # // Run the discord bot
    client.run("YOUR DISCORD BOT TOKEN")
    