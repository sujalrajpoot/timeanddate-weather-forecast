
# TimeandDate Weather Scraper
The TimeandDate Weather Scraper is a Python class that allows users to scrape and extract real-time weather data from the timeanddate.com website for any specified location.

This tool helps developers, hobbyists, and weather enthusiasts gather structured weather information such as temperature, wind conditions, humidity, visibility, pressure, dew point, and forecast data, which can be programmatically accessed and utilized.
# Authors

- [@sujalrajpoot](https://github.com/sujalrajpoot)

# Features

- Extracts real-time weather data from the Time and Date website for any specified location.
- Captures various weather parameters, including:
    - Temperature
    - Feels Like temperature
    - Forecast for the day
    - Visibility
    - Pressure
    - Humidity
    - Dew Point
    - Wind Speed and Direction
- Uses requests.Session to maintain a persistent connection and clear cookies after fetching data.

# How It Can Help

- Weather Aggregators: Developers can use this script to build weather aggregator services or dashboards.
- Automated Alerts: You can integrate it into automation systems to fetch weather updates and send notifications.
- Educational Purpose: It’s an excellent tool for learning how to work with web scraping libraries such as requests and BeautifulSoup.
- Simplicity: The class allows users to easily retrieve specific weather data with minimal setup and code.

# Requirements

- Make sure you have the following Python packages installed:

- requests
- beautifulsoup4
- re (part of Python’s standard library)
### You can install the required packages using pip:

- pip install requests beautifulsoup4
## Usage/Examples

```python
# Import the TimeandDate class
from timeanddate_weather_scraper import TimeandDate

# Instantiate the class with the URL of the desired location's weather page
weather = TimeandDate('https://www.timeanddate.com/weather/uk/london')

# Access weather attributes
print("Temperature:", weather.temperature)
print("Feels Like:", weather.feels_like)
print("Forecast:", weather.forecast)
print("Visibility:", weather.visibility)
print("Pressure:", weather.pressure)
print("Humidity:", weather.humidity)
print("Dew Point:", weather.dew_point)
print("Wind:", weather.wind)
```
```
Output:
Temperature: 15 °C
Feels Like: 14 °C
Forecast: 19 °C to 13 °C
Visibility: 10 km
Pressure: 1005 mbar
Humidity: 82%
Dew Point: 12 °C
Wind: 17 km/h from West
```


## Running Tests

To run tests, run the following command

```python
python timeanddate_weather_scraper.py
```


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Installation


```bash
Clone the repository:
git clone https://github.com/sujalrajpoot/timeanddate-weather-forecast.git

Install the required packages: 
pip install requests beautifulsoup4
```
    
## 🚀 About Me
I'm a skilled Python programmer and experienced web developer. With a strong background in programming and a passion for creating interactive and engaging web experiences, I specialize in crafting dynamic websites and applications. I'm dedicated to transforming ideas into functional and user-friendly digital solutions. Explore my portfolio to see my work in action.
# Hi, I'm Sujal Rajpoot! 👋


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sujalrajpoot.netlify.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sujal-rajpoot-469888305/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/sujalrajpoot70)


# Disclaimer
This project is for educational and personal use only. The script scrapes data from AccuWeather and other related sources without explicit permission from these websites. Usage of this script must comply with the terms and conditions and policies of AccuWeather and other websites being scraped.
