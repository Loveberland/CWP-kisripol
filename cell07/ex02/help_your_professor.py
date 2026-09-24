def average(class_scores):
    total_score = 0
    student_count = 0
    for score in class_scores.values():
        total_score += score
        student_count += 1
    return total_score / student_count


if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9,
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13,
    }
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")
