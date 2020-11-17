# 93644991 Zihao Han
# knapsack algorithm
def knapsack(valueList, weightList, weightLimitation):
    result = []
    path = []
    # padding array
    for i in range(0,len(valueList)+1):
        resultItem = []
        pathItem = []
        for j in range(0, weightLimitation + 1):
            resultItem.append(0)
            pathItem.append("")
        result.append(resultItem)
        path.append(pathItem)
    # iterate array
    for i in range(1, len(valueList)+1):
        for j in range(0, weightLimitation+1):
            n = 1
            path[i][j] = path[i - 1][j]
            if weightList[i-1] > j:
                result[i][j] = result[i-1][j]
                continue
            while n * weightList[i-1] <= j:
                if n * valueList[i-1] + result[i-1][j - n * weightList[i-1]] > result[i-1][j] and n * valueList[i-1] + result[i-1][j - n * weightList[i-1]] > result[i][j]:
                    path[i][j] = path[i-1][j - n * weightList[i-1]]
                    for m in range(0, n):
                        path[i][j] = path[i][j] + " " + str(i)
                result[i][j] = max(result[i-1][j], n * valueList[i-1] + result[i-1][j - n * weightList[i-1]], result[i][j])
                n = n+1

    print(result[-1][-1])
    print(path[-1][-1].strip())
    print()
    print()
    print("2D array:")
    print(result)
    print("path array:")
    print(path)

# read file
f = open("KP_input_1.txt")
input = f.read().split()
weightLimitation = int(input[0])
valueList = []
weightList = []
for i in range(1, len(input)):
    if (i - 1) % 3 == 1:
        weightList.append(int(input[i]))
    if (i - 1) % 3 == 2:
        valueList.append(int(input[i]))
knapsack(valueList, weightList, weightLimitation)



