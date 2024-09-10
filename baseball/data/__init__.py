class Player:
    def __init__(self):
        pass

class Hitter(Player):
    def __init__(self, data, playerName):
        super().__init__()
        player = data[data.Name.str.contains(playerName)].iloc[0]
        self.name = player.Name
        self.singles = player.H - player['2B'] - player['3B'] - player.HR

        self.single_perc = self.singles / player.PA
        self.double_perc = player['2B'] / player.PA
        self.triple_perc = player['3B'] / player.PA
        self.hr_perc = player.HR / player.PA
        self.so_perc = player.SO / player.PA
        self.bb_perc = player.BB / player.PA
        self.all_other_outs_perc = 1 - (self.single_perc + self.double_perc + self.triple_perc + self.hr_perc + self.so_perc + self.bb_perc)

