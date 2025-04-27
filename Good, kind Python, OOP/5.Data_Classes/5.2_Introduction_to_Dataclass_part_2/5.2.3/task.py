from dataclasses import dataclass, field

# здесь продолжайте программу
@dataclass
class PolyLine:
    width: float = field(compare=False)
    color: int = field(compare=False, default=0)
    points: list = field(default_factory=lambda: [(0, 0)])


pl1 = PolyLine(0.5, 0)
pl2 = PolyLine(1.5, 2)
pl1.points.extend([(10, -5), (12, 1)])
pl2.points.extend([(10, -5), (12, 1)])
res = pl1 == pl2