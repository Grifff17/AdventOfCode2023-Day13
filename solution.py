
def solvepart1():
    data = fileRead("input.txt")
    data.append("\n")
    patterns = []
    currentPattern = []
    for row in data:
        if (row == "\n"):
            patterns.append(currentPattern.copy())
            currentPattern = []
        else:
            currentPattern.append(row.strip())

    sum = 0
    for pattern in patterns:
        val = checkPattern(pattern)
        sum = sum + val
    print(sum)

def solvepart2():
    data = fileRead("input.txt")
    data.append("\n")
    patterns = []
    currentPattern = []
    for row in data:
        if (row == "\n"):
            patterns.append(currentPattern.copy())
            currentPattern = []
        else:
            currentPattern.append(row.strip())

    sum = 0
    for pattern in patterns:
        val = checkSmudge(pattern)
        print(val)
        sum = sum + val
    print(sum)

def checkSmudge(pattern):
    oldPatternVal = checkPattern(pattern)
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            newPattern = pattern.copy()
            if pattern[i][j] == "#":
                newPattern[i] = newPattern[i][:j] + "." + newPattern[i][j+1:]
            else:
                newPattern[i] = newPattern[i][:j] + "#" + newPattern[i][j+1:]
            result = checkPattern(newPattern, oldPatternVal)
            if result != 0:
                return result

def checkPattern(pattern, oldPatternVal = -1):
    sum = 0

    for i in range(1,len(pattern[0])):
        sucessA = True
        sucessB = True
        for j in range(len(pattern)):
            left = pattern[j][:i][::-1]
            right = pattern[j][i:]
            if not (left[:len(right)] == right):
                sucessA = False
            if not (left == right[:len(left)]):
                sucessB = False
        if (sucessA or sucessB) and i != oldPatternVal:
            sum = sum + i
            break

    for i in range(1, len(pattern)):
        sucessA = True
        sucessB = True
        for j in range(len(pattern[0])):
            left = "".join([ row[j] for row in pattern[:i] ])[::-1]
            right = "".join([ row[j] for row in pattern[i:] ])
            if not (left[:len(right)] == right):
                sucessA = False
            if not (left == right[:len(left)]):
                sucessB = False
        if (sucessA or sucessB) and i*100 != oldPatternVal:
            sum = sum + (i * 100)
            break
    return sum
    
def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart2()