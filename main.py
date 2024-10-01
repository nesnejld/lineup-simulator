#!/usr/bin/env python
import baseball.data
import baseball.events
import baseball.state
import numpy as np
import logging
import sys
from pybaseball import batting_stats_bref
from baseballref import BaseballReference

# urlprefix = 'https://www.baseball-reference.com';
# urlpattern = "/leagues/daily.cgi?user_team=&bust_cache=&type={type}&lastndays=7&dates=fromandto&fromandto={start_dt}.{end_dt}&level={level}&franch={franch}&stat=&stat_value=0";
# csvfile = None
# debug = False

args = {"franch": 'ANY',
        "level": 'mlb',
        "end_dt": '2023-11-30',
        "start_dt": '2023-03-01',
        "type": 'b'
        }
options = {
    "debug": True
}
bref = BaseballReference(**options)
df = bref.getdataframe(args)
parameters = bref.getAllOptions()
df.to_pickle("test.pkl")
df.to_csv("test.csv")
myformat = '%(asctime)s %(levelname)s:%(name)s %(lineno)d :%(message)s'
# logging.basicConfig(filename='/tmp/test.log',
#                     level=logging.WARN, format=format)
logging.basicConfig(stream=sys.stderr,
                    level=logging.WARN, format=myformat)
logger = logging.getLogger('lineup-simulator.main')
data = (batting_stats_bref(2023))
for col in data.columns:
    logger.info(col)

eventGenerator = baseball.events.SimpleEventGenerator()


def runsimulations(players, nsimulations=1000):
    i = 0
    scores = []
    for i in range(1, nsimulations+1):
        if i % 100 == 0:
            logger.info(i)
        state = baseball.state.SimpleGameState(players)
        while not state.gameover():
            event = eventGenerator.generateEvent(state.getCurrentHitter())
            logger.info(eventGenerator)
            logger.info(state.updateState(event))
        scores.append(state.score)

    # logger.warning(player.name)
    logger.warning(np.sum(scores))
    logger.warning(np.average(scores))
    logger.warning(np.std(scores))

lineup=['Robert Jr.', 'Nimmo']

# lineup = ['Lindor', 'Casas']
for player in lineup:
  logger.warning(f"==============={player}")
  runsimulations([baseball.data.Hitter(data, player)])
lineup = ['Lindor', 'Lindor', 'Lindor', 'Casas',
          'Lindor', 'Lindor', 'Lindor', 'Lindor', 'Lindor']
logger.warning("===============Running lineup")
logger.warning(lineup)
players = list(map(lambda p: baseball.data.Hitter(data, p), lineup))
runsimulations(players, nsimulations=10000)
pass
