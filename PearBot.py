import discord, json

with open("settings.json", "r") as json_file:
    settings = json.load(json_file)

client = discord.Client()

@client.event
async def on_ready():
    print(f"Bot is ready! \nLogged in as {client.user}")

@client.event
async def on_message(message):
    id = client.get_guild(settings["server_id"])
    if str(message.author) != str(client.user):
        print(f"{message.author.name}@{message.channel}> {message.content}")
        for word in settings["welcome"]:
            if word in str(message.content).lower():
                await message.channel.send("Welcome")
        if str(message.channel) in settings["cmd_channels"]:
            if str(message.content) == "!users":
                await message.channel.send(f"Number of users is: {id.member_count}")
    
client.run(str(settings["token"]))