import baseball.data
from pybaseball import batting_stats_bref


data = (batting_stats_bref(2023))
for col in data.columns:
    print(col)

player = baseball.data.Hitter(data, 'Lindor')
print(player.name)