import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate dates
def get_location_weather_report(latitude, longitude): 
    today = datetime.now()
    week_ago = today - timedelta(days=7)
    start_date = week_ago.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(url)
    print(response.json())
    return response.json()

def get_pd_report(): 
    data = get_location_weather_report(48.85, 2.35)
    daily_data = data['daily']
    df = pd.DataFrame({
        'date': daily_data['time'],
        'max_temp': daily_data['temperature_2m_max'],
        'min_temp': daily_data['temperature_2m_min']
    })
    # Convert date strings to datetime
    df['date'] = pd.to_datetime(df['date'])
    print(df)
    return df


def creating_data_plot():
    # Create the plot
    plt.figure(figsize=(10, 6))
    df = get_pd_report()
    plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
    plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Paris Weather - Past 7 Days')
    plt.legend()

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plt.savefig('weather_chart.png')
    plt.show()

# Save to excel

def save_to_excel():
    if not os.path.exists('data'):
        os.makedirs('data')

    get_pd_report.to_csv('data/paris_weather.csv', index=False)
    print("Data saved to data/paris_weather.csv")


creating_data_plot()
