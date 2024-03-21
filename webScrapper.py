import requests
import csv

url = "https://moviesdatabase.p.rapidapi.com/titles"

headers = {
    "X-RapidAPI-Key": "371e846c56mshe17c5f46b6a72c9p1eb3cbjsne8f25cbae976",
    "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}

# Send a GET request to the API endpoint
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Extract JSON data from the response
    series_data = response.json()
    
    # Specify the file path
    file_path = "series_data.csv"
    
    # Open the CSV file in write mode
    with open(file_path, mode='w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['Series ID', 'Title', 'Genre', 'Rating'])
        
        # Process and write the data to the CSV file
        for series in series_data.get('results', []):
            series_id = series.get('id')
            series_title = series.get('titleText', {}).get('text')
            series_genre = series.get('titleType', {}).get('text')
            series_rating = series.get('rating')
            
            # Write the row to the CSV file
            writer.writerow([series_id, series_title, series_genre, series_rating])
    
    print(f"Data has been successfully written to {file_path}")
else:
    print("Failed to fetch data from the API")
