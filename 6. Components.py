
# //////////////////
# //  Components  //
# //////////////////
from discord_components import Button, ButtonStyle, Interaction
from discord.ext import commands


# // Components are a bit more complicated
# // But i'm sure they'll make sense once I've explained
# // them a bit better

# // First, Create a new command. In this case we'll name
# // our command '!send_button'
# //
# // Components are sent when you call 'await.ctx.send'
@commands.command()
async def send_button(ctx: commands.Context):
    
    # // Send a message back to the user
    return await ctx.send("A Message With A Button!",
                          
        # // Identify that you are using components
        components=[[
            
            # // A Button component
            Button(
                # // The button color
                style = ButtonStyle.blue, 
                
                # // The button title
                label='PRESS ME!', 
                
                # // A unique id which is used for determining 
                # // how to react once the button was pressed
                custom_id='press_me_button_id'
            )
        ]]
    )
    

# // Listen to the button clicks
@commands.Cog.listener()
async def on_button_click(res: Interaction):
    if not res.author.bot:

        # // The button with the id "press_me_button_id" has been pressed
        if res.component.id == "press_me_button_id":
            
            # // Send a response back to the author
            await res.channel.send("Button Pressed!")
