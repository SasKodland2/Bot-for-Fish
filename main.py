import discord, random, requests, os
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'{file_name}')
            await ctx.send(f'file disimpan atas nama {file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt', file_name)

            if hasil[0] == 'ikan nila\n' and hasil[1] >=0.6:
                await ctx.send("Ini adalah Ikan Nila!")
                await ctx.send("Ikan nila adalah sejenis ikan konsumsi air tawar. Ikan ini diintroduksi dari Afrika,tepatnya Afrika bagian timur, pada tahun 1969, dan kini menjadi ikan peliharaan yang populer di kolam-kolam air tawar di Indonesia sekaligus hama di setiap sungai dan danau Indonesia. Nama ilmiahnya adalah Oreochromis niloticus, dan dalam bahasa Inggris dikenal sebagai Nile Tilapia.")

            elif hasil[0] == 'ikan gurami\n' and hasil[1] >=0.6:
                await ctx.send("Ini adalah Ikan Gurami!")
                await ctx.send("Gurami atau gurame (Osphronemus gouramy) adalah sejenis ikan air tawar yang populer sebagai ikan konsumsi di Asia Tenggara dan Asia Selatan. Di samping itu, gurami juga sering dipelihara dalam akuarium.")

            else :
                await ctx.send("Gambar Tidak Valid :((")
    else:
        await ctx.send('ANDA TIDAK MENGIRIM APAPUN :((')

bot.run('apa hayo')
