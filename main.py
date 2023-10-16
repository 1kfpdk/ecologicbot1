python
import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

podelki = [
    "Венок из сухих цветов",
    "Корзинка из ивовых прутьев",
    "Каменные браслеты",
    "Поделка из ракушек",
    "Картина из листьев",
    "Поделка из сосновых шишек"
]

@bot.command()
async def podelka(ctx):
    chosen_podelka = random.choice(podelki)
    await ctx.send(f"Случайная поделка из природных материалов: {chosen_podelka}")

@bot.command()
async def add_podelka(ctx, *, podelka):
    podelki.append(podelka)
    await ctx.send(f"Новая поделка успешно добавлена!")

@bot.command()
async def remove_podelka(ctx, *, podelka):
    if podelka in podelki:
        podelki.remove(podelka)
        await ctx.send(f"Поделка успешно удалена!")
    else:
        await ctx.send(f"Поделка не найдена!")

bot.run('MTE1Mjk2MzQyNTQ1NTA1ODk0NA.G7QF6y.hUn-N4f4jWaC0I-_kr3bYQsi-Z5WgeqFgXev2c')

