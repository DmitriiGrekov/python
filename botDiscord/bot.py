import discord
import youtube_dl
import os
from discord.ext import commands
from discord.utils import get


client = commands.Bot(command_prefix = '.')


@client.event

async def on_ready():
    print("Bot connected")




@client.command(pass_context = True)
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello {author.mention}, I am a Bot for discord')

#connect

token =  'Njk5NjkyOTMyODMxMjQ4Mzg0.Xpis2g.FmFJqHBngiQNHIMYq_LXzF0gHOY'




@client.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients,guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот присоединился к каналу:{channel}')




@client.command()
async def leave(ctx):
    
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients,guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот оключился от канала:{channel}')




@client.command()
async def play(ctx,url:str):
    song_there = os.path.isfile('song.mp3')

    try:
        if song_there:
            os.remove('song.mp3')
            print('Старый файл удалён')

    except PermissionError:
        print('не удалось удалить файл')
    await ctx.send('Пожалуйста ожидайте')
    voice = get(client.voice_clients,guild = ctx.guild)
    
    ydl_opts = {
            'format':'besstaudio/best',
            'postprocessors':[{
                'key':'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'192',
                }],
            }
    with  youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Загружаю музыку')
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'Переименовываю файл {file}')
            os.rename(file,'song.mp3')
    voice.play(discord.FFmpegPCMAudio('song.mp3'),after = lambda e:print({name},'закончила своё проигрывание'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    song_name = name.rsplit('-',2)
    await ctx.send(f'Сейчас пригрывается музыка: {song_name[0]}')















client.run(token)
