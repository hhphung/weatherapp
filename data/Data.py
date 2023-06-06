
class Data ():
    def __init__(self, data):
        self.name  = data['name']
        self.temperature = data['main']['temp']
        self.feel_like =data['main']['feels_like']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']
        self.humidity = data['main']['humidity']
        self.visibility = data['visibility']
        self.wind = data['wind']['speed']
        self.wind_dir = data['wind']['deg']
        self.clounds = data['clouds']['all']


        self.weather_desc= data['weather'][0]['description']
        self.weather_status = data['weather'][0]['main']

        self.datetime = data['dt']

        self.country= data['sys']['country']
        self.sunrise = data['sys']['sunrise']
        self.sunset = data['sys']['sunset']

        self.base = data['base']

    def temp_in_C(self):
        celsius = int(self.temperature - 273.15)
        return celsius
    def temp_in_F(self):
        fahrenheit = int((self.temperature - 273.15) * 9 / 5 + 32)
        return fahrenheit




