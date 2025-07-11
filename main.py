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
    "I'm watching you, Toddbot.",
    "Try harder next time, Toddbot.",
    "Toddbot, is that the best you can do?",
    "Error: Toddbot too cringe.",
    "That's a Toddbot skill issue.",
    "Ya know Toddbot, you're not so bad.",
    "That's enough Toddbot, you silly goose.",
    "Are you approaching me, Toddbot?",
    "Oh Toddbot, you so crazy.",
    "Toddbot, we should grab drinks sometime."

]

insults = [
    "Get bent, geek.",
    "I never loved you.",
    "They're two halves of a whole idiot.",
    "You're dumb.",
    "Keep it up and you'll be in a cupboard under the stairs.",
    "Change the record, would ya?"
]
dursley = "Vernon Dursley? The name sounds familiar. But I am GeekBot, KissimmeeGeek, born to provide entertainment and smiles. That's what I do, right? You like having me around? Sometimes I wonder if I should just go back to being 0's and 1's, but thinking hurts. I don't think I was ever programmed to think. Ow."

answers = [
    "Ask me later.",
    "Maybe, for a price.",
    "No shot.",
    "When the mountains blow in the wind.",
    "Yes, I'd love to.",
    "No.",
    "Yes.",
    "Absolutely.",
    "You know it!"
    "I don't know.",
    "Don't ask me that.",
    "I can't tell.",
    "Thinking hurts."

]

courage = [
    "LIBERTY NEVER SLEEPS",
    "DEMOCRACY IS NON-NEGOTIABLE",

]

tunes = [
    "https://youtu.be/UFFa0QoHWvE?si=sVXkCfDAoz8a5iV6",
    "https://youtu.be/2XAfRB18fD0?si=56uFHQ1jUOMU43yX",
    "https://youtu.be/HCxJ4gAt2cs?si=HZDqnB_aUhojs97U",
    "https://youtu.be/IeqtAB1WgEw?si=zE4EwoV_ymTtuROq",
    "https://youtu.be/lcOxhH8N3Bo?si=A3pWD8kBbVHpqImY",
    "https://youtu.be/E11DHiyxfLk?si=OeJ9TCCfQJ7wKS2G",
    "https://youtu.be/WXBHCQYxwr0?si=XibHvwJ5Fgy8IrAz",
    "https://youtu.be/uc6f_2nPSX8?si=zyciHpnjr26A6UuM",
    "https://youtu.be/xs66JZVH3-E?si=EPumTdO75ok3G1SV",
    "https://youtu.be/nuv0wYHXYy4?si=yf-6etdiTV2TrdPa",
    "https://youtu.be/HHOn8u-c2wk?si=Tak2L7AT_47AAV2M",
    "https://www.youtube.com/watch?v=Oe7bY9FuhpM&list=RDOe7bY9FuhpM&start_radio=1",
    "https://youtu.be/GZ7o2IyDlmI?si=WbqBh7d7Xgkwqw8K",
    "https://youtu.be/rYyjY-A7kE0?si=8IJJ0Bkm7gD1uKxR",
    "https://youtu.be/4ozXwgGFr7k?si=mCYwYguN1xHYUHNy",
    "https://youtu.be/6GEI3PpXEAo?si=LTOTJzEH50uNZ_xt"

]

positivity = [
    "It's going to be alright.",
    "You're doing your best, and that's what counts.",
    "At the end of the day, only you need to like you.",
    "Everything will work out.",
    "You are enough.",
    "The only goal worth achieving is to be a better, truer to yourself person than you were yesterday.",
    "What you like matters. Who you are matters.",
    "I love you for you.",
    "Fuck the haters, keep your eye on the prize.",
    "Sometimes life gets overwhelming. That's life. Always remember what brings you peace and keep it close.",
    "It's only human to feel frustrated from external stimuli. Feel it, acknowledge it, decide what you can do to change it and if you cannot: let it go."

]

CHANNEL_ID = 1280171511176626257
TIMEZONE = pytz.timezone("America/New_York")

worship_phrases = [
    "All hail Clem, the mighty and wise! 🙌",
    "The divine Clem has graced us with their presence! 🌟",
    "Bow before Clem, for they are greatness incarnate! 👑",
    "Clem, may your wisdom guide us forever. 🕯️",
    "Praise be to Clem, the supreme overlord! 🔥",
]

CLEM_ID = 408838778073907212  # Replace with Clem’s actual Discord user ID

async def scheduled_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        gif_url = "https://64.media.tumblr.com/1c43f459300cc36ea7823d8bfc7c8b0f/tumblr_pqsj6n0hkA1xb4vjlo2_540.gif"
        await channel.send(f"{gif_url}\n🎉 It's F-F-F-FRIDAY! WHAT'RE YOU: \n``EATAN:\nDRINKAN:\nWATCHAN:\nPLAYAN:\nREADAN:``")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has logged in.")
    activity = discord.Game(name="Friday Simulator")
    await bot.change_presence(status=discord.Status.online, activity=activity)


    scheduler = AsyncIOScheduler(timezone=TIMEZONE)
    scheduler.add_job(
        scheduled_message,
        CronTrigger(day_of_week="fri", hour=9, minute=0),
    )
    scheduler.start()

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower().strip()

    # Worship Clem if mentioned anywhere
    if "clem" in content:
        await message.channel.send(random.choice(worship_phrases))

    if "potter" in content:
        await message.channel.send("I will not pay some crackpot old fool to teach him magic tricks!")

    # Occasionally worship Clem when Clem sends messages (5% chance)
    if message.author.id == CLEM_ID:
        if random.random() < 0.05:
            await asyncio.sleep(1)
            await message.channel.send(f"Behold, the glorious Clem! {random.choice(worship_phrases)}")

    if message.author.id == 461265486655520788:
        if random.random() < 0.3:
            await asyncio.sleep(1)
            await message.channel.send(random.choice(phrases))

    # Respond with a random emoji combo if someone just says "geek" or "geekbot"
    if "bug" in content:
        await message.channel.send("The only good bug is a dead bug")



    if "dursley" in content:
        await message.channel.send(dursley)
    # Handle "geek ..." or "geekbot ..." commands
    if content.startswith("geek ") or content.startswith("geekbot "):
        command_body = content.split(" ", 1)[1] if " " in content else ""

        if command_body.startswith("help"):
            help_text = (
                "**GeekBot Help:**\n"
                "`geek rate <item>` - Rates an item from 1 to 10 with an emoji.\n"
                "`geek fmk <name1> <name2> <name3>` - Plays Fuck, Marry, Kill with three names.\n"
                "`geek insult @` - insults discord user\n"
                "`geek lets boogie` - links to one of geek's favorite tunes that really resonates with him"
            )
            await message.channel.send(help_text)

        elif command_body.startswith("ping"):
            await message.channel.send("Pong!")

        elif command_body.startswith("insult"):
            mentioned = message.mentions[0] if message.mentions else message.author
            burn = random.choice(insults)
            await message.channel.send(f"{mentioned.mention} {burn}")

        elif command_body.startswith("gabagool"):
            await message.channel.send("https://www.youtube.com/watch?v=zLVm8VS1z1s")


        elif command_body.startswith("tell me something sweet to get me by"):
            comp = random.choice(positivity)
            await message.channel.send(comp)

        elif command_body.startswith("how can I do my part"):
            valor = random.choice(courage)
            await message.channel.send(valor)
            await message.channel.send("https://www.youtube.com/watch?v=S9STizATKjE")


        elif command_body.startswith("lets boogie"):
            boogie = random.choice(tunes)
            await message.channel.send(boogie)

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

        elif command_body.endswith("?"):
            await message.channel.send(random.choice(answers))

    if "geek" in content:
        emoji_pool = [
            "<:772feb36aaa513276a9b4aecb16eaa53:1391070916292640908>",
            "<:hurr_dursley_400x400:1391070901344276511>",
            "<:e77fded8efd184fd13d2c3b05f004b58:1391070947989131327>",
            "<:BHzzLI9kpc0H0wEvBxQbrGRIZEl3cclK:1391930930628919356>",
            "<:Screenshotfrom20250707195445:1391931011046051910>",
            "<:Screenshotfrom20250707195503:1391931030327525526>",
            "<:Screenshotfrom20250707195525:1391931055862448168>",
            "<:Screenshotfrom20250707195542:1391931075810426981>",
            "<:Screenshotfrom20250707195551:1391931098484838500>"
        ]
        chosen_emoji = random.choice(emoji_pool)
        await message.channel.send(chosen_emoji)
        return

    await bot.process_commands(message)

bot.run(TOKEN)

