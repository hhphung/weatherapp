
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
        self.clounds = data['clounds']['all']


        self.weather_desc= data['weather']['description']
        self.weather_status = data['weather']['mains']

        self.dattime = data['st']

        self.country= data['sys']['country']
        self.sunrise = data['sys']['sunrise']
        self.sunset = data['sys']['sunset']

        self.base = data['base']



