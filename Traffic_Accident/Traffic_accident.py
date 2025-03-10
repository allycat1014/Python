import pandas
from Crash_type_to_damage import Crash_type_to_damage
import operator

accident_file = pandas.read_csv('traffic_data/traffic_accidents.csv', encoding='latin1', usecols=['crash_date', 'traffic_control_device', 'weather_condition', 'lighting_condition', 'first_crash_type', 'trafficway_type', 'alignment','roadway_surface_cond', 'road_defect','crash_type', 'intersection_related_i','damage','prim_contributory_cause','num_units','most_severe_injury','injuries_total','injuries_fatal','injuries_incapacitating','injuries_non_incapacitating','injuries_reported_not_evident','injuries_no_indication','crash_hour','crash_day_of_week','crash_month'])
accidents = accident_file.to_dict(orient='records')

crash_type_to_crash_type_with_total_damage = {}


for accident in accidents:
    crash_date = str(accident['crash_date'])
    traffic_control_device = str(accident['traffic_control_device'])
    weather_condition = str(accident['weather_condition'])
    lighting_condition = str(accident['lighting_condition'])
    first_crash_type = str(accident['first_crash_type'])
    trafficway_type = str(accident['trafficway_type'])
    alignment = str(accident['alignment'])
    roadway_surface_cond = str(accident['roadway_surface_cond'])
    road_defect = str(accident['road_defect'])
    crash_type = str(accident['crash_type'])
    intersection_related = str(accident['intersection_related_i'])
    damage = str(accident['damage'])
    prim_contributory_cause = str(accident['prim_contributory_cause'])
    num_units = int(accident['num_units'])
    most_severe_injury = str(accident['most_severe_injury'])
    injuries_total = float(accident['injuries_total'])
    crash_hour = int(accident['crash_hour'])
    crash_day_of_week = int(accident['crash_day_of_week'])
    crash_month = int(accident['crash_month'])

    if crash_type not in crash_type_to_crash_type_with_total_damage.keys():
        crash_type_obj = Crash_type_to_damage(first_crash_type)
        crash_type_to_crash_type_with_total_damage[first_crash_type] = crash_type_obj
    else:
        crash_type_obj = crash_type_to_crash_type_with_total_damage.get(first_crash_type)



'''
Which crash type has most damage
first make class with name crash_type_to_damage
    - 2 attributes - crash_type and damage
make dictionary crash_type_to_crash_type_with_total_damage
    - key will be crash_type and value will be the Class object
write function to parse damage name it parseDamage
first write parseDamage function then underneath write for loop and everytime
    the for loop goes over damage call the function and the function will return a number ex: 500 instead of $500
once damage number is parsed add the number to the total_damage variable which is in the Class
for accident in accidents:
    first_crash_type = str(accident['first_crash_type'])
    damage = str(accident['damage'])
    crash_type_obj = crash_type_to_crash_type_with_total_damage.get(first_crash_type)
    crash_type_obj.add_to_total_damage(damage)

sorted_list = sorted(crash_type_to_crash_type_with_total_damage.values(), key=operator.attrgetter('total_damage'), reverse=True)

print(sorted_list[0])
'''










'''
What is the most frequent type of damage?
'''




'''
- How many accidents happen while it’s raining and night
count total accident that happen at night
count total accident that happen while its raining
add both of the numbers
accidents_while_raining = 0
accidents_while_night = 0
accidents_while_raining_night = 0
for accident in accidents:
    lighting_condition = str(accident['lighting_condition'])
    weather_condition = str(accident['weather_condition'])
    if lighting_condition == "DARKNESS" or lighting_condition == "DARKNESS, LIGHTED ROAD":
        accidents_while_night += 1
    elif weather_condition == "RAIN":
        accidents_while_raining += 1
    accidents_while_raining_night = (accidents_while_night+accidents_while_raining)
print(accidents_while_raining_night)
'''
'''
- What percent of accidents happen in day
count up total accidents that have happened 
count up total accident that happened in the day
divide the accidents that happened in the day by the total accident that happened
mutiple that number by 100

total_accidents = 0
accidents_in_day = 0
percent_of_accidents_in_day = 0

for accident in accidents:
    lighting_condition = str(accident['lighting_condition'])
    total_accidents = len(accidents)
    if lighting_condition == "DAYLIGHT":
        accidents_in_day += 1
    percent_of_accidents_in_day = ((accidents_in_day/total_accidents)*100)

print(percent_of_accidents_in_day)
'''

'''
- Find trends between raining and day accident

'''
'''
- Find trends between type of accident and weather condition
'''
