import discord
from discord.ext import commands

import os
import random
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")
CURRENCY_TOKEN = os.environ.get("CURRENCY_TOKEN")
currency_url = "https://api.currencyapi.com/v3/latest"
currency_headers = {"apikey": CURRENCY_TOKEN}
cevap_url = "https://yesno.wtf/api"
kisalt_url = "https://is.gd/create.php"
ad_url = "https://api.adviceslip.com/advice"
import requests
# izinler 

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
bot = commands.Bot(command_prefix="/", intents= intents)

@bot.event

async def on_ready():

    print(f"{bot.user.name} is logged in")

@bot.event

async def on_message(message):

    if message.author == bot.user:

        return
    if message.content.startswith("i am coming daddy ahh"):
        
        await message.channel.send(f"i am coming too ahhhhh")
        
    if message.content.startswith("hello"):

        await message.channel.send(f"Hello, I am {bot.user.name}")
        
    await bot.process_commands(message)
mesaj = input("açılım mesajı gir")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command(name="gay")
async def gay(ctx, sh):
    a = random.randint(1, 100)
    await ctx.send(f"{sh} %{a} gaydir şu anda")
@bot.command(name="flag")
async def flag(ctx, country):
    country = country.upper()
    if country == "TR":
        await ctx.send(f"Türk geçiyor as bayrakları:flag_tr::drum::drum::flag_tr:")
    await ctx.send(f"https://flagsapi.com/{country}/flat/64.png")
@bot.command(name="tavsiye")
async def tavsiye(ctx):
    response = requests.get(ad_url)
    all_data = response.json()
    dum_data = all_data['slip']
    rom_data = dum_data['advice']
    await ctx.send(f"işte tavsiye:{rom_data}")
@bot.command(name="breakingbad")
async def breakingbad(ctx):
    response = requests.get("https://api.breakingbadquotes.xyz/v1/quotes")
    all_data = response.json()
    kut = all_data[0]
    s = kut["quote"]
    y = kut["author"]
    await ctx.send(f"{s} - {y}")
@bot.command(name = "dolar")
async def dolar(ctx):
    response = requests.get(currency_url, headers=currency_headers)
    all_data = response.json()
    try_data = all_data["data"]["TRY"]["value"]
    await ctx.send(f"1 dolar = {try_data} türklirası")
@bot.command(name = "start")
async def start(ctx):
    await ctx.send(f"Merhaba bu botun sahibinden bu mesajı alıyor sunuz lütfen sahiplik çıkarmayın veya kötüye kullanmayın eğer yazım hatası bulursanız boş yapmayın. komut listesi:(başına ! getirmeyi unutmayın)!dolar(1 dolar kaç tl gösterir)!flag(bir ülkenin 2 harfli kodunu girdiğinizde ülkenin bayrağını gösterir yanlış girerseniz sadece link çıkar)[1 nisan 2024, 1.04.2024]")
@bot.command(name="evethayir")
async def evethayir(ctx):
    response = requests.get(cevap_url)
    all_data = response.json()
    cevap_data = all_data["image"]
    await ctx.send(f"cevabın:||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| {cevap_data}")
@bot.command(name = "komutlar")
async def komutlar(ctx):
    await ctx.send(f"!komutlar: bu mesajı gösterir")
    await ctx.send(f"!meme: bir tane rasgele seçilmiş mem gösterir")
    await ctx.send(f"!gay (x) bir kişinin yüzde kaç gay olduğunu söyler")
    await ctx.send(f"!duck rastgele ördek fotoğrafı gösterir")
    await ctx.send(f"!start: önemli bilgiler verir (mutlaka oku):saluting_face: ")
    await ctx.send(f"!tavsiye: size bir hayat tavsiyesi verir(ingilizce)")
    await ctx.send(f"!breakingbad: breaking bad'den bir cümle söyler(ingilizcedir)")
    await ctx.send(f"!dolar: 1 doların kaç tl olduğunu gösterir:moneybag:")
    await ctx.send(f"!flag (x): bir ülkenin ilk iki harfli kodunu girince bayrağını gösterir:flag_tr:")
    await ctx.send(f"!evethayir 50/50 evet mi hayırmı için:x: :white_check_mark: ")
    await ctx.send(f"!sahipmesaj: botu başlatırken girilen yazıyı verir(sadece sahip değiştirebilir)")
    await ctx.send(f"!echo (x): söylediğin mesajı tekrar söyler:repeat: ")
    await ctx.send(f"(ünlemsiz)hello: bot ismini söyleyerek merhaba der:man::hand_splayed: ")
    await ctx.send(f"(ünlemsiz)i am coming daddy ahh: bence denemeyin bile...:skull:")
    await ctx.send(f"başlangıcınız hayırlı uğurlu olsun:partying_face:")
@bot.command(name="sahipmesaj")
async def sahipmesaj(ctx):
    await ctx.send(mesaj)
@bot.command(name="echo")
async def ehco(ctx, mas):
    await ctx.send(mas)
meme_list = os.listdir("./memes")
@bot.command(name="meme")
async def meme(ctx):
    selected_meme = random.choice(meme_list)
    file = os.path.join(f"./memes/{selected_meme}")
    with open(file, "rb") as doc:
        picture = discord.File(doc)
    await ctx.send(file = picture)
@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
bot.run(TOKEN)