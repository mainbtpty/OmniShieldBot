
OMNISHIELD ANTI-ALT & PROXY GATEKEEPER - TECHNICAL DEPLOYMENT GUIDE


OmniShield is an enterprise-grade perimeter border protection system 
designed to secure high-traffic Discord servers and monetized gaming 
networks from raid bots, proxy bypass accounts, and malicious alt users.

ENVIRONMENTAL WORKSPACE CONFIGURATION VARIABLES REQUIRED:
-------------------------------------------------------------------
1. DISCORD_TOKEN
   - Your premium Discord application bot authentication string.
   
2. SECURITY_LOG_CHANNEL_ID
   - The exact numerical ID of the private staff log channel where 
     OmniShield will transmit real-time perimeter breach alerts.
     
3. PROXYCHECK_API_KEY (Optional)
   - Your custom API access token generated from proxycheck.io. 
     Leave blank to operate under proxycheck's free daily tiers.

PLATFORM DEPENDENCY MANAGEMENT:
-------------------------------------------------------------------
- Script core executes on Python 3.11 or higher.
- System dependencies map directly to standard open-source nodes:
  * discord.py (https://pypi.org)
  * Flask (https://pypi.org)
  * aiohttp (https://pypi.org)

DEPLOYMENT PIPELINE LAUNCH INSTRUCTIONS:
-------------------------------------------------------------------
1. Navigate to your Discord Developer Portal application settings.
2. Open the 'Bot' tab and ensure all 3 Privileged Gateway Intents 
   (Presence, Server Members, Message Content) are toggled ON (Green).
3. Execute 'pip install -r requirements.txt' on your network panel node.
4. Execute 'python main.py' to active the border security firewall array.

===================================================================
                     DEVELOPED BY ONITECHZ SECURITY
===================================================================
