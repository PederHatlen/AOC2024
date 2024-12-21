import re

def t1(data):
    total = 0
    machines = [l.split("\n") for l in data.split("\n\n")]
    for m in machines:
        a = [int(n) for n in re.findall(r"[0-9]+", m[0])]
        b = [int(n) for n in re.findall(r"[0-9]+", m[1])]
        p = [int(n) for n in re.findall(r"[0-9]+", m[2])]

        results = [float("inf")]
        for ac in range(0, max(p[0], p[1])):
            for bc in range(0, max(p[0], p[1])):
                x, y = ac*a[0] + bc*b[0], ac*a[1] + bc*b[1]
                if x > p[0] or y > p[1]: break
                elif [x, y] == p: results += [(ac*3) + bc]
        if min(results) != float("inf"): total += min(results)
    return total

def t2(data):
    total = 0
    machines = [l.split("\n") for l in data.split("\n\n")]
    for m in machines:
        ax, ay = [int(n) for n in re.findall(r"[0-9]+", m[0])]
        bx, by = [int(n) for n in re.findall(r"[0-9]+", m[1])]
        x, y = [int(n) + 10000000000000 for n in re.findall(r"[0-9]+", m[2])]

        bc = (x*ay - y*ax)/(bx*ay - by*ax)
        ac = (x - (bx*bc))/ax

        if ac%1==0 and bc%1==0: total += int((ac*3) + bc)
    return total

def getData(): return open("data/" + __file__.split("/")[-1].split(".")[0] + ".txt").read()
if __name__ == "__main__":
    data = getData()
    print(t1(data))
    print(t2(data))