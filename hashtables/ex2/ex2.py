#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route_dict = {}
    route = []

    for ticket in tickets:
        route_dict[ticket.source] = ticket.destination

    source = "NONE"
    dest = ""
    while dest != "NONE":
        dest = route_dict[source]
        route.append(dest)
        source = dest

    return route