import urllib.request
import xml.etree.ElementTree as ET
import datetime

# 1. The News Source (RSS Feed URL)
url = 'http://feeds.bbci.co.uk/news/world/rss.xml'

# 2. Fetch the data
response = urllib.request.urlopen(url)
rss_data = response.read()
root = ET.fromstring(rss_data)
items = root.findall('./channel/item')

# 3. Write the HTML website design
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Automated Daily News</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: auto; padding: 20px; background-color: #f4f4f9; }}
        h1 {{ color: #333; text-align: center; }}
        .news-item {{ background: white; padding: 15px; margin-bottom: 10px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        .news-item a {{ text-decoration: none; color: #0066cc; font-size: 1.2em; font-weight: bold; }}
        .news-item a:hover {{ text-decoration: underline; }}
        .footer {{ text-align: center; margin-top: 30px; font-size: 0.9em; color: #777; }}
    </style>
</head>
<body>
    <h1>🌍 Daily World News</h1>
"""

# 4. Loop through the top 15 news articles and add them to the website
for item in items[:15]:
    title = item.find('title').text
    link = item.find('link').text
    description = item.find('description').text
    
    html_content += f"""
    <div class="news-item">
        <a href="{link}" target="_blank">{title}</a>
        <p>{description}</p>
    </div>
    """

# 5. Finish the HTML and stamp it with the current time
html_content += f"""
    <div class="footer">
        <p>This page is automatically generated.<br>Last updated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </div>
</body>
</html>
"""

# 6. Save this as the index.html file
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
    
print("Successfully generated index.html with the latest news!")
