import requests
from bs4 import BeautifulSoup
import re

class TimeandDate:
    """
    A class to extract weather data from a given URL from the timeanddate.com website using requests.Session.

    Example:
    weather = TimeandDate('https://www.timeanddate.com/weather/uk/london')
    print(weather.temperature)
    print(weather.feels_like)
    """

    def __init__(self, url: str):
        """
        Initialize the class by extracting weather data from the given URL.

        Args:
            url (str): The URL of the weather page to extract data from.
        """
        self.url = url
        self.temperature = None
        self.visibility = None
        self.pressure = None
        self.humidity = None
        self.dew_point = None
        self.feels_like = None
        self.forecast = None
        self.wind = None

        # Extract weather data and assign it to the instance attributes
        self.extract_weather_data()

    def extract_weather_data(self):
        """
        Extracts weather data from the specified URL and assigns values to instance attributes using requests.Session.
        """
        session = requests.Session()
        
        try:
            # Send a GET request using the session
            response = session.get(self.url, timeout=None)
            # Raise an exception if the request was not successful
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching the URL: {e}")
            session.cookies.clear()  # Clear cookies after an error
            return

        try:
            # Parse the HTML content of the response
            soup = BeautifulSoup(response.content, 'html.parser')

            def clean_text(text):
                """Utility function to clean text by removing non-breaking spaces."""
                return text.replace('\xa0', ' ').strip()

            # Find and clean the temperature text
            temperature_tag = soup.find(class_='h2')
            self.temperature = clean_text(temperature_tag.text) if temperature_tag else None

            # Find and clean the wind info text
            wind_info_tag = soup.find('p').find_next_sibling('p')
            wind_info = clean_text(str(wind_info_tag.text).replace('CF', 'C, F').replace('CW', 'C, W').replace(' / ', ' °C to ').replace('↑ ', '')) if wind_info_tag else None

            # Extract specific information from the wind info text using regular expressions
            feels_like_match = re.search(r'Feels Like:\s*([^,]+)', wind_info)
            forecast_match = re.search(r'Forecast:\s*([^,]+)', wind_info)
            wind_match = re.search(r'Wind:\s*([^,]+)', wind_info)

            self.feels_like = clean_text(feels_like_match.group(1)) if feels_like_match else None
            self.forecast = clean_text(forecast_match.group(1)) if forecast_match else None
            self.wind = clean_text(wind_match.group(1)) if wind_match else None

            # Find the info table and extract the necessary rows
            info_table = soup.find('table', class_='table--left')
            rows = info_table.find_all('tr') if info_table else []

            # Extract and clean specific data from the table rows
            self.visibility = clean_text(rows[3].find('td').text) if len(rows) > 3 else None
            self.pressure = clean_text(rows[4].find('td').text) if len(rows) > 4 else None
            self.humidity = clean_text(rows[5].find('td').text) if len(rows) > 5 else None
            self.dew_point = clean_text(rows[6].find('td').text) if len(rows) > 6 else None

        except Exception as e:
            print(f"Error processing the data: {e}")
        
        finally:
            # Clear cookies after the data extraction
            session.cookies.clear()

# Example Usage:
if __name__ == '__main__':
    weather = TimeandDate('https://www.timeanddate.com/weather/uk/london')
    print(f"Temperature: {weather.temperature}")
    print(f"Feels like: {weather.feels_like}")
    print(f"Forecast: {weather.forecast}")
    print(f"Visibility: {weather.visibility}")
    print(f"Pressure: {weather.pressure}")
    print(f"Humidity: {weather.humidity}")
    print(f"Dew point: {weather.dew_point}")
    print(f"Wind speed: {weather.wind}")
