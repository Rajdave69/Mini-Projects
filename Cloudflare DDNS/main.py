"""
This is a public script made by RajDave69 on GitHub
This script implements DDNS (Dynamic DNS) for users using CloudFlare.
It's super easy to configure and deploy too! Just run it as a daemon.
"""

from cloudflare_ddns import CloudFlare
import time

email = ""    # Your cloudflare Email
api_key = ""  # Needs to be the "Global API Key" from https://dash.cloudflare.com/profile/api-tokens
domain = ""   # The domain you want DDNS to be for

cf = CloudFlare(email, api_key, domain)


def update_dns():
    try:
        print(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()), end=" | ")
        e = cf.sync_dns_from_my_ip()
        
    except Exception as e:
        print(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()), end=" | ")
        print(e)
    
print("Started")

while True:
    update_dns()
    time.sleep(300)

