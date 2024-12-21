def floodFill(x, y, crop, m, found):
    if (x, y) in found: return found, 0
    if not (0 <= y < len(m)) or not (0 <= x < len(m[y])) or m[y][x] != crop: return found, 1

    found.append((x,y))

    found, p0 = floodFill(x, y+1, crop, m, found)
    found, p1 = floodFill(x, y-1, crop, m, found)
    found, p2 = floodFill(x+1, y, crop, m, found)
    found, p3 = floodFill(x-1, y, crop, m, found)

    return found, p0+p1+p2+p3

def t1(data):
    m = [list(l) for l in data.split("\n")]
    fields = {}
    total = 0
    for y in range(len(m)):
        for x in range(len(m[y])):
            crop = m[y][x]
            if crop not in fields: fields[crop] = []
            elif (x, y) in fields[crop]: continue
            found, perimiter = floodFill(x, y, crop, m, [])
            fields[crop] += found
            total += len(found) * perimiter
            print(f"Region {crop} with Price: {len(found)} * {perimiter} = {len(found) * perimiter}")
    return total

def floodFillSides(x, y, dir, crop, m, found, sides):
    if (x, y) in found: return found, sides
    if not (0 <= y < len(m)) or not (0 <= x < len(m[y])) or m[y][x] != crop:
        if dir in "ns":
            if f"{dir}{y}" not in sides.keys():
                sides[f"{dir}{y}"] = []
            sides[f"{dir}{y}"].append(x)
        if dir in "ew":
            if f"{dir}{x}" not in sides.keys():
                sides[f"{dir}{x}"] = []
            sides[f"{dir}{x}"].append(y)

        return found, sides
    found.append((x,y))

    found, sides = floodFillSides(x, y+1, "n", crop, m, found, sides)
    found, sides = floodFillSides(x, y-1, "s", crop, m, found, sides)
    found, sides = floodFillSides(x+1, y, "e", crop, m, found, sides)
    found, sides = floodFillSides(x-1, y, "w", crop, m, found, sides)

    return found, sides

def t2(data):
    m = [list(l) for l in data.split("\n")]
    fields = {}
    total = 0
    for y in range(len(m)):
        for x in range(len(m[y])):
            crop = m[y][x]
            if crop not in fields: fields[crop] = []
            elif (x, y) in fields[crop]: continue
            found, sides = floodFillSides(x, y, "", crop, m, [], {})

            totalSides = 0
            for dir in sides.keys():
                sides[dir].sort()
                totalSides += sum([1 for i in range(1, len(sides[dir])) if sides[dir][i-1]+1 != sides[dir][i]]) + 1

            fields[crop] += found
            total += len(found) * totalSides
            print(f"Region {crop} with Price: {len(found)} * {totalSides} = {len(found) * totalSides}")
    return total

def getData(): return open("data/" + __file__.split("/")[-1].split(".")[0] + ".txt").read()
if __name__ == "__main__":
    data = getData()
    print(t1(data))
    print(t2(data))