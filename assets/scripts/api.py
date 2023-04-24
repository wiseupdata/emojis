import requests

# Make a request to the GitHub API to get the emojis
response = requests.get('https://api.github.com/emojis')

# Get the emojis from the response
emojis = response.json()

# Loop through each emoji and create a Markdown string
markdown = ''
for emoji_name, emoji_url in emojis.items():
    markdown += f':{emoji_name}: `:{emoji_name}:`\n'

# Save the Markdown to a file
with open('emojis.md', 'w') as f:
    f.write(markdown)

