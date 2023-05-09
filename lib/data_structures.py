spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

############## get_names ##############################
##### longer version #####
# def get_names(spicy_foods):
#     names = []
#     for each_food in spicy_foods:
#             names.append(each_food["name"])
#     print(names)
#     return names
#     pass   

##### shorter version #####
def get_names(spicy_foods):
    #print([each_food["name"] for each_food in spicy_foods])
    return [each_food["name"] for each_food in spicy_foods]
    pass
#get_names(spicy_foods)



############## get_spiciest_foods ######################
#### longer version ####
# def get_spiciest_foods(spicy_foods):
#     spicy_foods_list = []
#     for each_food in spicy_foods:
#         if each_food["heat_level"] > 5: #if the heat level is greater than 5
#             spicy_foods_list.append(each_food)
#     print(spicy_foods_list)
#     return spicy_foods_list
#     pass

##### shorter version #####
def get_spiciest_foods(spicy_foods):
    return [ each_food for each_food in spicy_foods if each_food["heat_level"] > 5 ]

#get_spiciest_foods(spicy_foods)


############## print_spicy_foods ######################
# def print_spicy_foods(spicy_foods):
#     for each_food in spicy_foods:
#         print(f'{each_food["name"]} ({each_food["cuisine"]}) | Heat Level: {each_food["heat_level"] * "🌶"}')
#     pass

def print_spicy_foods(spicy_foods):
    for each_food in spicy_foods:
        name = each_food["name"]
        cuisine = each_food["cuisine"]
        heat_level = each_food["heat_level"]*"🌶"
        
        print(f'{name} ({cuisine}) | Heat Level: {heat_level}')

#print(print_spicy_foods(spicy_foods))


def get_spicy_food_by_cuisine(spicy_foods, cuisine):

    for each_food in spicy_foods:
        if each_food["cuisine"] == cuisine:
            print(each_food)
            return each_food
    pass

#get_spicy_food_by_cuisine(spicy_foods, "Thai")


def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))
    pass
#print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    sum = 0
    for each_food in spicy_foods:
        sum += each_food["heat_level"]
    print(sum/len(spicy_foods))
    return sum/len(spicy_foods)
    pass
#get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
