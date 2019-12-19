import discord, json

with open("settings.json", "r") as json_file:
    settings = json.load(json_file)

client = discord.Client()

@client.event
async def on_ready():
    print(f"Bot is ready! \nLogged in as {client.user}")

@client.event
async def on_message(message):
    print(f"{message.author.name}> {message.content}")
    if message.content in settings["welcome"]:
        await message.channel.send("Welcome")

client.run(str(settings["token"]))