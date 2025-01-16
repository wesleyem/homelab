import sys
import requests
import time
from cloudflare import Cloudflare
import os

# Configuration from environment variables
CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
CLOUDFLARE_API_EMAIL = os.getenv("CLOUDFLARE_API_EMAIL")
CLOUDFLARE_ZONE_ID = os.getenv("CLOUDFLARE_ZONE_ID")
CLOUDFLARE_DNS_RECORD_ID = os.getenv("CLOUDFLARE_DNS_RECORD_ID")

def get_public_ip():
    """Fetch the public IP address."""
    try:
        response = requests.get("https://api.ipify.org", timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        sys.exit(1)

def update_cloudflare_record(ip):
    """Monitor IP changes and edit Cloudflare."""
    client = Cloudflare(
        api_key=CLOUDFLARE_API_TOKEN
    )
    """Edit the Cloudflare DNS record."""
    try:
        # Edit the DNS record
        client.dns.records.edit(dns_record_id=CLOUDFLARE_DNS_RECORD_ID, zone_id=CLOUDFLARE_ZONE_ID, content=ip)
        print(f"Edited Cloudflare DNS record to IP: {ip}")
    except Exception as e:
        print(f"Error editing Cloudflare DNS record: {e}")
        sys.exit(1)

def main():
    current_ip = get_public_ip()

    if current_ip:
        print(f"Detected IP: {current_ip}")
        update_cloudflare_record(current_ip)

if __name__ == "__main__":
    main()
