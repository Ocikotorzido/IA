import discord

llave = "ODI2NTcxMTQwNTE5ODIxMzQy.YGOaXA.NTyNVAFbshwtKcmPJfNdpu_nG3U"

cliente=discord.Client()
@cliente.event
async def on_message(mensaje):
	if mensaje.content.find("Hola")!=-1:
		await mensaje.channel.send("Hola! desde discord")
cliente.run(llave)
