import discord
from discord.ext import commands
from model import get_class
import os
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
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            try:
                clase = get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}")
                if clase == "Gorriones":
                    await ctx.send("Los gorriones se alimentan principalmente semillas. En la mayoría de los casos, gran parte de su dieta se basa en semillas de hierbas y malezas o residuos de granos.")
                elif clase == "Palomas":
                    await ctx.send("Las palomas se alimenta de granos desechados, semillas de muchas hierbas y otras plantas y a veces de bayas o bellotas; puede comer algunas lombrices o insectos.")
                #await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
            except:
                await ctx.send("Formato de imagen incorrecto, trata de usar JPG, PNG, JPEG... :)")
            
            os.remove(f"./{attachment.filename}")
    else:
        await ctx.send("Olvidaste subir la imagen :(")

bot.run("TU TOKEN")
