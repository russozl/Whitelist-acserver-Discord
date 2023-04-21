# Whitelist-acserver-Discord
# Author: russozl
# Contact: russozl#1111
#
# Description: This script is a Discord bot that allows server administrators to manage a whitelist for an Assetto Corsa server.

import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

# Sets the path of the text file
path = r'C:\Users\youruser\whitelist.txt'

# Sets the ID of the role that can remove the user's code
role_id = 1075880077641912451

# Loads the whitelist codes from the whitelist.txt file
def load_whitelist():
    with open(path, 'r') as f:
        codes = f.read().splitlines()
    return codes

# Saves the list of codes to the whitelist.txt file
def save_whitelist(codes):
    with open(path, 'w') as f:
        for code in codes:
            f.write(code + '\n')

@client.event
async def on_member_update(before, after):
    # Checks if the user lost the specified role
    if any(role.id == role_id for role in before.roles) and not any(role.id == role_id for role in after.roles):
        # Removes the user's code from the whitelist codes list
        codes = load_whitelist()
        user_code = str(after.id)
        if user_code in codes:
            index = codes.index(user_code)
            if index > 0:
                code = codes[index - 1]
                codes.remove(code)
                codes.remove(user_code)
                save_whitelist(codes)
                print(f"Code {code} removed from the whitelist.")

@client.command()
async def whitelist(ctx, code: str = None):
    if code is None:
        # Sends a message in the "whitelist" channel
        await ctx.send(f"{ctx.author.mention}, please provide a 17-digit code found on your Steam account and send it in the whitelist registration channel.")
    elif len(code) != 17 or not code.isdigit():
        # Sends a message in the "whitelist" channel
        await ctx.send(f"{ctx.author.mention}, invalid code! Make sure the code is 17 digits long and consists only of numbers. The code can be found on your Steam account.")
    else:
        # Loads the whitelist codes from the whitelist.txt file
        codes = load_whitelist()

        # Checks if the user has already added a code to the list
        user_code = str(ctx.author.id)
        if user_code in codes:
            # Sends a message in the "whitelist" channel
            await ctx.send(f"{ctx.author.mention}, you have already added a code to the list. If you need to add another code, please contact an administrator.")
        elif code in codes:
            # Sends a message in the "whitelist" channel
            await ctx.send(f"{ctx.author.mention}, this whitelist code has already been added to the list. If you need to add another code, please contact an administrator.")
        else:
            # Adds the new code to the whitelist codes list
            codes.append(code)
            # Adds the user ID to the list to check if they have already added a code
            codes.append(user_code)
            # Saves the updated list to the whitelist.txt file
            save_whitelist(codes)

            # Adiciona a role "passed" ao usuário
            user = ctx.author
            role = discord.utils.get(user.guild.roles, name="passed")
            await user.add_roles(role)

            # Sends a message in the "whitelist" channel
            await ctx.send(f"{ctx.author.mention}, whitelist successfully released! Please proceed to the download channel to complete the installation.")

          client.run('your discord bot token')
