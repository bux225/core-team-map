import json
import re

# Read the generated JSON data
with open('generated_map_data.json', 'r') as f:
    map_data = json.load(f)

# Read the current HTML file
with open('team-map-from-csv.html', 'r') as f:
    html_content = f.read()

# Convert the JSON to a JavaScript object string
js_data = json.dumps(map_data, indent=2)

# Replace the mapData object in the HTML
pattern = r'const mapData = \{.*?\};'
replacement = f'const mapData = {js_data};'

# Use DOTALL flag to match across newlines
updated_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

# Write the updated HTML file
with open('team-map-from-csv.html', 'w') as f:
    f.write(updated_html)

print("Updated team-map-from-csv.html with new hover text!")