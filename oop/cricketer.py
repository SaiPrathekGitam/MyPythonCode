class Cricketer:
    def __init__(self, name, country):
        self.name = name
        self.country = country


class Batsman(Cricketer):
    def __init__(self, name, country, runs):
        Cricketer.__init__(self, name, country)
        self.runs = runs

    @property
    def points(self):
        return self.runs

    def get_points(self):
        return self.runs // 100


class Bowler(Cricketer):
    def __init__(self, name, country, wickets):
        Cricketer.__init__(self, name, country)
        self.wickets = wickets

    @property
    def points(self):
        return self.runs

    def get_points(self):
        return self.wickets // 5


class Allrounder(Batsman, Bowler):
    def __init__(self, name, country, runs, wickets):
        Batsman.__init__(self, name, country, runs)
        Bowler.__init__(self, name, country, wickets)

    @property
    def points(self):
        return Batsman.get_points(self) + Bowler.get_points(self)

    def get_points(self):
        return Batsman.get_points(self) + Bowler.get_points(self)


obj = Allrounder("Hardik", "India", 10000, 500)
print(obj.get_points())
print(obj.points)