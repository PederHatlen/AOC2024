import re

def t1(data):
    mx, my = 101, 103
    map = [[0 for _ in range(mx)] for _ in range(my)]
    for robot in data.split("\n"):
        x, y, vx, vy = [int(n) for n in re.findall(r"-*[0-9]+", robot)]
        fx, fy = (x + (vx*100))%mx, (y + (vy*100))%my

        map[fy][fx] += 1

    # print("\n".join(["".join([str(s) for s in l]) for l in map]))
    t = 1
    t *= sum([sum(l[:(len(l)//2)]) for l in map[:(len(map)//2)]])
    t *= sum([sum(l[(len(l)//2)+1:]) for l in map[:(len(map)//2)]])
    t *= sum([sum(l[:(len(l)//2)]) for l in map[(len(map)//2)+1:]])
    t *= sum([sum(l[(len(l)//2)+1:]) for l in map[(len(map)//2)+1:]])
    return t

def t2_fun(data):
    mx, my = 101, 103
    robots = [[int(n) for n in re.findall(r"-*[0-9]+", robot)] for robot in data.split("\n")]

    isTree, s = False, 28
    while not isTree:
        s += 103
        map = [[0 for _ in range(mx)] for _ in range(my)]
        for x, y, vx, vy in robots:
            fx, fy = (x + (vx*s))%mx, (y + (vy*s))%my
            map[fy][fx] += 1
        
        print("\n".join(["".join(["#" if s != 0 else " " for s in l]) for l in map]))
        isTree = input(f"Does this look like a christmas tree? (y/n) (seconds: {s}): ") == "y"
    
    return s

def t2(data):
    mx, my = 101, 103
    robots = [[int(n) for n in re.findall(r"-*[0-9]+", robot)] for robot in data.split("\n")]

    isTree, s = False, 0
    while not isTree:
        s += 1
        map = [[0 for _ in range(mx)] for _ in range(my)]
        for x, y, vx, vy in robots:
            fx, fy = (x + (vx*s))%mx, (y + (vy*s))%my
            map[fy][fx] += 1
        candidate = "\n".join(["".join(["#" if s != 0 else " " for s in l]) for l in map])
        if re.search(r"#{10}", candidate):
            isTree = True
            print(candidate)
    return s

def getData(): return open("data/" + __file__.split("/")[-1].split(".")[0] + ".txt").read()
if __name__ == "__main__":
    data = getData()
    print(t1(data))
    print(t2(data))