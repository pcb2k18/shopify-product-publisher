import datetime
import xmlrpc.client

# Set your WordPress credentials and URL
wordpress_url = 'https://ghanainsider.com/xmlrpc.php'
wordpress_username = 'Editorial Team'
wordpress_password = 'ntH*U3B9su4$Q0My'

# Connect to WordPress via XML-RPC
wp = xmlrpc.client.ServerProxy(wordpress_url)

# Get current date and time
current_datetime = datetime.datetime.now()

# Calculate the new modified date (1 week from now)
new_modified_datetime = current_datetime + datetime.timedelta(weeks=1)

# Format the new modified date in the required WordPress format
new_modified_date = new_modified_datetime.strftime('%Y%m%dT%H:%M:%S')

# Retrieve all articles from WordPress
articles = wp.wp.getPosts(0, wordpress_username, wordpress_password, {
    'post_type': 'post',
    'number': 100,  # Adjust the number as per your requirements
})

# Update the modified date for each article
for article in articles:
    article_id = article['post_id']
    result = wp.wp.editPost(article_id, wordpress_username, wordpress_password,
                            {'post_modified': new_modified_date, 'post_modified_gmt': new_modified_date})

    if result:
        print(f"Modified date updated for article with ID {article_id}.")
    else:
        print(f"Failed to update modified date for article with ID {article_id}.")
