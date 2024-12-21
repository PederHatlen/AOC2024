def t1(data):
    map = [list(l) for l in data.split("\n\n")[0].split("\n")]
    instructions = "".join(data.split("\n\n")[1].split("\n"))

    rx, ry = 0,0
    for y in range(len(map)):
        if "@" in map[y]: 
            rx, ry = map[y].index("@"), y
            break

    for i in instructions:
        dx = 1 if i == ">" else -1 if i == "<" else 0
        dy = 1 if i == "v" else -1 if i == "^" else 0
        
        if map[ry+dy][rx+dx] == ".":
            map[ry][rx], map[ry+dy][rx+dx] = ".", "@"
            rx += dx
            ry += dy
        elif map[ry+dy][rx+dx] == "#": continue
        elif map[ry+dy][rx+dx] == "O":
            for o in range(1, len(map[0])):
                if map[ry+(dy*o)][rx+(dx*o)] == "#": break
                if map[ry+(dy*o)][rx+(dx*o)] == ".":
                    map[ry+(dy*o)][rx+(dx*o)] = "O"
                    map[ry][rx], map[ry+dy][rx+dx] = ".", "@"
                    rx += dx
                    ry += dy
                    break
    return sum([sum([y*100 + x for x in range(len(map[y])) if map[y][x] == "O"]) for y in range(len(map))])
    # 1517819

def findCrateBlock(rx, ry, dx, dy, maap):
    x, y = rx+dx, ry+dy
    if maap[y][x] == ".": return True, []
    elif maap[y][x] == "#": return False, []
    elif maap[y][x] in "[]":
        co = 1 if maap[y][x] == "[" else -1
        currentCrates = [(x,y,maap[y][x]),(x+co,y,maap[y][x+co])]

        if dx != 0:
            r, c = findCrateBlock(x+co, y, dx, dy, maap)
            return r, c+currentCrates
        
        r0, c0 = findCrateBlock(x, y, dx, dy, maap)
        r1, c1 = findCrateBlock(x+co, y, dx, dy, maap)
        if r0 and r1: return True, c0+c1+currentCrates
        else: return False, []

def t2(data):
    instructions = "".join(data.split("\n\n")[1].split("\n"))
    maap = []
    rx, ry = 0,0
    for i, l in enumerate(data.split("\n\n")[0].split("\n")):
        templ = ""
        for e in l:
            if e in ".#": templ += f"{e}{e}"
            elif e == "O": templ += "[]"
            elif e == "@":
                rx, ry = len(templ), i
                templ += "@."
        maap.append(list(templ))

    for i in instructions:
        dx = 1 if i == ">" else -1 if i == "<" else 0
        dy = 1 if i == "v" else -1 if i == "^" else 0

        if maap[ry+dy][rx+dx] in "[]":
            res, crates = findCrateBlock(rx, ry, dx, dy, maap)
            if not res: continue
            for x, y, c in crates: maap[y][x] = "."
            for x, y, c in crates: maap[y+dy][x+dx] = c
        elif maap[ry+dy][rx+dx] == "#": continue

        maap[ry][rx], maap[ry+dy][rx+dx] = ".", "@"
        rx += dx
        ry += dy
        # print("\n".join([f"\nMove {i}:"]+["".join(l) for l in maap]))
    return sum([sum([y*100 + x for x in range(len(maap[y])) if maap[y][x] == "["]) for y in range(len(maap))])

def getData(): return open("data/" + __file__.split("/")[-1].split(".")[0] + ".txt").read()
if __name__ == "__main__":
    data = getData()
    print(t1(data))
    print(t2(data))