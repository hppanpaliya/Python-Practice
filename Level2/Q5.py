def analyze_temperature(temperature_readings):
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    max_temp = max(temperature_readings)
    min_temp = min(temperature_readings)
    return {
        'Average Temperature': round(avg_temp, 1),
        'Highest Temperature': max_temp,
        'Lowest Temperature': min_temp
    }


if __name__ == '__main__':
    temperature_readings = [25, 28, 21, 24, 27]
    assert analyze_temperature(temperature_readings) == {
            'Average Temperature': 25.0,
            'Highest Temperature': 28,
            'Lowest Temperature': 21
        }
    