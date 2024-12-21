def t1(data):
    drive = []
    id = 0
    for i in range(len(data)):
        if i%2 == 0:
            drive += [id]*int(data[i])
            id += 1
        else: drive += ["."]*int(data[i])
    moving = [(drive[i], i) for i in range(0, len(drive)) if drive[i] != "."][::-1]
    
    for i in range(len(drive)):
        if drive[i] == ".":
            item = moving.pop(0)
            if item[1] < i: break
            drive[i] = item[0]
            drive[item[1]] = "#"

    return sum([int(drive[i])*i for i in range(len(drive)) if drive[i] not in [".", "#"]])

def smallestSpace(index, empty, f):
    for i in range(0, index):
        if empty[i] >= f[1]: return i
    return None

def t2(data):
    files = [(i, int(data[::2][i])) for i in range(len(data[::2]))]
    empty = [int(e) for e in data[1::2]] + [0]

    for f in files[::-1]:
        index = files.index(f)

        space = smallestSpace(index, empty, f)
        if space == None: continue

        empty[space] -= f[1]
        empty[index-1] += empty[index]+f[1]

        empty.pop(index)
        empty.insert(space, 0)

        files.insert(space+1, files.pop(index))
    
    final = [(".", empty.pop(0)) if i%2 else files.pop(0) for i in range(len(files) + len(empty))]

    drive = []
    for f in final: drive += [f[0]]*f[1]
    return sum([f*i for i,f in enumerate(drive) if f != "."])

def getData(): return open("data/" + __file__.split("/")[-1].split(".")[0] + ".txt").read()
if __name__ == "__main__":
    data = getData()
    print(t1(data))
    print(t2(data))