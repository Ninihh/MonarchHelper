import discord
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot ligado com sucesso como: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.bot and len(message.embeds) > 0:
        print(f"🎯 ALERTA: Mensagem com Embed detetada do bot: {message.author.name}")

    if message.content.lower() == 'm!ping':
        try:
            await message.channel.send('Pong!')
            print("✅ Respondi 'Pong!' com sucesso no chat!")
        except Exception as e:
            print(f"❌ Erro ao tentar enviar mensagem: {e}")

# Inicia o servidor web em segundo plano para o Render não dar timeout
keep_alive()

client.run('MTU2NDgxNTM5MDgwOTUyNjMwMg.G8PNrt.oFZSgEbmi_BuyW1ps1wvCr_BBDqvPCcqysxDNo')
      
