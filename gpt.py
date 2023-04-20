import openai_secret_manager
import openai
import discord
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option

# Load secrets
secrets = openai_secret_manager.get_secret("discord")

# Connect to Discord
client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

# Connect to OpenAI
openai.api_key = secrets["openai_key"]

# Define command options
prompt_option = create_option(
    name="prompt",
    description="The prompt to start the conversation",
    option_type=3,
    required=True
)

# Define /gpt command
@slash.slash(name="gpt", description="Start a conversation with GPT-3", options=[prompt_option])
async def gpt(context: SlashContext, prompt: str):
    # Send typing status to user
    await context.send_typing()

    # Define conversation parameters
    engine = "davinci"
    temperature = 0.7
    max_tokens = 5000

    # Call OpenAI's GPT-3 API to generate response
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Send response to user
    await context.send(response.choices[0].text)

# Print output message when connected to Discord
@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("--------------------")

# Start the bot
if __name__ == "__main__":
    client.run(secrets["bot_token"])
