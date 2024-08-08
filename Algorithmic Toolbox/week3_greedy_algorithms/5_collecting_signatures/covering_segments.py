from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort(key=lambda x: x[1])

    # Initialize an empty list to store points
    points = []

    # Iterate through the sorted segments
    for segment in segments:
        # If the current segment is not covered by the last point, add a new point
        if not points or points[-1] < segment[0]:
            points.append(segment[1])

    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
