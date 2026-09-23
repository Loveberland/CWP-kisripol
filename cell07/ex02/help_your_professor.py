def average(class_scores):
    total_score = 0
    total_students = 0
    for i in class_scores.keys():
        total_score += class_scores[i]
        total_students += 1
    return total_score/total_students

if __name__ == "__main__":
    class_3B = {
            "marine": 18,
            "jean": 15, 
            "coline": 8,
            "luc": 9}
    class_3C = {
            "quentin": 17,
            "julie": 15, 
            "marc": 8, 
            "stephanie": 13}
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")
