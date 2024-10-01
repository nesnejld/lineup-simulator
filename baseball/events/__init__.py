import numpy as np


class SimpleEventGenerator:
    events = ["so",
              "single",
              "double",
              "triple",
              "hr",
              "bb",
              "all_other_outs"
              ]

    def __init__(self):
        pass

    def generateEvent(self, currentHitter):
        self.event = np.random.choice(
            a=[0, 1, 2, 3, 4, 5, 6],
            size=1,
            p=[currentHitter.so_perc,
                currentHitter.single_perc,
                currentHitter.double_perc,
                currentHitter.triple_perc,
                currentHitter.hr_perc,
                currentHitter.bb_perc,
                currentHitter.all_other_outs_perc]
        )[0]
        return self.event

    def __str__(self):
        return f"""{self.events[self.event]}: {self.event}"""
