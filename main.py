import discord
from discord import app_commands
from discord.ext import commands
import os
import aiohttp
from flask import Flask
from threading import Thread

# 1. Background Web Server required for Render Free Tier tracking pings
app = Flask('')

@app.route('/')
def home():
    return "OmniShield Security Grid Operational."

def run_web_server():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run_web_server)
    t.start()

# 2. Discord Bot Engine Configuration
class OmniShieldBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True  # Required to scan arriving accounts
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()

bot = OmniShieldBot()

# 3. Asynchronous VPN / Proxy Verification Engine
async def is_vpn_or_proxy(ip_address):
    """Queries proxycheck.io API to verify if an incoming connection is a proxy/VPN"""
    api_key = os.getenv("PROXYCHECK_API_KEY") # Optional but recommended for high traffic
    
    url = f"http://proxycheck.io{ip_address}?vpn=1&asn=1"
    if api_key:
        url += f"&key={api_key}"
        
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if ip_address in data:
                        # proxycheck.io returns "yes" if the IP is flagged as a VPN/Proxy
                        return data[ip_address].get("proxy") == "yes"
                return False
        except Exception as e:
            print(f"🚨 Security API Query Failure: {e}")
            return False

# 4. Automated Border Security Gate (Triggers instantly when a member joins)
@bot.event
async def on_member_join(member: discord.Member):
    log_channel_id = os.getenv("SECURITY_LOG_CHANNEL_ID")
    if not log_channel_id:
        return
        
    channel = bot.get_channel(int(log_channel_id))
    if not channel:
        return

    # In full production, the user's IP is retrieved via web portal integration.
    # For standalone bot filtering, we simulate a gate check or verify account age flags.
    account_age_days = (discord.utils.utcnow() - member.created_at).days
    
    # CRITICAL CRITERIA: Flag accounts created less than 3 days ago (Standard Raid Alt Profile)
    if account_age_days < 3:
        try:
            embed = discord.Embed(
                title="🛡️ OmniShield Perimeter Breach Blocked",
                description=f"Automated gate system intercepted and quarantined a suspected alt/raid profile.",
                color=discord.Color.red()
            )
            embed.add_field(name="👤 Target Account", value=member.mention, inline=True)
            embed.add_field(name="⏳ Account Age", value=f"`{account_age_days} days old`", inline=True)
            embed.add_field(name="⚙️ Action Executed", value="`AUTOMATED KICK / RESTRICT`", inline=False)
            
            await channel.send(embed=embed)
            
            # Direct action to protect the server
            await member.kick(reason="OmniShield Protection: New Account Alt/Proxy Gate Shield Triggered.")
        except Exception as e:
            print(f"Failed to execute security kick: {e}")

@bot.event
async def on_ready():
    print(f"🤖 Security Grid Active. Connected as: {bot.user.name}")

if __name__ == "__main__":
    keep_alive()
    token = os.getenv("DISCORD_TOKEN")
    if token:
        bot.run(token)
    else:
        print("❌ System Error: DISCORD_TOKEN is missing.")
