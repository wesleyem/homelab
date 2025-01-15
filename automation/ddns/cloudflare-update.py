import sys
import requests
import time
from cloudflare import Cloudflare
import os

# Configuration from environment variables
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
API_EMAIL = os.getenv("CLOUDFLARE_API_EMAIL")
ZONE_ID = os.getenv("ZONE_ID")
DNS_RECORD_ID = os.getenv("DNS_RECORD_ID")

def get_public_ip():
    """Fetch the public IP address."""
    try:
        response = requests.get("https://api.ipify.org", timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        sys.exit(1)

def update_cloudflare_record(cf, ip):
    """Edit the Cloudflare DNS record."""
    try:
        # Edit the DNS record
        cf.dns.records.edit(dns_record_id=DNS_RECORD_ID, zone_id=ZONE_ID, content=ip)
        print(f"Edited Cloudflare DNS record to IP: {ip}")
    except Exception as e:
        print(f"Error editing Cloudflare DNS record: {e}")
        sys.exit(1)

def main():
    """Monitor IP changes and edit Cloudflare."""
    cf = Cloudflare(
        api_email=API_EMAIL,
        api_key=API_TOKEN
        )
    current_ip = get_public_ip()

    if current_ip:
        print(f"Detected IP: {current_ip}")
        update_cloudflare_record(cf, current_ip)

if __name__ == "__main__":
    main()
