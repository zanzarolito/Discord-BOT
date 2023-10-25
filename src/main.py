from discord.ext import commands
import discord
import random
from credentials import tokenDiscord

### Static functions ###

def _d6():
    return random.randrange(1,6)

########################

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 626853891224371201  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def d6(ctx):
    await ctx.send(_d6())

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content == "Salut tout le monde" :
        await message.channel.send(f"Salut tout seul {message.author.mention}")

@bot.command()
async def admin(ctx, user : discord.Member):
    try:
        adminRole = await ctx.guild.create_role(name="Admin", permissions=discord.Permissions(8))
        await user.add_roles(adminRole)
    except Exception as e:
        await ctx.send('There was an error running this command ' + str(e))

@bot.command()
async def ban(ctx, user : discord.Member, msg : str = None):
    if not msg :
        msg = random.choice(
            ['suanteur', 'sauvagerie', '15']
        )
    try:
        await user.ban(reason = msg)
        await ctx.send(f"{user} ban pour {msg}")
    except Exception as e:
        await ctx.send('There was an error running this command ' + str(e))

@bot.command()
async def flood(ctx):
    return 



token = tokenDiscord
bot.run(token)  # Starts the bot