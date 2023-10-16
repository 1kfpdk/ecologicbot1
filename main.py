python
import discord
from discord.ext import commands
import random

# Создание экземпляра бота
bot = commands.Bot(command_prefix='!')

# Список вариантов поделок из природных материалов
podelki = [
    "Венок из сухих цветов",
    "Корзинка из ивовых прутьев",
    "Каменные браслеты",
    "Поделка из ракушек",
    "Картина из листьев",
    "Поделка из сосновых шишек"
]

# Команда для выбора случайной поделки
@bot.command()
async def podelka(ctx):
    chosen_podelka = random.choice(podelki)
    await ctx.send(f"Случайная поделка из природных материалов: {chosen_podelka}")

# Запуск бота
bot.run('YOUR_BOT_TOKEN'
