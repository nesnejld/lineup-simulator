import baseball.data
import baseball.events
import baseball.state

from pybaseball import batting_stats_bref


data = (batting_stats_bref(2023))
for col in data.columns:
    print(col)

player = baseball.data.Hitter(data, 'Lindor')
state = baseball.state.SimpleGameState([player])
eventGenerator = baseball.events.SimpleEventGenerator();
i = 0;
while i < 100:
    event = eventGenerator.generateEvent(state.getCurrentHitter())
    print(event)
    print(state.updateState(event))
    i += 1

print(player.name)
