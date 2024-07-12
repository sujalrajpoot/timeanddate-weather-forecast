import requests
from bs4 import BeautifulSoup
import re

class TimeandDate:
    """A class to extract weather data from a given URL from timeanddate.com website.\n\nExample: https://www.timeanddate.com/weather/uk/london
    \nOutput: {'temperature': '15 °C', 'visibility': 'N/A', 'pressure': '1005 mbar', 'humidity': '82%', 'dew_point': '12 °C', 'feels_like': '14 °C', 'forecast': '19 °C to 13 °C', 'wind': '17 km/h from West'}"""
    
    def extract_weather_data(url: str):
        """
        Extracts weather data from the specified URL.

        Args:
            url (str): The URL of the weather page to extract data from.

        Returns:
            dict: A dictionary containing weather data such as temperature, visibility, pressure, humidity, dew point, feels like temperature, forecast, and wind information. Returns None if there is an error.
        """
        try:
            # Send a GET request to the URL
            response = requests.get(url, timeout=None)
            # Raise an exception if the request was not successful
            response.raise_for_status()
        except requests.RequestException as e:
            # Print an error message if there was an issue with the request
            print(f"Error fetching the URL: {e}")
            return None

        try:
            # Parse the HTML content of the response
            soup = BeautifulSoup(response.content, 'html.parser')
            
            def clean_text(text):
                """Utility function to clean text by removing non-breaking spaces."""
                return text.replace('\xa0', ' ').strip()

            # Find and clean the temperature text
            temperature_tag = soup.find(class_='h2')
            temperature = clean_text(temperature_tag.text) if temperature_tag else 'N/A'
            
            # Find and clean the wind info text
            wind_info_tag = soup.find('p').find_next_sibling('p')
            wind_info = clean_text(str(wind_info_tag.text).replace('CF', 'C, F').replace('CW', 'C, W').replace(' / ', ' °C to ').replace('↑ ', '')) if wind_info_tag else 'N/A'
            
            # Extract specific information from the wind info text using regular expressions
            feels_like_match = re.search(r'Feels Like:\s*([^,]+)', wind_info)
            forecast_match = re.search(r'Forecast:\s*([^,]+)', wind_info)
            wind_match = re.search(r'Wind:\s*([^,]+)', wind_info)
            
            feels_like = clean_text(feels_like_match.group(1)) if feels_like_match else 'N/A'
            forecast = clean_text(forecast_match.group(1)) if forecast_match else 'N/A'
            wind = clean_text(wind_match.group(1)) if wind_match else 'N/A'
            
            # Find the info table and extract the necessary rows
            info_table = soup.find('table', class_='table--left')
            rows = info_table.find_all('tr') if info_table else []
            
            # Extract and clean specific data from the table rows
            visibility = clean_text(rows[3].find('td').text) if len(rows) > 3 else 'N/A'
            pressure = clean_text(rows[4].find('td').text) if len(rows) > 4 else 'N/A'
            humidity = clean_text(rows[5].find('td').text) if len(rows) > 5 else 'N/A'
            dew_point = clean_text(rows[6].find('td').text) if len(rows) > 6 else 'N/A'
            
            # Create a dictionary to store the extracted weather data
            weather_data = {
                'temperature': temperature,
                'visibility': visibility,
                'pressure': pressure,
                'humidity': humidity,
                'dew_point': dew_point,
                'feels_like': feels_like,
                'forecast': forecast,
                'wind': wind
            }
            
            return weather_data
        except Exception as e:
            # Print an error message if there was an issue processing the data
            print(f"Error processing the data: {e}")
            return None
        
if __name__=='__main__':
    print(TimeandDate.extract_weather_data(url='https://www.timeanddate.com/weather/uk/london'))
