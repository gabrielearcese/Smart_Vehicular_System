import carla
import time

weathers = [
    carla.WeatherParameters.CloudyNoon,
    carla.WeatherParameters.MidRainSunset,
    carla.WeatherParameters.WetNight,
    carla.WeatherParameters.HardRainNoon,
    carla.WeatherParameters.Default,
]

client = carla.Client("localhost", 2000)

client.set_timeout(15)
client.load_world("Town10HD_Opt")
print("Map loaded")
world = client.get_world()
world.set_weather(carla.WeatherParameters.CloudyNoon)
settings = world.get_settings()

for weather in weathers:
    world.set_weather(weather)
    print(f"Weather set to {weather}")
    time.sleep(5)

settings.synchronous_mode = True
print("Setting synchrounous mode")
world.apply_settings(settings)

countS = 0
while countS <= 100:
    world.tick()
    time.sleep(0.1)
    countS += 1
    print(f"Ticked the server {countS}", end="\r")

settings.synchronous_mode = False
world.apply_settings(settings)
print("Setting asynchrounous mode")
client.reload_world()
