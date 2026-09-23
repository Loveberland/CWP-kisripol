def sorting(keys_list, items_list):
    sorted_keys = []
    while len(items_list) > 0:
        oldest_birth_year = 0
        oldest_index = 0
        for i in items_list:
            if int(i) > oldest_birth_year:
                oldest_birth_year = int(i)
                oldest_index = items_list.index(i)
        sorted_keys.append(keys_list.pop(oldest_index))
        items_list.pop(oldest_index)
    return sorted_keys

def famous_births(scientists_dict):
    keys_list = []
    items_list = []
    for i in scientists_dict:
        keys_list.append(i)
        items_list.append(scientists_dict[i]["date_of_birth"])
    return sorting(keys_list, items_list)

if __name__ == "__main__":
    women_scientists = {
            "ada": { "name": "Ada Lovelace", "date_of_birth": "1815"}, 
            "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" }, 
            "lise": {"name": "Lise Meitner", "date_of_birth": "1878"}, 
            "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}}
    for i in famous_births(women_scientists)[::-1]:
        print(f"{women_scientists[i]["name"]} is a great scientist born in {women_scientists[i]["date_of_birth"]}.")
