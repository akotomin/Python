class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1
        v1.links.append(self)
        v2.links.append(self)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        for existing_link in self._links:
            if (existing_link.v1 == link.v1 and existing_link.v2 == link.v2) or \
                    (existing_link.v1 == link.v2 and existing_link.v2 == link.v1):
                return
        self._links.append(link)
        self.add_vertex(link.v1)
        self.add_vertex(link.v2)

    def find_path(self, start_v, stop_v):
        self._start_v = start_v
        self._stop_v = stop_v
        self._best_path = None
        self._best_links = None
        self._min_dist = float('inf')

        self._find_path(start_v, [start_v], [], 0)

        return (self._best_path, self._best_links)

    def _find_path(self, current_v, path, links, current_dist):
        if current_v == self._stop_v:
            if current_dist < self._min_dist:
                self._min_dist = current_dist
                self._best_path = path.copy()
                self._best_links = links.copy()
            return

        for link in current_v.links:
            next_v = link.v2 if link.v1 == current_v else link.v1
            if next_v not in path:
                path.append(next_v)
                links.append(link)
                self._find_path(next_v, path, links, current_dist + link.dist)
                path.pop()
                links.pop()


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self.dist = dist
