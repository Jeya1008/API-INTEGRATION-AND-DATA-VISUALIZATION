import requests
import json
import matplotlib.pyplot as plt

API_KEY = '77223a930f4b3648e4f961881f801200'

CITIES = {
    "Chennai": (13.0827, 80.2707),
    "Mumbai": (19.0760, 72.8777),
    "Delhi": (28.6139, 77.2090),
    "Kolkata": (22.5726, 88.3639),
    "Bangalore": (12.9716, 77.5946)
}

def fetch_weather(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

def main():
    print("Fetching data from OpenWeatherMap...")
    data = {}
    for city, (lat, lon) in CITIES.items():
        weather = fetch_weather(lat, lon)
        data[city] = weather

    with open("weather_data.json", "w") as f:
        json.dump(data, f, indent=2)

    # Extract metrics
    cities = []
    temps = []
    humidity = []
    rain = []
    pressure = []

    for city, details in data.items():
        main = details.get("main", {})
        rain_data = details.get("rain", {})
        cities.append(city)
        temps.append(main.get("temp", 0))
        humidity.append(main.get("humidity", 0))
        rain.append(rain_data.get("1h", 0))
        pressure.append(main.get("pressure", 0))

    # Dashboard
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Live Weather Dashboard", fontsize=16)

    axs[0, 0].bar(cities, temps, color='tomato')
    axs[0, 0].set_title("Temperature (°C)")

    axs[0, 1].bar(cities, humidity, color='skyblue')
    axs[0, 1].set_title("Humidity (%)")

    axs[1, 0].bar(cities, rain, color='mediumseagreen')
    axs[1, 0].set_title("Rainfall (mm)")

    axs[1, 1].bar(cities, pressure, color='plum')
    axs[1, 1].set_title("Pressure (hPa)")

    for ax in axs.flat:
        ax.set_ylim(bottom=0)
        ax.set_xlabel("City")
        ax.set_ylabel("Value")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig("weather_dashboard.png")
    print("✅ Dashboard saved as 'weather_dashboard.png'")
    plt.show()

if __name__ == "__main__":
    main()
