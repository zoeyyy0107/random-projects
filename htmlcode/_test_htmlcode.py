import html
from urllib.parse import *
# Create Text
text = 'B&#x27;CUZ SNACKS'
# text = 'Chloe & Lola'
encodedStr  = '/b/Est%26%23233%3Be+Lauder'
encodedStr = '/b/Giorgio+Armani'
  
# It Converts given text To String
print(html.unescape(text)) 
  
# It Converts given text to HTML Entities 
print(html.escape(text)) 

print(f"https://www.myer.com.au/b/{quote(html.unescape(text))}")

print(f"https://www.myer.com.au/b/{quote((text))}")