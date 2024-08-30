import pandas as pd
import requests
import json

# Shopify API credentials and endpoint
SHOPIFY_STORE_NAME = ''  # Replace with your store name
ACCESS_TOKEN = ''  # Replace with your access token
API_VERSION = ''  # Replace with your Shopify API version
API_ENDPOINT = f'https://{SHOPIFY_STORE_NAME}.myshopify.com/admin/api/{API_VERSION}/products.json'

# Read CSV file
csv_file_path = r''  # Path to your CSV file
df = pd.read_csv(csv_file_path)

# Function to construct dynamic SEO description
def get_dynamic_seo_description(title, price):
    return f"{title}✓ 17 in stock for sale in Ghana ❤ Price starting from ➔ GH₵ {price} ➔ Shop and buy today!"

# Function to publish product to Shopify
def publish_product(product):
    # Check if product should be published, defaulting to True if not specified
    published = 'TRUE'

    # Handle NaN values and convert them to default values
    variant_price = str(product.get("Variant Price", 0)).strip()

    # Set inventory_quantity to 17
    inventory_quantity = 17

    # Get the original title and append "For Sale"
    original_title = str(product.get("Title", "")).strip()
    title_with_suffix = f"{original_title} For Sale"

    # Construct the dynamic SEO description
    seo_description = get_dynamic_seo_description(
        title_with_suffix,
        variant_price
    )

    # Extract image URL from CSV
    image_src = str(product.get("Image Src", "")).strip()

    # Construct the product data payload
    product_data = {
        "product": {
            "title": title_with_suffix,  # Updated title with "For Sale"
            "body_html": str(product.get("Body (HTML)", "")).strip(),
            "variants": [
                {
                    "price": variant_price,
                    "grams": int(product.get("Variant Grams", 0)),
                    "cost": str(product.get("Cost per item", 0)).strip(),
                    "inventory_management": "shopify",
                    "inventory_quantity": inventory_quantity  # Set to 17
                }
            ],
            "images": [
                {
                    "src": image_src  # Adding image URL from CSV to product data
                }
            ],
            "published": published,
            "metafields_global_description_tag": seo_description  # Dynamic SEO Description
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': ACCESS_TOKEN,
    }

    # Send request to Shopify API
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(product_data))

    # Handle the response
    if response.status_code == 201:
        print(f"Product '{title_with_suffix}' published successfully.")
    else:
        print(f"Failed to publish product '{title_with_suffix}': {response.status_code} - {response.text}")

# Iterate over rows in DataFrame and publish each product
for index, row in df.iterrows():
    publish_product(row)
