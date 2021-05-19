import json

def read_food_json():
    open_json_file = open('food_db.json', 'r')
    read_json_file = open_json_file.read()

    food_data = json.loads(read_json_file)

    return food_data

def write_food_json(food_dict):
    foods_list = read_food_json()
    foods_list.append(food_dict)

    open_json_file = open('food_db.json', 'w')
    json.dump(foods_list, open_json_file, indent=4)

    return food_dict

def delete_food_json(food_name):
    foods_list = read_food_json()
    for item in foods_list:
        if item['Name'].lower() == food_name.lower():
            foods_list.remove(item)
            open_json_file = open('food_db.json', 'w')
            json.dump(foods_list, open_json_file, indent=4)
            return 200
    return 500

def update_food_json(food_name, new_info):
    foods_list = read_food_json()
    if len(new_info) == 0:
        return 500
    for index, item in enumerate(foods_list):
        if item['Name'].lower() == food_name.lower():
            for update_item in list(new_info.keys()):
                if update_item not in list(item.keys()):
                    return 500
            foods_list[index].update(new_info)
            open_json_file = open('food_db.json', 'w')
            json.dump(foods_list, open_json_file, indent=4)
            return 200
    return 500