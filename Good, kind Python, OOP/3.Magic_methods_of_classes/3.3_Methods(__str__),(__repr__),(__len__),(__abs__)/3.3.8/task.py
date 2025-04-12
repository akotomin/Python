class Clock:
    def __init__(self, hours, minutes, seconds):
        if self.check_time(hours) and self.check_time(minutes) and self.check_time(seconds):
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    @staticmethod
    def check_time(value):
        return isinstance(value, int) and value >= 0

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock):
        self.clock1 = clock1
        self.clock2 = clock2

    def __len__(self):
        if self.clock1.get_time() - self.clock2.get_time() < 0:
            return 0
        return self.clock1.get_time() - self.clock2.get_time()

    def __str__(self):
        diff = len(self)
        hours = diff // 3600
        minutes = diff % 3600 // 60
        seconds = diff % 3600 % 60
        return f"{hours:02}: {minutes:02}: {seconds:02}"


dt = DeltaClock(Clock(2, 45, 0), Clock(3, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)