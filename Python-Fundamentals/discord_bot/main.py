import discord

from sensitive_data import token

client = discord.Client()
keywords = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


def remove_newlines(fname):
    flist = open("substring.txt").readlines()
    return [s.rstrip('\n') for s in flist]


substring = (remove_newlines("substring.txt"))
print(substring)
print(len(substring))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    rip = False

    count = 0
    just_do_it = False
    x = message.content.lower()
    for i in range(len(substring)):
        if x.find(substring[i]) != -1:
            rip = True
    if rip is False:
        for k in range(len(keywords)):
            if keywords[k] in x:
                just_do_it = True
        if just_do_it is True:
            await message.channel.send(f"{message.author.mention} Кирилица...")




client.run(token)
