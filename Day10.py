def searchForPath(x, y, topo):
    val = topo[y][x]
    trailheads = []
    if val == 9: return [(x,y)]

    if x > 0 and topo[y][x-1] == val+1: trailheads += searchForPath(x-1, y, topo)
    if x < len(topo[y])-1 and topo[y][x+1] == val+1: trailheads += searchForPath(x+1, y, topo)
    if y > 0 and topo[y-1][x] == val+1: trailheads += searchForPath(x, y-1, topo)
    if y < len(topo)-1 and topo[y+1][x] == val+1: trailheads += searchForPath(x, y+1, topo)
    return trailheads

def t1(data):
    m = data.split("\n")
    topo, heads = [], []
    for y in range(len(m)):
        tmp = []
        for x in range(len(m[0])):
            if m[y][x] == "0": heads.append((x, y))
            tmp.append(int(m[y][x]))
        topo.append(tmp)
    
    trailheads = []
    for x,y in heads:
        sumits = searchForPath(x, y, topo)
        print(sumits)
        trailheads.append(len(set(sumits)))
    print(trailheads)
    return sum(trailheads)

def t2(data):
    m = data.split("\n")
    topo, heads = [], []
    for y in range(len(m)):
        tmp = []
        for x in range(len(m[0])):
            if m[y][x] == "0": heads.append((x, y))
            tmp.append(int(m[y][x]))
        topo.append(tmp)
    
    trailheads = []
    for x,y in heads:
        sumits = searchForPath(x, y, topo)
        print(sumits)
        trailheads.append(len(sumits))
    print(trailheads)
    return sum(trailheads)

def getData(): return open("data/" + __file__.split("/")[-1].split(".")[0] + ".txt").read()
if __name__ == "__main__":
    data = getData()
    print(t1(data))
    print(t2(data))