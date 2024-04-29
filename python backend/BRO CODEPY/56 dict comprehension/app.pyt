# cities_in_F = {"Nsawam": 32, "Accra": 75, "kumama": 120, "La": 50}
# cities_in_C = {key: ((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
# print(cities_in_C)

# weather = {"New York": "Snowing", "Boston": "sunny", "los angles": "sunny", "accra":"cozy"}
# sunny_weather = {key:value for (key, value) in weather.items() if value == "sunny"}
# print(sunny_weather)


# cities = {"Nsawam": 32, "Accra": 75, "kumama": 10, "La": 50}
# desc_cities = {key:("warmth" if value >= 40 else "cold") for (key,value) in cities.items()}
# print(desc_cities)



def check_temp(value):
    if value >=70:
        return 'HOT' 
    elif 67 >= value >= 40:
        return 'WARM'
    else:
        return "cold"
cities = {"Nsawam": 32, "Accra": 75, "kumama": 10, "La": 50}
desc_cities = {key:check_temp(value) for (key,value) in cities.items()}
print(desc_cities)
