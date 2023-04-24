import requests

# Make a request to the GitHub API to get the emojis
response = requests.get('https://api.github.com/emojis')

# Get the emojis from the response
emojis = response.json()

COLS = 3

# Create a list of emoji and code pairs
pairs = [f':{name}: `:{name}:`' for name in emojis.keys()]

# Group the pairs into sets
chunks = [pairs[i:i+COLS] for i in range(0, len(pairs), COLS)]

# Convert the sets to rows in a Markdown table
rows = [f'| {" | ".join(chunk)} |' for chunk in chunks]

row_join = '\n'.join(rows)

# Create the header row
header = '| ' + ' | '.join(['Emoji', 'Code'] * COLS) + ' |' + '\n| ' + ' | '.join(['---', '---'] * COLS) + ' |'

# Create the markdown
markdown = header + f"\n{row_join}"

# Save the Markdown to a file
with open('emojis.md', 'w') as f:
    f.write(markdown)
