class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.lines = []
        self.__length = 0

    def add_track(self, tr):
        s_x = self.lines[-1].to_x if self.lines else self.start_x
        s_y = self.lines[-1].to_y if self.lines else self.start_y
        self.__length += ((s_x - tr.to_x) ** 2 + (s_y - tr.to_y) ** 2) ** 0.5
        self.lines.append(tr)

    def get_tracks(self):
        return self.lines

    def __len__(self):
        return int(self.__length)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = (track1 == track2)