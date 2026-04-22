def summarize_scores(scores):
    valid_scores = [score for score in scores if isinstance(score, (int, float))]
    if not valid_scores:
        return {"count": 0, "average": 0, "highest": None, "lowest": None}

    total = 0
    highest = valid_scores[0]
    lowest = valid_scores[0]
    for score in valid_scores:
        total += score
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score

    average = total / len(valid_scores)
    return {"count": len(valid_scores), "average": average, "highest": highest, "lowest": lowest}


def format_user_record(name, age, tags):
    clean_name = str(name).strip().title()
    safe_age = int(age) if age is not None else 0
    normalized_tags = []
    for tag in tags:
        text = str(tag).strip().lower()
        if text and text not in normalized_tags:
            normalized_tags.append(text)

    description = f"{clean_name} is {safe_age} years old."
    if normalized_tags:
        description += f" Tags: {', '.join(normalized_tags)}."
    return {"name": clean_name, "age": safe_age, "tags": normalized_tags, "description": description}


def build_report(items):
    lines = []
    total_length = 0
    for index, item in enumerate(items, start=1):
        text = str(item).strip()
        if not text:
            continue

        total_length += len(text)
        lines.append(f"{index}. {text}")

    report = "\n".join(lines)
    return {
        "line_count": len(lines),
        "character_count": total_length,
        "report": report,
    }
