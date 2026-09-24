def sorting(keys_list, items_list):
    sorted_keys = []
    while items_list:
        latest_birth_year = 0
        selected_index = 0
        for index, birth_year_text in enumerate(items_list):
            birth_year = int(birth_year_text)
            if birth_year > latest_birth_year:
                latest_birth_year = birth_year
                selected_index = index
        sorted_keys.append(keys_list.pop(selected_index))
        items_list.pop(selected_index)
    return sorted_keys


def famous_births(scientists_dict):
    scientist_ids = []
    birth_years = []
    for scientist_id, scientist in scientists_dict.items():
        scientist_ids.append(scientist_id)
        birth_years.append(scientist["date_of_birth"])
    return sorting(scientist_ids, birth_years)


if __name__ == "__main__":
    women_scientists = {
        "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
        "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
        "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
        "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
    }
    for scientist_id in famous_births(women_scientists)[::-1]:
        scientist = women_scientists[scientist_id]
        print(
            f"{scientist['name']} is a great scientist "
            f"born in {scientist['date_of_birth']}."
        )
