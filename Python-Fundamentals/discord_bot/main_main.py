import discord
client = discord.Client()
substring = ["play", "web", "nice", "http", "yes", "cya", "server", "working", "process"]
keywords = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        count = 0
        just_do_it = False
        i = None
        x = message.content.lower()
        for i in range(len(substring)):
            if x.find(substring[i]) != -1:
                return
        for k in range(len(keywords)):
            if keywords[k] in x:
                just_do_it = True
        if just_do_it is True:
            await message.channel.send(f"{message.author.mention} Кирилица...")


client.run("NzYwMTk2NzUxMzM5OTQ2MDM1.X3IiZQ.iKclYIvjrwjs4jk1OkJwjAzRVZ4")

# text_file = open("substring.txt", "r")
# lines = text_file.readlines()
# print (lines)
# print(len(lines))
# text_file.close()