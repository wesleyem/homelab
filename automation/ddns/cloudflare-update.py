import requests
import time
from cloudflare import Cloudflare
import os

# Configuration from environment variables
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
API_EMAIL = os.getenv("CLOUDFLARE_API_EMAIL")
ZONE_ID = os.getenv("ZONE_ID")
DNS_RECORD_ID = os.getenv("DNS_RECORD_ID")
CHECK_INTERVAL = 300  # This interval is unused when run in GitHub Actions


def get_public_ip():
    """Fetch the public IP address."""
    try:
        response = requests.get("https://api.ipify.org", timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None

def update_cloudflare_record(cf, ip):
    """Update the Cloudflare DNS record."""
    try:
        # Fetch the current DNS record details
        dns_record = cf.zones.dns_records.get(ZONE_ID, DNS_RECORD_ID)
        current_ip = dns_record["content"]

        # Check if the IP needs to be updated
        if current_ip == ip:
            print(f"IP address is already up-to-date: {ip}")
            return

        # Update the DNS record
        dns_record["content"] = ip
        cf.zones.dns_records.put(ZONE_ID, DNS_RECORD_ID, data=dns_record)
        print(f"Updated Cloudflare DNS record to IP: {ip}")
    except Exception as e:
        print(f"Error updating Cloudflare DNS record: {e}")

def main():
    """Monitor IP changes and update Cloudflare."""
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
