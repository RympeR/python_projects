with open('stat.txt', 'r') as f:
    y = x = 0
    for data in f.readlines():
        if data.startswith('0'): 
            y += 1
        elif data.startswith('x'):
            x+= 1
    print(f"x {x} y {y}")