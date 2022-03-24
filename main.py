import discord
import os
import random
import requests
import json

client = discord.Client()

bad_word = [
  "anjing", 
  "monyet",
  "tolol", 
  "bangsat", 
  "ngentot", 
  "goblok",
  "nigga",
  "tai",
]

sewot_word = [
  "Santai dong mas",
  "Mohon bahasanya dijaga ya goblok",
  "Anda ngomong kasar!, minus 1000000000 social credit",
  "Bahasanya dijaga ya!",
  "Astagfirullah ngomongnya",
  "Tidak santai ya"
]

# kopit indo
def get_covidind():
  response = requests.get("https://api.kawalcorona.com/indonesia/provinsi")
  json_data = json.loads(response.text)
  covidind = json_data[0]['Provinsi']
  return(covidind)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('Selamat pagi'):
    await message.channel.send('Bacot')

  if message.content.startswith('curhat'):
    await message.channel.send('Ngomong ama pantat')

  if msg.startswith('$covid'):
    covidind = get_covidind()
    await message.channel.send(covidind)

  if any(word in msg for word in bad_word):
    await message.channel.send(random.choice(sewot_word))

client.run(OTM1NzI1OTYwODI3OTIwNDQ0.YfC0tg.Fe3d-TE5MsJJZ_P5Gq6-tel7a2M)
