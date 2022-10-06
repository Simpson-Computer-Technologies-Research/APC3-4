from discord.ext import commands
import discord, datetime

# // With every discord command, a ctx (commands.Context) is passed.
# // The command would be called as followed:
# 
# command: !profile @user
# example: !profile @tristan
@commands.command()
async def profile(ctx: commands.Context, user: discord.Member):
    

    # // Create a new embed object
    embed = discord.Embed(
        # // The title of the embed
        title = "Embed Title",
        # // The embed's description
        description = "Embed Description",
        
        # // The color you want the embed to be
        color = 33023, 
        
        # // The current time as a timestamp
        timestamp = datetime.datetime.utcnow()
    )
    
    # // All of the above are optional. This means you can literally create
    # // and embed object as so:
    # // embed = discord.Embed()
    
    
    # // Set the embed author
    embed.set_author(
        # // The authors name
        name = f"Author Tristan", 
        
        # // Set the Avatar image to the users profile picture
        icon_url = user.avatar_url
    )
    
    # // Set the embeds footer to
    embed.set_footer(
        # // The footer text
        text = "The embed footer", 
        
        # // The footer icon image
        icon_url = user.avatar_url
    )
    
    # // Add fields to the embed
    embed.add_field(
        name = "Embed Field 1", 
        value=f"Embed Field 1 Description"
    )
    embed.add_field(
        name = "Embed Field 2", 
        value=f"Embed Field 2 Description"
    )
    
    # // Send the embed to the discord channel
    await ctx.send(embed = embed)
    
    