import requests

# Make a request to the GitHub API to get the emojis
response = requests.get('https://api.github.com/emojis')

# Get the emojis from the response
emojis = response.json()

# Create a Markdown table header
markdown = '| Emoji Name | Emoji Code |\n| --- | --- |\n'

# Loop through each emoji and add it to the Markdown table
for emoji_name, emoji_url in emojis.items():
    markdown += f'| :{emoji_name}: | `:{emoji_name}:` |\n'

# Save the Markdown to a file
with open('emojis.md', 'w') as f:
    f.write(markdown)
