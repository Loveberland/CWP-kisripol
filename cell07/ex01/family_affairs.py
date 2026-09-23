def find_the_redheads(family_dict):
    redheads_list = []
    for i in family_dict.keys():
        if family_dict[i] == "red":
            redheads_list.append(i)
    return redheads_list

if __name__ == "__main__":
    dupont_family = {
            "florian": "red", 
            "marie": "blond",
            "virginie": "brunette", 
            "david": "red", 
            "franck": "red"}
    print(find_the_redheads(dupont_family))
