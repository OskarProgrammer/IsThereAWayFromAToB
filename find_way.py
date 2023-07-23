from collections import deque

def isWay(start, end, graph):
    searching = deque()
    searching += graph[start]
    alreadySearched = []

    while searching:
        point = searching.popleft()

        if point not in alreadySearched:
            if point == end:
                return True
            alreadySearched.append(point)
            searching += graph[point]

    return False

graph = {
    "A": ["B","C"],
    "B": ["E", "F"],
    "C": ["F", "B"],
    "E": [],
    "F": ["E"]
}

arg1 = "E"
arg2 = "F"

if isWay(arg1, arg2, graph):
    print(f"Found way from {arg1} to {arg2}")
else:
    print(f"No way from {arg1} to {arg2}")