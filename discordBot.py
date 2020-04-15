
from googletrans import Translator
import googletrans
translator = Translator()
#pip install googletrans
#https://stackabuse.com/text-translation-with-google-translate-api-in-python/
import discord
from discord.ext import commands
import emoji
import random

bot = commands.Bot(command_prefix='!')

lang='russian'
@bot.event
async def on_ready():
    print('Logged in')

@bot.command()
async def t(ctx, *sentence):
    original = emoji.demojize(' '.join(sentence))
    translated = translator.translate(original, src='nl', dest='ru').text

    #await ctx.channel.send(original)
    await ctx.channel.send(emoji.emojize(translated))

@bot.command()
async def reverse(ctx, *sentence):
    reversedStr= (' '.join(sentence))[::-1]
    await ctx.channel.send(reversedStr)

@bot.command()
async def set(ctx, language):
    global lang
    if language in googletrans.LANGUAGES:
        lang = language
        await ctx.channel.send("Set translate language to {}".format(googletrans.LANGUAGES[lang]))
    else:
        await ctx.channel.send("Language not found")



@bot.command()
async def languages(ctx):
    await ctx.channel.send(googletrans.LANGUAGES)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    if times > 5:
        await ctx.send("Repeat limit exceeded")
        return
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


bot.run('TOKEN')
