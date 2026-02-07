def stats(words):
    total = 0
    average = 0
    topScore = 0

    for i in words:
        num = int(i)
        total = total + num
        topScore = max(topScore, num)

    average = total / len(words)
    return total, average, topScore
