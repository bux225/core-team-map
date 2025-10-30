import csv
import json
from collections import defaultdict

# Read the CSV file
with open('cities.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Group people by city and time zone
city_groups = defaultdict(lambda: {
    'people': [], 
    'lat': None, 
    'lon': None, 
    'timezone': None, 
    'color': None,
    'city': None
})

for row in data:
    city_key = f"{row['City']},{row['Time Zone']}"
    city_groups[city_key]['people'].append({
        'name': row['Name'],
        'role': row['Role']
    })
    city_groups[city_key]['lat'] = float(row['Latitude'])
    city_groups[city_key]['lon'] = float(row['Longitude'])
    city_groups[city_key]['timezone'] = row['Time Zone']
    city_groups[city_key]['color'] = row['Color']
    city_groups[city_key]['city'] = row['City']

# Generate map data
map_data = []
legend_data = []

# Track which time zones we've seen for legend
seen_timezones = set()

for city_info in city_groups.values():
    # Create text for display (names separated by <br>)
    display_text = '<br>'.join([person['name'] for person in city_info['people']])
    
    # Create hover text (just role for each person)
    hover_lines = []
    for person in city_info['people']:
        hover_lines.append(person['role'])
    hover_text = '<br>'.join(hover_lines) + f"<br>{city_info['city']}"
    
    # Add main data point
    map_data.append({
        "lat": [city_info['lat']],
        "lon": [city_info['lon']],
        "locationmode": "USA-states",
        "marker": {
            "color": city_info['color'],
            "line": {
                "color": "black",
                "width": 1
            },
            "size": 10
        },
        "mode": "markers+text",
        "name": city_info['timezone'],
        "showlegend": False,
        "text": [display_text],
        "textposition": "bottom center",
        "textfont": {
            "size": 12,
            "color": "black"
        },
        "hovertext": [hover_text],
        "hovertemplate": "%{hovertext}<extra></extra>",
        "type": "scattergeo"
    })
    
    # Add legend entry if we haven't seen this timezone yet
    if city_info['timezone'] not in seen_timezones:
        legend_data.append({
            "lat": [None],
            "lon": [None],
            "marker": {
                "color": city_info['color'],
                "size": 10,
                "line": {
                    "color": "black",
                    "width": 1
                }
            },
            "mode": "markers",
            "name": city_info['timezone'],
            "type": "scattergeo",
            "showlegend": True
        })
        seen_timezones.add(city_info['timezone'])

# Combine all data
all_data = map_data + legend_data

# Create the complete map configuration
map_config = {
    "data": all_data,
    "layout": {
        "geo": {
            "scope": "usa",
            "projection": {
                "type": "albers usa"
            },
            "showland": True,
            "landcolor": "lightgray",
            "subunitcolor": "white",
            "countrycolor": "white",
            "showlakes": True,
            "lakecolor": "lightblue"
        },
        "legend": {
            "title": {
                "text": "Time Zones"
            }
        },
        "title": {
            "text": "Core Team Member Locations by Time Zone"
        },
        "margin": {
            "r": 0,
            "t": 50,
            "l": 0,
            "b": 0
        }
    }
}

# Save to a JSON file for reference
with open('generated_map_data.json', 'w') as f:
    json.dump(map_config, f, indent=2)

print("Generated map data from CSV!")
print(f"Found {len(city_groups)} unique city/timezone combinations")
print(f"Total team members: {len(data)}")