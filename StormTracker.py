import requests
import json

# Base URL for the NWS API related to tropical cyclones
TROPICAL_STORM_URL = "https://api.weather.gov/products/types/TCM/locations/AL"

# Function to get data from NWS API
def get_active_storms():
    response = requests.get(TROPICAL_STORM_URL)
    if response.status_code == 200:
        data = response.json()
        return data['@graph']  # Return the list of storms
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

# Extract storm details
def parse_storm_data(storm):
    title = storm.get('title', 'Unknown Storm')
    issuance_time = storm.get('issuanceTime', 'N/A')
    location = storm.get('location', 'N/A')
    forecast = storm.get('productText', 'N/A')
    
    print(f"Storm Name: {title}")
    print(f"Issuance Time: {issuance_time}")
    print(f"Location: {location}")
    
    # Extract forecast details from the product text
    # Depending on the format of the forecast text, you can refine this part to get more precise data
    print(f"Forecast: {forecast[:500]}...")  # Display first 500 characters of the forecast
    print("=" * 50)

# Main function to display active tropical cyclones
def display_active_storms():
    print("Fetching active tropical storms, hurricanes, and typhoons...\n")
    
    storms = get_active_storms()
    
    if not storms:
        print("No active storms found.")
        return
    
    for storm in storms:
        parse_storm_data(storm)

# Run the program
if __name__ == "__main__":
    display_active_storms()
