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


def calculate_order_total(prices, discount_rate, tax_rate):
    subtotal = 0
    for price in prices:
        if price < 0:
            continue
        subtotal += price
    discount = subtotal * discount_rate
    taxed_base = subtotal - discount
    tax = taxed_base * tax_rate
    total = taxed_base + tax
    return round(total, 2)
