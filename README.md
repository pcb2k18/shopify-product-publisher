# shopify-product-publisher
A Python script that automates the process of publishing products to a Shopify store. 
This script reads product data from a CSV file and uses Shopify's API to create and update product listings. Key features include:

Dynamic SEO Descriptions: Automatically generates SEO-friendly product descriptions based on product title and price.
Inventory Management: Sets a default inventory quantity and handles variant pricing and cost data.
Image Support: Uploads product images from CSV file URLs.
Automatic Product Publishing: Publishes products directly to your Shopify store with the ability to customize product titles and descriptions.
Features:

CSV Integration: Reads product information from a CSV file for bulk product management.
Customizable SEO: Constructs product descriptions dynamically to enhance search visibility.
Error Handling: Provides feedback on success or failure of product publishing.

Setup Instructions:
Install Dependencies: Ensure you have the required Python libraries installed:

pip install pandas requests

Update Credentials:

Replace SHOPIFY_STORE_NAME with your Shopify store name.
Replace ACCESS_TOKEN with your Shopify API access token.
Update API_VERSION to your desired Shopify API version.
Prepare CSV File: Ensure your CSV file includes columns for product details such as Title, Variant Price, Image Src, etc.

Run the Script: Execute the script to publish products to your Shopify store.
