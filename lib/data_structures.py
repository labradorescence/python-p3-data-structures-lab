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

# def get_names(spicy_foods): #declare function 
#     for each_food in spicy_foods: #iterate the list
#         print(each_food["name"])
#     pass

# get_names(spicy_foods) #function invocation

######################
#long version
#def get_spiciest_foods(spicy_foods):
#     spicy_foods_list = [] # create listt

#     for  each_food in spicy_foods: # for loop, grab each dictionary
#         if each_food["heat_level"] > 5: #if the heat level is greater than 5
#             spicy_foods_list.append(each_food)
#         print(spicy_foods_list)
#         return spicy_foods_list
# get_spiciest_foods(spicy_foods)

######################
#shorter version
def get_spiciest_foods(spicy_foods):
    return [ each_food for each_food in spicy_foods if each_food["heat_level"] > 5]

# print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for each_food in spicy_foods: # for loop
        print(f'{each_food["name"]} ({each_food["cuisine"]})') #name and cuisine
    pass

# print(print_spicy_foods(spicy_foods))

# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     for each_food in spicy_foods: #iterate over the entire spicy foods
#         if each_food["cuisine"] == cuisine: #if cuisine value matches the cuisine param
#             print(each_food)
#             return each_food
#     pass
# get_spicy_food_by_cuisine(spicy_foods, "Sichuan")

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))
    #get_spiciest_food returns a list comprised of dictionaries
    #so use the function invocation as a parameter
    pass

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    #longer version 
    # sum = 0
    # for each_food in spicy_foods:
    #     sum += each_food["heat_level"]
    # print(sum/len(spicy_foods))

    #short version 
    print(sum([each_food["heat_level"] for each_food in spicy_foods])/len(spicy_foods))
    pass
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass