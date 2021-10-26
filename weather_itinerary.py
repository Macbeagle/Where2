import random 
import requests
from .models import Food, Activity

def get_weather():
    '''Gets the current weather data'''
    api = "http://reg.bom.gov.au/fwo/IDQ60901/IDQ60901.95591.json"

    #Calls the api and cleans the response
    response = requests.get(api)
    current_data = response.json()
    current_data = current_data['observations']["data"]
    current = current_data[0]

    #Determine a nice day
    def weather_forcast():
        ''' Determins if it is a nice day based on weather data '''
        if (current['cloud'] == '-' or current['rain_trace'] == 0.0) and current['gust_kmh'] < 25:
            return True
        else:
            return False
    
    weather = weather_forcast()
    return weather


def create_itinerary():
    ''' Creates the itinerary '''
    #Stores the Food model
    resturants = Food.objects.order_by('time_scene')
    resturant_dict = {
        'Breakfast' : [],
        'Lunch': [],
        'Dinner': []
        }
    
    #Sorts the resturant instances
    for resturant in resturants:
        if resturant.time_scene == 'BR':
            resturant_dict['Breakfast'].append(resturant)
        elif resturant.time_scene == 'LU':
            resturant_dict['Lunch'].append(resturant)
        else:
            resturant_dict['Dinner'].append(resturant)

    def where_to_eat():
        ''' Creates a list of three places to eat '''

        previous_food = [] #this should be global to prevent from being wiped everytime

        # Get where to eat
        breakfast = random.choice(list(resturant_dict['Breakfast']))
        lunch = random.choice(list(resturant_dict['Lunch']))
        dinner = random.choice(list(resturant_dict['Dinner']))

        while breakfast in previous_food or lunch in previous_food or dinner in previous_food:
            breakfast = random.choice(list(resturant_dict['Breakfast']))
            lunch = random.choice(list(resturant_dict['Lunch']))
            dinner = random.choice(list(resturant_dict['Dinner']))

        previous_food = [breakfast, lunch, dinner]

        return breakfast, lunch, dinner

    def get_activities(good_weather, for_itinerary):
        ''' Get the two weather based activities '''
        #TODO: Add a previous activities to prevent the same ones being choosen

        #Stores the activity model
        activities = Activity.objects.order_by('weather')
        activity_dict = {
            'Sunny' : [],
            'Raining': [],
            }

        #Sorts the activity instances
        for activity in activities:
            if activity.weather == 'SU':
                activity_dict['Sunny'].append(activity)
            else:
                activity_dict['Raining'].append(activity)

        #Chooses the two activities
        def loop_activities(weather):
            activity_1 = ''
            activity_2 = ''
            while activity_1 == activity_2:
                activity_1 = random.choice(list(activity_dict[weather]))
                activity_2 = random.choice(list(activity_dict[weather]))
            return activity_1, activity_2

        if good_weather != True:
            # Get wet activites
            activity_1, activity_2 = loop_activities('Raining')
        else:
            # Get dry activites
            activity_1, activity_2 = loop_activities('Sunny')

        # If a single activity should be choosen
        if for_itinerary != True:
            return activity_1
        else:
            return activity_1, activity_2

    def get_itinerary():
        ''' Creates the Itinerary'''
        nice_day = get_weather()
        breakfast, lunch, dinner = where_to_eat()
        activity_1, activity_2 = get_activities(nice_day, True)

        itinerary = [breakfast, activity_1, lunch, activity_2, dinner]	
        return itinerary, nice_day
    
    itinerary, weather = get_itinerary()
    return itinerary, weather
