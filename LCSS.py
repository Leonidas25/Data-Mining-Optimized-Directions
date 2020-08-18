import haversine


def LCSS(x, y):

    m = len(x)+1
    n = len(y)+1

    C = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m):
        for j in range(1, n):

            dx = [x[i-1][1], x[i-1][2]]
            dy = [y[j-1][1], y[j-1][2]]

            distance = (haversine.haversine(dx, dy)) * 1000

            if distance <= 200:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])

    return C[m-1][n-1]


def LCSS_Trajectory(x, y):

    result = []

    m = len(x)+1
    n = len(y)+1

    C = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m):
        for j in range(1, n):

            dx = [x[i-1][1], x[i-1][2]]
            dy = [y[j-1][1], y[j-1][2]]

            distance = (haversine.haversine(dx, dy)) * 1000

            if distance <= 200:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])

    index = C[m-1][n-1]
    i = m-1
    j = n-1

    while i > 0 or j > 0:

        if i > 0 and C[i-1][j] == index:
            index = C[i-1][j]
            i = i-1
        elif j > 0 and C[i][j-1] == index:
            index = C[i][j-1]
            j = j - 1
        else:
            result.append([y[j-1][1], y[j-1][2]])
            index = C[i-1][j-1]
            i = i-1
            j = j-1

    return result
