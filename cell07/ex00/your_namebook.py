def array_of_names(persons_dict):
    full_names = []
    for first_name, last_name in persons_dict.items():
        formatted_first_name = first_name[0].upper() + first_name[1:]
        formatted_last_name = last_name[0].upper() + last_name[1:]
        full_names.append(formatted_first_name + " " + formatted_last_name)
    return full_names


if __name__ == "__main__":
    people = {
        "jean": "valjean",
        "grace": "hopper",
        "ivier": "niel",
        "fifi": "brindacier",
    }
    print(array_of_names(people))
