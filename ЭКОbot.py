import discord
from discord.ext import commands
import os, random

client = commands.Bot(command_prefix='$',intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f"Вы зашли как ЭКОbot#5003")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Привет! Я бот!')
    if message.content.startswith('$правила'):
        await message.channel.send('1) Покупать только то что действительно необходимо 2) Сдавать отходы на переработку 3) Ответственно избавляться от опасных отходов 4) Ходить за покупками с многоразовой сумкой 5) Все же выключать воду 6) Избегать одноразовой посуды 7) Выключать свет и электроприборы из сети 8) Полностью загружать стиральную и посудомоечную машины 9) При готовке накрывать крышкой кастрюли и сковороды 10) Убавлять мощность отопления, если возможно 11) Предпочитать личному автомобилю общественный транспорт 12) Печатать на бумаге с двух сторон 13) Во время праздников отказаться от воздушных шаров 14) Удалять неактуальные имейлы, фотографии из соцсетей, файлообменников 15) Иногда отказываться от мяса 16) Интересоваться экологией и делиться информацией с другими')   
    if message.content.startswith('$commands'):
        await message.channel.send('Привет! Этот бот имеет такие команды как: $hello $эко $аудитория $commands $картинки $правила')
    if message.content.startswith('$эко'):
        await message.channel.send('Естественная наука о взаимодействиях живых организмов между собой и с их средой обитания, об организации и функционировании биосистем различных уровней.')
    if message.content.startswith('$аудитория'):
        await message.channel.send('Люди, которые заботятся о окружающей среде и хотят узнать больше об экологичных практиках и способах уменьшения отходов')   
 
client.run("MTExMzQ4NzM3OTgzMjAwMDYyMw.GSUmZs.ILr0JBacDS7KMs86p3RxBTuadA5Y4ikMMOfD5M")
