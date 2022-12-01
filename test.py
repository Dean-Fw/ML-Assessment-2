
y = [1, 0, 0, 0, 1, 2, 1, 1, 2, 1]

classTotals = {}
for i in range(len(y)):
    if y[i] not in classTotals:
        classTotals[y[i]] = 1
    else:
        classTotals[y[i]] += 1

print(f"Class Totals: {classTotals}")

classProbs = {}
for i in classTotals:
    classProbs[i] = classTotals[i] / len(y)

print(classProbs)