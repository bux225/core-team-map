# Core Team Map Generator

This project automatically generates an interactive map of core team member locations from a CSV file.

## Files Overview

- `cities.csv` - Source data with team member information.  MUST HAVE unique lat/lon's.  Jitter folks living in same city
- `generate_map_data.py` - Python script to process CSV and generate JSON data
- `update_html.py` - Python script to update the HTML file with new data
- `team-map-from-csv.html` - Final interactive map (self-contained HTML file)
- `generated_map_data.json` - Intermediate JSON data file

## How to Update the Map

When the team roster changes, follow these simple steps:

### Step 1: Update the CSV File

Edit `cities.csv` with your changes. The CSV format is:

```csv
Name,Role,City,Latitude,Longitude,Time Zone,Color
Matt Soltis,Core Team Lead,"Broomfield, CO",39.92,-105.086,MST,green
Meghan Batt,Program Manager,"Cincinnati, OH",39.103,-84.512,EST,red
...
```

**CSV Column Details:**
- **Name**: Team member's full name
- **Role**: Their job title/role
- **City**: City and state (use quotes if it contains commas)
- **Latitude**: Decimal latitude coordinates
- **Longitude**: Decimal longitude coordinates  
- **Time Zone**: PST, MST, CST, or EST
- **Color**: blue (PST), green (MST), orange (CST), or red (EST)

**Common Changes:**
- **Add new person**: Add a new row with their information
- **Remove person**: Delete their row
- **Change role**: Update the Role column
- **Relocate person**: Update City, Latitude, Longitude, Time Zone, and Color columns

### Step 2: Regenerate the Map Data

Run the Python script to process your CSV changes:

```bash
python3 generate_map_data.py
```

This will:
- Read your updated `cities.csv`
- Group people by city and time zone
- Handle multiple people in the same city (with `<br>` separation)
- Generate `generated_map_data.json` with the plot data

### Step 3: Update the HTML File

Run the update script to embed the new data into your HTML file:

```bash
python3 update_html.py
```

This will:
- Read the generated JSON data
- Update `team-map-from-csv.html` with the new information
- Preserve all the styling and functionality

### Step 4: View Your Updated Map

Open `team-map-from-csv.html` in your browser or serve it locally:

```bash
python3 -m http.server 8002
```

Then visit `http://localhost:8002/team-map-from-csv.html`

## Map Features

The generated map includes:

- **Interactive markers** for each city with team members
- **Names displayed below markers** for easy identification
- **Hover tooltips** showing roles and city (no coordinates)
- **Time zone legend** with color coding
- **Grouped locations** - Multiple people in the same city show as stacked names
- **Download buttons** for PNG and PDF export
- **No lat/lon clutter** in hover text

## Time Zone Colors

- **PST (Pacific)**: Blue
- **MST (Mountain)**: Green  
- **CST (Central)**: Orange
- **EST (Eastern)**: Red

## Finding Coordinates

If you need to add a new city, you can find coordinates using:
- [LatLong.net](https://www.latlong.net/)
- [GPS Coordinates](https://gps-coordinates.org/)
- Google Maps (right-click → "What's here?")

## Troubleshooting

**CSV encoding issues**: The script handles UTF-8 BOM encoding automatically.

**Missing columns**: Ensure your CSV has exactly these headers:
`Name,Role,City,Latitude,Longitude,Time Zone,Color`

**Multiple people, same city**: The script automatically groups them and uses `<br>` to separate names in the display.

**Script errors**: Make sure you're in the correct directory and have Python 3 installed.

## Example Workflow

1. **Sarah joins the team in Austin, TX (CST)**
   - Add row: `Sarah Wilson,UX Designer,"Austin, TX",30.267,-97.743,CST,orange`

2. **Run the update**:
   ```bash
   python3 generate_map_data.py
   python3 update_html.py
   ```

3. **Done!** Sarah now appears on the map with the CST (orange) color.

## Confluence Integration

The `team-map-from-csv.html` file is self-contained and can be:
- Embedded using Confluence's HTML macro
- Uploaded as an attachment for viewing
- Used to generate PNG/PDF exports for static inclusion

---

*Last updated: October 29, 2025*