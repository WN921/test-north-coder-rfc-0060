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
