import discord
import openai
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

openai.api_key = "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"

@bot.command(name='The-V')
async def chat_with_gpt(ctx, *, message):
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=60
    )
    
    await ctx.send(response.choices[0].text)
bot.run('MTA5ODE4MzgxODE2NDMyNjQxMA.GeIrTG.ZRQsqSfjDnR8PgdJB4m6QBK9EA1rc5Xv3vJi2g')