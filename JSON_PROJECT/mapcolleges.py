import json
import time
from geopy.geocoders import Nominatim
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

def split_address(address, max_line_length=50):
    words = address.split(' ')
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return '<br>'.join(lines)

infile = open('univ.json', 'r')
univ_data = json.load(infile)
infile.close()

infile = open('schools.geojson', 'r')
geo_data = json.load(infile)
infile.close()

geolocator = Nominatim(user_agent="big12_locator")

lons, lats, hover_texts, sizes, colors = [],[], [], [], []

BIG12_CONFERENCE_CODE = 108

print("PROCESSING BIG 12 CONFERENCE SCHOOLS")
print("=" * 50)

big12_schools_found = []

for school in univ_data:
    if 'NCAA' in school:
        ncaa_data = school['NCAA']
        conference_code = ncaa_data.get('NAIA conference number football (IC2020)')
        
        if conference_code == BIG12_CONFERENCE_CODE:
            name = school['instnm']
            big12_schools_found.append(name)
            
            lon = school['Longitude location of institution (HD2020)']
            lat = school['Latitude location of institution (HD2020)']
            
            total_enrollment = school.get('Total  enrollment (DRVEF2020)', 0)
            percent_women = school.get('Percent of total enrollment that are women (DRVEF2020)', 0)
            
            if isinstance(total_enrollment, int) and isinstance(percent_women, (int, float)):
                female_students = int(total_enrollment * percent_women / 100)
                male_students = total_enrollment - female_students
            else:
                female_students = "Unknown"
                male_students = "Unknown"
            
            try:
                location = geolocator.reverse((lat, lon), language='en')
                address = location.address
                print(f"✓ Found: {name}")
            except Exception as e:
                address = "Address Not Found"
                print(f"✓ Found: {name} (geocoding failed)")
            
            time.sleep(1)
            
            formatted_address = split_address(address)
            
            hover_text = (
                f"{name}<br>"
                f"{formatted_address}<br>"
                f"Total Enrollment: {total_enrollment:,}<br>"
                f"Male: {male_students:,}<br>"
                f"Female: {female_students:,}"
            )
            
            if isinstance(total_enrollment, int) and total_enrollment > 0:
                size = max(8, min(20, total_enrollment / 2000))
            else:
                size = 10
            
            lons.append(lon)
            lats.append(lat)
            hover_texts.append(hover_text)
            sizes.append(size)
            colors.append(total_enrollment if isinstance(total_enrollment, int) else 1000)

print("\n" + "=" * 50)
print(f"TOTAL BIG 12 SCHOOLS FOUND: {len(big12_schools_found)}")
print("=" * 50)

for school in big12_schools_found:
    print(f"• {school}")

if len(lons) > 0:
    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'mode': 'markers',
        'marker': {
            'size': sizes,
            'color': colors,
            'colorscale': 'Rainbow',
            'colorbar': {'title': 'Enrollment Size'},
            'line': {'width': 0.5, 'color': 'black'}
        },
        'hoverinfo': 'text'
    }]

    my_layout = Layout(
        title='Big 12 Conference Schools Map - Dynamic NCAA Filtering',
        geo={
            'scope': 'usa',
            'projection': {'type': 'albers usa'},
            'showland': True,
            'landcolor': 'rgb(217, 217, 217)'
        }
    )

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='big12_schools_map.html')

    print(f"\n✅ Map created successfully!")
    print(f"📍 Total Big 12 schools mapped: {len(lons)}")
    print(f"📄 Output file: big12_schools_map.html")
    
    if len(lons) > 0:
        print(f"📊 Enrollment range: {min(colors):,} to {max(colors):,} students")
else:
    print("❌ No Big 12 schools found with NCAA conference code 108")
    print("Check if the data structure or conference code is correct.")