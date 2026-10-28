import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot ligado com sucesso como: {client.user}')

@client.event
async def on_message(message):
    # Ignora mensagens do próprio bot
    if message.author == client.user:
        return

    # Se a mensagem veio do Monarch e tem embeds (o formato de spawn do Pokémon)
    if message.author.name == "Monarch" and len(message.embeds) > 0:
        print("🎯 ALERTA: O Monarch mandou um Embed (possível Pokémon)!")

    # Resposta ao comando com o novo prefixo m!ping
    if message.content.lower() == 'm!ping':
        try:
            await message.channel.send('Pong!')
            print("✅ Respondi 'Pong!' com sucesso no chat!")
        except Exception as e:
            print(f"❌ Erro ao tentar enviar mensagem: {e}")

client.run('MTU2NDgxNTM5MDgwOTUyNjMwMg.G8PNrt.oFZSgEbmi_BuyW1ps1wvCr_BBDqvPCcqysxDNo')
