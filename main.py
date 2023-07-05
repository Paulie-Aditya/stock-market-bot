import requests


import config

'''
import nextcord
from nextcord.ext import commands


prefix = "&"
bot = commands.Bot(command_prefix = prefix, intents = nextcord.Intents.all(), activity= nextcord.Activity(type= nextcord.ActivityType.streaming, name= '/start', url="https://github.com/Paulie-Aditya/quiz_bot"))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.slash_command(name = 'chart',description = "Chart of stock")
async def chart(
    interaction: nextcord.Interaction,
    ticker: str = nextcord.SlashOption(
        required= True,
        description= "Enter Ticker of Stock",
    )
):
    global keywords
    keywords = ticker
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={config.api_key}'
    r = requests.get(url)
    data = r.json()
    await interaction.response.send_message(data['bestMatches'])
    print(data['bestMatches'])

bot.run(config.bot_token)
'''
#keywords = "btc"
def search(keywords: str):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={config.api_key}'
    r = requests.get(url)
    data = r.json()
    #print(data['bestMatches'])
    return (len(data['bestMatches']))

search("btc")