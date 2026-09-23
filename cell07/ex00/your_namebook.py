def array_of_names(persons_dict):
    full_names = []
    for i in persons_dict:
        full_names.append(i[0].upper()+i[1:]+" "+persons_dict[i][0].upper()+persons_dict[i][1:])
    return full_names

if __name__ == "__main__":
    person = {
            "jean": "valjean", 
            "grace": "hopper", 
            "ivier": "niel", 
            "fifi": "brindacier"}
    print(array_of_names(person))
