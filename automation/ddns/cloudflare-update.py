import sys
import requests
from cloudflare import Cloudflare
import os
from dotenv import load_dotenv



def get_public_ip():
    """Fetch the public IP address."""
    try:
        response = requests.get("https://api.ipify.org", timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        sys.exit(1)

def update_cloudflare_record(ip, api_token, zone_id, dns_record_id):
    """Monitor IP changes and edit Cloudflare."""
    client = Cloudflare(
        api_token=api_token
    )
    """Edit the Cloudflare DNS record."""
    try:
        # Edit the DNS record
        response = client.dns.records.edit(
            dns_record_id=dns_record_id,
            zone_id=zone_id,
            content=ip
        )
        print(f"Successfully updated DNS record to IP")
    except Exception as e:
        print(f"Error editing Cloudflare DNS record: {e}")
        sys.exit(1)

def main():
    # Check for a flag to determine how to load environment variables
    if len(sys.argv) > 1 and sys.argv[1] == "--use-env-file":
        print("Loading environment variables from .env file...")
        load_dotenv()

    # Configuration from environment variables
    CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
    CLOUDFLARE_API_EMAIL = os.getenv("CLOUDFLARE_API_EMAIL")
    CLOUDFLARE_ZONE_ID = os.getenv("CLOUDFLARE_ZONE_ID")
    CLOUDFLARE_DNS_RECORD_ID = os.getenv("CLOUDFLARE_DNS_RECORD_ID")

    if not CLOUDFLARE_API_TOKEN or not CLOUDFLARE_ZONE_ID or not CLOUDFLARE_DNS_RECORD_ID:
        print("Missing required environment variables.")
        sys.exit(1)

    # Fetch the current public IP address
    current_ip = get_public_ip()

    if current_ip:
        print(f"Detected IP")
        # Update the Cloudflare DNS record
        update_cloudflare_record(
            current_ip,
            CLOUDFLARE_API_TOKEN,
            CLOUDFLARE_ZONE_ID,
            CLOUDFLARE_DNS_RECORD_ID
        )

if __name__ == "__main__":
    main()
