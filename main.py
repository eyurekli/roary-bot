from discord import Intents, Client
import responses
import os
from dotenv import load_dotenv

load_dotenv()

def run_bot(token: str):
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    knowledge: dict = responses.load_knowledge('knowledge.json')

    #Async function that triggers on bot running
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    #Async function that triggers on a message being sent
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content.startswith('!roar'):
            print(f'({message.channel})) {message.author}: "{message.content}"')
            response: str = responses.get_response(message.content[5:], knowledge=knowledge)  # Strip the "!" before processing
            await message.channel.send(response)
        else:
            print('Message did not start with "!" and was ignored.')

    
    client.run(token=token)

if __name__ == '__main__':
    token = os.getenv('DISCORD_BOT_TOKEN')  # Get the token from environment variables
    run_bot(token=token)