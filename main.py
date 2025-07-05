import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=None, intents=intents)

bot.case_insensitive = True

phrases = [
    "I'm watching you.",
    "Try harder next time.",
    "Did you really think that would work?",
    "Error: User too cringe.",
    "That's a skill issue."
]

CHANNEL_ID = 123456789012345678
TIMEZONE = pytz.timezone("America/New_York")

worship_phrases = [
    "All hail Clem, the mighty and wise! 🙌",
    "The divine Clem has graced us with their presence! 🌟",
    "Bow before Clem, for they are greatness incarnate! 👑",
    "Clem, may your wisdom guide us forever. 🕯️",
    "Praise be to Clem, the supreme overlord! 🔥",
]

CLEM_ID = 123456789012345678  # Replace with Clem’s actual Discord user ID

async def scheduled_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        gif_url = "https://64.media.tumblr.com/1c43f459300cc36ea7823d8bfc7c8b0f/tumblr_pqsj6n0hkA1xb4vjlo2_540.gif"
        await channel.send("🎉 It's F-F-F-FRIDAY! WHAT'RE YOU: ``EATAN:\nDRINKAN:\nWATCHAN:\nPLAYAN:\nREADAN:``")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has logged in.")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(name="insult")
async def insult(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    burn = random.choice(phrases)
    await ctx.send(f"{member.mention} {burn}")

@bot.command(name="rate")
async def rate(ctx, *, item: str = None):
    if not item:
        await ctx.send("Rate what? Try `!rate your questionable idea`")
        return

    score = random.randint(1, 10)
    reactions = [
        "🔥", "💩", "👍", "👎", "🤖", "😬", "💀", "😂", "🍕", "🎯"
    ]
    response = f"{item.capitalize()}? {score}/10. {random.choice(reactions)}"
    await ctx.send(response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower().strip()

    # Worship Clem if mentioned anywhere
    if "clem" in content:
        await message.channel.send(random.choice(worship_phrases))

    # Occasionally worship Clem when Clem sends messages (10% chance)
    if message.author.id == CLEM_ID:
        if random.random() < 0.1:
            await asyncio.sleep(1)
            await message.channel.send(f"Behold, the glorious Clem! {random.choice(worship_phrases)}")

    # Respond with a random emoji combo if someone just says "geek" or "geekbot"
    if content == "geek" or content == "geekbot" or content == "geek bot":
        emoji_pool = [
            "<:772feb36aaa513276a9b4aecb16eaa53:1391070916292640908>",
            "<:hurr_dursley_400x400:1391070901344276511>",
            "<:e77fded8efd184fd13d2c3b05f004b58:1391070947989131327>"
        ]
        chosen_emoji = random.choice(emoji_pool)
        await message.channel.send(chosen_emoji)
        return

    # Handle "geek ..." or "geekbot ..." commands
    if content.startswith("geek ") or content.startswith("geekbot "):
        command_body = content.split(" ", 1)[1] if " " in content else ""

        if command_body.startswith("help"):
            help_text = (
                "**GeekBot Help:**\n"
                "`geek rate <item>` - Rates an item from 1 to 10 with an emoji.\n"
                "`geek fmk <name1> <name2> <name3>` - Plays Fuck, Marry, Kill with three names."
            )
            await message.channel.send(help_text)

        elif command_body.startswith("ping"):
            await message.channel.send("Pong!")

        elif command_body.startswith("insult"):
            mentioned = message.mentions[0] if message.mentions else message.author
            burn = random.choice(phrases)
            await message.channel.send(f"{mentioned.mention} {burn}")

        elif command_body.startswith("rate"):
            item = command_body[5:].strip()
            if not item:
                await message.channel.send("Rate what? Try `geek rate tacos`")
            else:
                score = random.randint(1, 10)
                emoji = random.choice(["🔥", "💩", "👍", "👎", "🤖", "💀", "😂"])
                await message.channel.send(f"{item.capitalize()}? {score}/10. {emoji}")

        elif command_body.startswith(("fmk", "fuckmarrykill")):
            args = command_body.split()[1:]
            if len(args) != 3:
                await message.channel.send("Please provide exactly three names, e.g., `geek fmk Alice Bob Charlie`")
            else:
                choices = ["Fuck", "Marry", "Kill"]
                random.shuffle(choices)
                response = "\n".join(f"**{choice}:** {name.capitalize()}" for choice, name in zip(choices, args))
                await message.channel.send(response)

    await bot.process_commands(message)

bot.run(TOKEN)
