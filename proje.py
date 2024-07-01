import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
cevre_bilinci_listesi = ["tabii ki çevre karşı bilinçli olmak için toplu taşıma araçları kullanımı artırıp kişisel araçların kullanımı azaltılmalıdır"
,"karbondioksit salınımını azaltılabiliriz"
,"çöp atanları uyaralım"]

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def cevre_bilinci(ctx):
    await ctx.send(random.choice(cevre_bilinci_listesi))

@bot.command()
async def bilresim(ctx):
    bilinc_list = os.listdir("proje1/images")
    bil = random.choice(bilinc_list)
    with open(f"proje1/images/{bil}", 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)




bot.run("")