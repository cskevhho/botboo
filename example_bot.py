import nextcord
import os
import random
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

GUILD_ID = int(os.getenv("GUILD_ID")) 
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'Successfully logged in as {bot.user}')

@bot.slash_command(description="Slash Command Test", guild_ids=[GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Slash Command Successful")


@bot.slash_command(description="Heads or Tails", guild_ids=[GUILD_ID])
async def hot(interaction: nextcord.Interaction, arg: str):
    cpu_decision = random.choice(["heads", "tails"])

    if cpu_decision == arg.lower():
        await interaction.response.send_message(f"PLY: {arg} // CPU: {cpu_decision}, You Win")
    else:
        await interaction.response.send_message(f"PLY: {arg} // CPU: {cpu_decision}, You Lose")


bot.run(BOT_TOKEN)
