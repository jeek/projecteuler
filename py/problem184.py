radius = 105

def dot(i, j):
    return i[0] * j[0] + i[1] * j[1]

def area(A, B, C):
    a = ((C[1] - B[1]) ** 2 + (C[0] - B[0]) ** 2) ** .5
    b = ((A[1] - B[1]) ** 2 + (A[0] - B[0]) ** 2) ** .5
    c = ((C[1] - A[1]) ** 2 + (C[0] - A[0]) ** 2) ** .5
    s = (a + b + c) / 2.0
    area = (s * (s - a) * (s - b) * (s - c))
    if area > 1:
        return area ** .5
    return 0


def inside(P, A, B, C):
    v0 = (C[0] - A[0], C[1] - A[1])
    v1 = (B[0] - A[0], B[1] - A[1])
    v2 = (P[0] - A[0], P[1] - A[1])
    dot00 = dot(v0, v0)
    dot01 = dot(v0, v1)
    dot02 = dot(v0, v2)
    dot11 = dot(v1, v1)
    dot12 = dot(v1, v2)
    
    invdenom = 1.0 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invdenom
    v = (dot00 * dot12 - dot01 * dot02) * invdenom
    
    return (u > 0.01) and (v > 0.01) and (u + v < 1)

points = []
for i in range(-radius, radius + 1):
    for j in range(-radius, radius + 1):
#        if (i ** 2 + j ** 2) ** .5 < radius and not(i == 0 and j == 0):
        if (i ** 2 + j ** 2) ** .5 < radius:
            points.append((i,j))
print len(points)
quit()
count = 0
for a in range(0, len(points)):
    for b in range(a + 1, len(points)):
        for c in range(b + 1, len(points)):
#            print points[a], points[b], points[c], area(points[a], points[b], points[c])
            if area(points[a], points[b], points[c]) >= 0.5 and inside((0,0), points[a], points[b], points[c]):
                print points[a],points[b],points[c],
                count += 1
                print count