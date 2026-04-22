"""Utility functions created for the user's request."""


def format_user_profile(name, age, city, hobbies):
    cleaned_name = name.strip().title()
    normalized_city = city.strip().title()
    hobby_list = []
    for hobby in hobbies:
        item = hobby.strip().lower()
        if item:
            hobby_list.append(item)
    hobby_text = ", ".join(hobby_list) if hobby_list else "no hobbies listed"
    profile = f"{cleaned_name}, {age}, lives in {normalized_city}"
    return f"{profile}. Hobbies: {hobby_text}."
