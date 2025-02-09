class PolyLine:
    def __init__(self, start_coord: tuple, *args):
        self.start_coord = start_coord
        self.other_coords = args
        self.coord_list = list((self.start_coord, ) + self.other_coords)

    def add_coord(self, x, y):
        coords = x, y
        self.coord_list.append(coords)

    def remove_coord(self, indx):
        self.coord_list.pop(indx)

    def get_coords(self):
        return self.coord_list
