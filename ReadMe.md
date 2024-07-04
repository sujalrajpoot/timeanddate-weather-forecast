# Weather Scraper

This project is a Python script to scrape weather data from the www.timeanddate.com website for a given location. The script extracts various weather parameters such as temperature, visibility, pressure, humidity, dew point, feels-like temperature, forecast, and wind information.

## Example

You can extract weather data from the following URL: [https://www.timeanddate.com/weather/uk/london]
```python

url = 'https://www.timeanddate.com/weather/uk/london'
weather_data = timeanddate.extract_weather_data(url)
print(weather_data)

The script will output a dictionary with the following keys:

- `temperature`
- `visibility`
- `pressure`
- `humidity`
- `dew_point`
- `feels_like`
- `forecast`
- `wind`

Example output:
```python
{
    'temperature': '15 °C',
    'visibility': 'N/A',
    'pressure': '1005 mbar',
    'humidity': '82%',
    'dew_point': '12 °C',
    'feels_like': '14 °C',
    'forecast': '19 °C to 13 °C',
    'wind': '17 km/h from West'
}
