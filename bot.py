import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    """Bot, kullanıcıya selam gönderir."""
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def sanslısayı(ctx):
    """Rastgele bir şanslı sayı (1 ile 100 arasında) seçer."""
    sayı = random.randint(1, 100)
    await ctx.send(f"🎰 Şanslı sayınız: {sayı}")

@bot.command()
async def tarih(ctx, member: discord.Member):
    """Bir kullanıcının sunucuya katılma tarihini gösterir."""
    await ctx.send(f'{member.name}  {discord.utils.format_dt(member.joined_at)} Katıldı')

@bot.command()
async def heh(ctx, count_heh=5):
    """Kullanıcıya 'he' kelimesi belirtilen sayıda tekrar edilir. Varsayılan 5'tir."""
    await ctx.send("he" * count_heh)

@bot.command()
async def kullanıcıbilgi(ctx, member: discord.Member):
    """Bir kullanıcının adı, katılma tarihi ve rolü hakkında bilgi verir."""
    await ctx.send(f"**Kullanıcı Bilgisi**:\n"
                   f"Adı: {member.name}\n"
                   f"Katılma Tarihi: {discord.utils.format_dt(member.joined_at)}\n"
                   f"Rol: {member.top_role.name}")

@bot.command()
async def komutlar(ctx):
    """Botun tüm komutlarını ve açıklamalarını listeler."""
    komutlar_listesi = (
        "$hello - Bot, kullanıcıya selam gönderir.\n"
        "$sanslısayı - Rastgele bir şanslı sayı (1 ile 100 arasında) seçer.\n"
        "$tarih <@kullanıcı> - Kullanıcının sunucuya katılma tarihini gösterir.\n"
        "$heh [count] - 'he' kelimesini belirtilen sayıda tekrar eder (Varsayılan: 5).\n"
        "$kullanıcıbilgi <@kullanıcı> - Kullanıcının adı, katılma tarihi ve rolü hakkında bilgi verir."
    )
    await ctx.send(f"**Mevcut Komutlar:**\n{komutlar_listesi}")

bot.run("TOKEN")
