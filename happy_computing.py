from distributions import exponential, normal, poisson, select_type
from queue import Queue
import math


class HappyComputing:
    def __init__(self, hours, sellers=2, technicals=3, specialized_technicals=1):
        self.journal_duration = hours * 60
        self.sellers = sellers
        self.technicals = technicals
        self.specialized_technicals = specialized_technicals

    def simulate(self):
        pass

    def estimated_gain(self, time_to_run):
        pass
