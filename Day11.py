def t1(data):
    stones = data.split(" ")
    for i in range(25):
        nStones = []
        for s in stones:
            if s == "0": nStones.append("1")
            elif not len(s) % 2:
                half = len(s)//2
                nStones.extend([s[:half], str(int(s[half:]))])
            else: nStones.append(str(int(s)*2024))
        stones = [] + nStones
    return len(stones)

def getTotalPaths(s, paths, depth):
    stones = 0
    if depth <= 0: return 1, paths
    elif s in paths[depth]: return paths[depth][s], paths
    elif s == "0": stones, paths = getTotalPaths("1", paths, depth-1)
    elif not len(s) % 2:
        half = len(s)//2
        stones, paths = getTotalPaths(s[:half], paths, depth-1)
        tmps, paths = getTotalPaths(str(int(s[half:])), paths, depth-1)
        stones += tmps
    else: stones, paths = getTotalPaths(str(int(s)*2024), paths, depth-1)
    
    paths[depth][s] = stones
    return stones, paths

def t2(data):
    stones = data.split(" ")
    iterations = 75

    paths = {n:{} for n in range(iterations+1)}
    total = 0

    for s in stones:
        tmps, paths = getTotalPaths(s, paths, iterations)
        total += tmps
    return total

def getData(): return open("data/" + __file__.split("/")[-1].split(".")[0] + ".txt").read()
if __name__ == "__main__":
    data = getData()
    print(t1(data))
    print(t2(data))