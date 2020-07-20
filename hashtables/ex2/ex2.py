#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    storage = {}
    route = []
    reconstructing = True
    location = "NONE"

    for t in tickets:
        storage[t.source] = t.destination

    while reconstructing:
        if storage[location] == "NONE":
            reconstructing = False
        route.append(storage[location])
        location = storage[location]

    return route
