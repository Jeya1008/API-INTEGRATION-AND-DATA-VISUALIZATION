# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY : CODTECH IT SOLUTIONS

NAME : M JEYA BHARATHI

INTERN ID : CT04DG139

DOMAIN : PYTHON

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH

DESCRIPTION :

This project is centered around the integration of real-time weather data from a public API with Python and transforming that raw data into meaningful visual insights using Seaborn, a popular data visualization library. Specifically, it focuses on using the OpenWeatherMap API, which provides up-to-date meteorological information for any location in the world. The main objective of the project is to collect current weather data for multiple cities and visualize key weather attributes such as temperature, humidity, pressure, wind speed, and rainfall in a comparative manner.

The first step in the project involves setting up access to the OpenWeatherMap API. This API requires an API key, which is freely available upon registration. Using the Python requests library, the script sends HTTP GET requests to the API endpoint by providing latitude and longitude coordinates along with the API key. The response is returned in JSON format, which is parsed to extract relevant weather parameters.

Once the data is collected for a list of cities, it is processed into a structured format using Python dictionaries and lists. This structured data includes numerical values for temperature (in Celsius), humidity (percentage), pressure (in hPa), wind speed (m/s), and rainfall (mm). These values are then aggregated for all cities and passed into a Pandas DataFrame, which serves as the base structure for visualization.

The project uses Seaborn to plot bar charts that represent each of these weather features across cities. Seaborn is built on top of Matplotlib and provides an intuitive interface for statistical plots. For each weather metric, a bar graph is generated that displays the values for all cities side-by-side, allowing for quick visual comparison. The graphs are rendered using Matplotlib’s pyplot interface, making the dashboard viewable directly in a Python script.

Through this approach, users can visually interpret and compare weather trends in multiple locations. For instance, the bar charts help answer questions like which city is the most humid, where it’s currently raining, or which city is experiencing the highest wind speeds. This makes the project not only a demonstration of API integration and data handling but also a practical tool for real-world meteorological comparison.

RESOURCES USED :

Python 3: Primary programming language for scripting.

Requests: Python module to fetch data via HTTP.

JSON: Format used to parse API responses.

Matplotlib & Seaborn: Used for creating clean, professional bar charts.

OpenWeatherMap API: Public API used to retrieve real-time weather data.

