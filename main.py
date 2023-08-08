import discord
from discord.ext import commands
import random
import json


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!')

TOKEN = "BOT_TOKEN"


# Load quotes from JSON file
def load_quotes():
    try:
        with open('quotes.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save quotes to thing JSON file
def save_quotes(quotes):
    with open('quotes.json', 'w') as file:
        json.dump(quotes, file, indent=4)

quote_list = load_quotes()
# logs the quotes
@bot.command(name='quote')
async def quote(ctx, *, quote_text):
    author = ctx.author.display_name
    new_quote = {"content": quote_text, "author": author}
    quote_list.append(new_quote)
    save_quotes(quote_list)
    await ctx.send(f'Quote added: "{quote_text}" - {author}')

@bot.command(name='randomquote', aliases=['rq'])
async def randomquote(ctx):
    if quote_list:
        random_quote = random.choice(quote_list)
        quote_text = random_quote.get("content", "No quote text available")
        author_name = random_quote.get("author", "Unknown Author")

        quote_message = f'"{quote_text}" - {author_name}'
        await ctx.send(quote_message)

bot.run('TOKEN')
