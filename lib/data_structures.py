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
    }
]

def get_names(spicy_foods):
    print([food["name"] for food in spicy_foods])
    return [food["name"] for food in spicy_foods]
#get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    print([food for food in spicy_foods if food["heat_level"] > 5])
    print([each_food for each_food in spicy_foods if each_food["heat_level"] > 5])
    return [each_food for each_food in spicy_foods if each_food["heat_level"] > 5]
#get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for each_food in spicy_foods:
        print(f'{each_food["name"]} ({each_food["cuisine"]}) | Heat Level: {"🌶" * each_food["heat_level"]}')
        return f'{each_food["name"]} ({each_food["cuisine"]}) | Heat Level: {"🌶" * each_food["heat_level"]}'
#print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for each_food in spicy_foods:
        if each_food["cuisine"] == cuisine:
            print(each_food)  
            return each_food       
#get_spicy_food_by_cuisine(spicy_foods, "Thai")

def print_spiciest_foods(spicy_foods):
    s_f = get_spiciest_foods(spicy_foods)
    print_spicy_foods(s_f)
#print_spiciest_foods(spicy_foods)


#def get_average_heat_level(spicy_foods):
#     return sum(each_food["heat_level"] for each_food in spicy_foods) / len(spicy_foods)
# get_average_heat_level(spicy_foods)

def get_average_heat_level(spicy_foods):
    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)


# def get_names(spicy_foods):
#     return [food["name"] for food in spicy_foods]

# def get_spiciest_foods(spicy_foods):
#     return [food for food in spicy_foods if food["heat_level"] > 5]

# def print_spicy_foods(spicy_foods):
#     for food in spicy_foods:
#         print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     for food in spicy_foods:
#         if food["cuisine"] == cuisine:
#             return food

# # def sort_by_heat(spicy_foods):
# #     return sorted(spicy_foods, key=lambda h: h['heat_level'])

# def print_spiciest_foods(spicy_foods):
#     spiciest_foods = get_spiciest_foods(spicy_foods)
#     print_spicy_foods(spiciest_foods)

# def get_average_heat_level(spicy_foods):
#     return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)