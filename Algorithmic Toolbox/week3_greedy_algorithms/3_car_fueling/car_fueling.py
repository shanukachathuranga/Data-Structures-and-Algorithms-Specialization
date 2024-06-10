from sys import stdin


def min_refills(distance, tank, stops):
    refillCount = 0
    stops.append(distance)
    numOfStops = len(stops)
    lastFill = 0
    tankLeft = 0
    for i in range(len(stops)-1):
        tankLeft = tank - (stops[i] - lastFill)

        if tank < stops[i+1]-stops[i]:
            return -1
        elif tankLeft < stops[i+1]-stops[i]:
            refillCount += 1
            lastFill = stops[i]


    return refillCount

# def test():
#     print(min_refills(200,250,[100,150]))
#
# test()

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
