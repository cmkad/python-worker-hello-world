import discord

color=0xFF6500
key_features = {#Key:Value
    'temp' : 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' : 'Minimum Temperature',
    'temp_max' : 'Maximum Temperature'
}

def parse_data(data):
    goodData = {}
    for key in data:
        if key in key_features:
            goodData[key] = data[key]
    return goodData

def weather_message(data, location):
    location = location.title()
    message = discord.Embed(
        title=f'{location} Weather',
        description=f'Here is the weather data for {location}.',
        color=color
    )
    for key in data:
        message.add_field(
            name=key_features[key],
            value=str(data[key]),
            inline=False
        )
    return message

def error_message(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location}.',
        color=color
    )
