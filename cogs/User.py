import discord
from discord.ext import commands
from discord import app_commands
from database.user import UserManager

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_manager = UserManager() 

    @app_commands.command(name="start_user", description="Start user setup")
    async def start_user(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)  
        
        await interaction.response.send_message("Your account is being created. Please wait.")

        user_created = await self.user_manager.create_user(user_id, interaction.user.name)
        
        if user_created:
            print(user_created)
            await interaction.channel.send(f"User {interaction.user.name} created successfully!")
        else:
            await interaction.channel.send("Failed to create user.")
    
    @app_commands.command(name="view", description="View user details")
    async def view(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)  

        await interaction.response.send_message("Your account is being grabbed. Please wait.")

        print("calling get user")
        user = await self.user_manager.get_user(user_id)
        print(user)
        
        if user:
            await interaction.channel.send(f"{user.name} has a streak of {user.streak}")
        else:
            await interaction.channel.send("User not found.")

async def setup(bot):
    await bot.add_cog(User(bot))
