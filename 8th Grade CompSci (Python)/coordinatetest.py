import random
radius = 5
rangeX = (0, 100)
rangeY = (0, 100)
qty = 50  # or however many points you want

# Generate a set of all points within 200 of the origin, to be used as offsets
# later
deltas = set()
for x in range(-radius, radius+1):
    for y in range(-radius, radius+1):
        if x*x + y*y <= radius*radius:
            deltas.add((x,y))

randPoints = []
excluded = set()
i = 0
while i<qty:
    x = random.randrange(*rangeX)
    y = random.randrange(*rangeY)
    if (x,y) in excluded: continue
    randPoints.append((x,y))
    i += 1
    excluded.update((x+dx, y+dy) for (dx,dy) in deltas)
print (randPoints)
