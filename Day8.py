def t2(data):
    m = [list(l) for l in data.split("\n")]
    antennas = {}
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == ".": continue
            if m[y][x] not in antennas: antennas[m[y][x]] = []
            antennas[m[y][x]].append((x,y))

    antinodes = set()

    for t in antennas.keys():
        antinodes.update(antennas[t])
        for a0 in antennas[t]:
            for a1 in antennas[t][antennas[t].index(a0)+1:]:
                dx = a1[0] - a0[0]
                dy = a1[1] - a0[1]

                x, y = (a0)
                i = 0
                while 0 <= x-(dx*i) < len(m[0]) and 0 <= y-(dy*i) < len(m):
                    antinodes.add((x-(dx*i), y-(dy*i)))
                    i+=1
                
                i = 0
                while 0 <= x+(dx*i) < len(m[0]) and 0 <= y+(dy*i) < len(m):
                    antinodes.add((x+(dx*i), y+(dy*i)))
                    i+=1
    for n in antinodes:
        if m[n[1]][n[0]] == ".":
            m[n[1]][n[0]] = "#"

    print("\n".join(["".join(l) for l in m]))
    return len(antinodes)


def getData(): return open("data/" + __file__.split("/")[-1].split(".")[0] + ".txt").read()
if __name__ == "__main__":
    data = getData()
    print(t2(data))