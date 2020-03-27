
def user_info():
    age = int(input('What is your age: '))
    gender = input('What is your gender: ')
    weight = int(input('What is your weight: '))
    height = int(input('What is your height in inches: '))


    if gender == 'male':
        c1 = 66
        hm = 6.2 * height
        wm = 12.7 * weight
        am = 6.76 * age
    elif gender == 'female':
        c1 = 655.1
        hm = 4.35 * height
        wm = 4.7 * weight
        am = 4.7 * age

    #BMR = 665 + (9.6 X 69) + (1.8 x 178) – (4.7 x 27)
    bmr_result = c1 + hm + wm - am
    return int(bmr_result)


def calculate_activity(bmr_result):
    activity_level = input('What is your activity level (none, light, moderate, heavy, or extreme): ')

    if activity_level == 'none':
        activity_level = 1.2 * bmr_result
    elif activity_level == 'light':
        activity_level = 1.375 * bmr_result
    elif activity_level == 'moderate':
        activity_level = 1.55 * bmr_result
    elif activity_level == 'heavy':
        activity_level = 1.725 * bmr_result
    elif activity_level == 'extreme':
        activity_level = 1.9 * bmr_result

    return(int(activity_level))

def gain_or_lose(activity_level):
    goals = input('Do you want to lose, maintain, or gain weight: ')

    if goals == 'lose':
        calories = activity_level - 500
    elif goals == 'maintain':
        calories = activity_level
    elif goals == 'gain':
        gain = int(input('Gain 1 or 2 pounds per week? Enter 1 or 2: '))
        if gain == 1:
            calories = activity_level + 500
        elif gain == 2:
            calories = activity_level + 1000

    print('in order to ', goals, 'weight, your daily caloric goals should be', int(calories), '!')


gain_or_lose(calculate_activity(user_info()))



import json
Food ='''
{
  "food": [
        {"foodName":"BBQ Chicken Flatbread", "foodType":"Sandwich", "calories":380, "carbs":41 },
        {"foodName":"Chicken Flatbread", "calories":380, "correctedTerm":"BBQ Chicken Flatbread", "carbs":41 },
        {"foodName":"Tomato Mozzarella Flatbread", "calories":350, "carbs":35 },
	    {"foodName":"Roasted Turkey Cranberry Flatbread", "calories":310, "carbs":36 },
	    {"foodName":"Turkey Cranberry Flatbread", "calories":310, "carbs":36 },
	    {"foodName":"Half Size Italian on Hoagie Roll", "calories":440, "carbs":38 },
	    {"foodName":"Half Italian", "calories":440, "correctedTerm":"Half Size Italian on Hoagie Roll", "carbs":38 },
        {"foodName":"Italian", "calories":880, "correctedTerm":"Italian on Hoagie Roll", "carbs":75 },
        {"foodName":"Chicken Burrito", "foodType":"Burrito", "protein":"chicken", "calories":975},
        {"foodName":"Steak Burrito", "foodType":"Burrito", "protein":"steak", "calories":945},
        {"foodName":"Carnitas Burrito", "foodType":"Burrito", "protein":"carnitas", "calories":1005},
        {"foodName":"Barbacoa Burrito", "foodType":"Burrito", "protein":"barbacoa", "calories":965},
        {"foodName":"Chorizo Burrito", "foodType":"Burrito", "protein":"chorizo", "calories":1095},
        {"foodName":"Sofritas Burrito", "foodType":"Burrito", "protein":"sofritas", "calories":945},
        {"foodName":"Chicken Burrito Bowl", "foodType":"Burrito Bowl", "calories":630},
        {"foodName":"Chicken Bowl", "calories":630},
        {"foodName":"Steak Burrito Bowl", "foodType":"Burrito Bowl", "calories":600},
        {"foodName":"Steak Bowl", "calories":600}
  ]
}'''
data = json.loads(Food)
print(data)
calories = input('Please input calories:')
for food in data['food']:
     if (food["calories"] == (calories)):
         food_name= str(food["foodName"])
print(food['foodName'])

