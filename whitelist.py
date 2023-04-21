# Whitelist-acserver-Discord
# Author: russozl
# Contact: russozl#1111
#
# Description: This script is a Discord bot that allows server administrators to manage a whitelist for an Assetto Corsa server.

import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

# Define o caminho do arquivo de texto
path = r'C:\Users\sergi\Desktop\saitama bot\whitelist.txt'

# Define o ID do cargo que pode remover o código do usuário
role_id = 1075880077641912451

# Carrega a lista de códigos de whitelist do arquivo whitelist.txt
def load_whitelist():
    with open(path, 'r') as f:
        codes = f.read().splitlines()
    return codes

# Salva a lista de códigos no arquivo whitelist.txt
def save_whitelist(codes):
    with open(path, 'w') as f:
        for code in codes:
            f.write(code + '\n')

@client.event
async def on_member_update(before, after):
    # Verifica se o usuário perdeu o cargo especificado
    if any(role.id == role_id for role in before.roles) and not any(role.id == role_id for role in after.roles):
        # Remove o código do usuário da lista de códigos de whitelist
        codes = load_whitelist()
        user_code = str(after.id)
        if user_code in codes:
            index = codes.index(user_code)
            if index > 0:
                code = codes[index - 1]
                codes.remove(code)
                codes.remove(user_code)
                save_whitelist(codes)
                print(f"Código {code} removido da lista de whitelist.")

@client.command()
async def whitelist(ctx, code: str = None):
    if code is None:
        # Envia a mensagem no canal de "whitelist"
        await ctx.send(f"{ctx.author.mention}, por favor, forneça um código de 17 dígitos encontrado na sua conta Steam e envie-o no canal de registro de whitelist.")
    elif len(code) != 17 or not code.isdigit():
        # Envia a mensagem no canal de "whitelist"
        await ctx.send(f"{ctx.author.mention}, código inválido! Verifique se o código tem 17 dígitos e é composto apenas de números. O código pode ser encontrado na sua conta Steam.")
    else:
        # Carrega a lista de códigos de whitelist do arquivo whitelist.txt
        codes = load_whitelist()

        # Verifica se o usuário já adicionou um código à lista
        user_code = str(ctx.author.id)
        if user_code in codes:
            # Envia a mensagem no canal de "whitelist"
            await ctx.send(f"{ctx.author.mention}, você já adicionou um código à lista. Se precisar adicionar outro código, entre em contato com um administrador.")
        elif code in codes:
            # Envia a mensagem no canal de "whitelist"
            await ctx.send(f"{ctx.author.mention}, esse código de whitelist já foi adicionado à lista. Se precisar adicionar outro código, entre em contato com um administrador.")
        else:
            # Adiciona o novo código à lista de códigos de whitelist
            codes.append(code)
            # Adiciona o ID do usuário à lista para verificar se ele já adicionou um código
            codes.append(user_code)
            # Salva a lista atualizada no arquivo whitelist.txt
            save_whitelist(codes)

            # Adiciona a role "passed" ao usuário
            user = ctx.author
            role = discord.utils.get(user.guild.roles, name="passed")
            await user.add_roles(role)

            # Envia a mensagem no canal de "whitelist"
            await ctx.send(f"{ctx.author.mention}, whitelist liberada com sucesso! Por favor, siga para o canal de download para concluir a instalação.")

