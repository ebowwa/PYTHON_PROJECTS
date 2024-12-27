import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Shopify API credentials
SHOP_NAME = os.getenv('SHOP_NAME')
API_KEY = os.getenv('SHOPIFY_API_KEY')
PASSWORD = os.getenv('SHOPIFY_PASSWORD')
API_VERSION = '2024-07'  # Use the latest stable version as of September 2024

# Shopify API URL
SHOP_URL = f"https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin"