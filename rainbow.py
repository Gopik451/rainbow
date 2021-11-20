import discord
import asyncio
import random

token = 'OTExNjUwMzgyODk4NDA1NDE3.YZkelA.rzL0Y7n-1RL8EUuQKhXi0PMLSFs'
serverid = 897842308077207593
rainbowrolename = "RAINBOW"
delay = 12


client = discord.Client()
colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]

async def rainbowrole(role):
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            print("detected role")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("")
                    pass
                await asyncio.sleep(delay)
    print('Нет роли ' + rainbowrolename)
    print("Создание роли...")
    try:
        await client.get_guild(serverid).create_role(reason="Создана роль", name=rainbowrolename)
        print("Роль создана!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("Нет прав на изменение роли RAINBOW")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))

@client.event
async def on_ready():
    client.loop.create_task(rainbowrole(rainbowrolename))
    print('Залогиннен как')
    print(client.user.name)
    print(client.user.id)
    print('Подключен.')
    print('------------')

client.run(token)