import discord
from discord.ext import commands
from netmiko import Netmiko

TOKEN = "<paste_your_token_here"

client = commands.Bot(command_prefix = "$")


@client.event
async def on_ready():
    print("I am ready !..")


@client.command(name= "get_interface")
async def get_interface(ctx,arg1 ,interface):
    
    net_connect = Netmiko(
        host = arg1,
        username = "cisco",
        password = "admin",
        device_type = "cisco_ios")
    
    output = net_connect.send_command_expect("show ip interface brief", use_genie=True)
    parsed = output["interface"][interface]["ip_address"]
    
    net_connect.disconnect()
    await ctx.send(parsed)

@client.command(name="get_interface_status")
async def get_interface_status(ctx,arg1):
    
    net_connect = Netmiko(
        host = arg1,
        username = "cisco",
        password = "admin",
        device_type = "cisco_ios")
    parsed=""
    output = net_connect.send_command_expect("show ip interface brief", use_genie=True)
    for n in output["interface"]:
        status = output["interface"][n]["status"]
        parsed += n + " = " + status + "\n"
        
    net_connect.disconnect()

    await ctx.send(parsed)
    
client.run(TOKEN)
