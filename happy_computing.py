from distributions import exponential, normal, poisson, select_random_type
from queue import Queue
import math


class HappyComputing:
    def __init__(self, hours, sellers=2, technicals=3, specialized_technicals=1):
        self.journal_duration = hours * 60
        self.sellers = sellers
        self.technicals = technicals
        self.specialized_technicals = specialized_technicals

    def simulate(self):
        gain = 0

        # [True] * self.technicals
        free_sellers = [0] * self.sellers
        free_technical = [0] * self.technicals
        free_specialized_technicals = [0] * self.specialized_technicals

        customers_waiting_sellers = Queue()
        customers_waiting_technicals = Queue()
        customers_waiting_specialized_technicals = Queue()

        client_time = 0

        for _ in range(self.journal_duration):
            # Update client reach time
            if client_time > 0:
                client_time -= 1
            else:
                client_time = poisson(20)
                customers_waiting_sellers.put(select_random_type())
            if (customers_waiting_sellers.empty() and
                    customers_waiting_specialized_technicals.empty()
                    and customers_waiting_technicals.empty()):
                for i in range(len(free_sellers)):
                    free_sellers[i] = free_sellers[i] - 1 if free_sellers[i] > 0 else 0
                for i in range(len(free_technical)):
                    free_technical[i] = free_technical[i] - 1 if free_technical[i] > 0 else 0
                for i in range(len(free_specialized_technicals)):
                    free_specialized_technicals[i] = free_specialized_technicals[i] - 1 \
                        if free_specialized_technicals[i] > 0 else 0
                continue

            # Update specialized technicals details
            for i in range(len(free_specialized_technicals)):
                free_specialized_technicals[i] = free_specialized_technicals[i] - 1 \
                    if free_specialized_technicals[i] > 0 else 0

            if not customers_waiting_specialized_technicals.empty():
                for i in range(len(free_specialized_technicals)):
                    if free_specialized_technicals[i] == 0:
                        _ = customers_waiting_specialized_technicals.get()
                        free_specialized_technicals[i] = int(exponential(15))
                        gain += 500
                        if customers_waiting_specialized_technicals.empty():
                            break

            # Update technicals details
            for i in range(len(free_technical)):
                free_technical[i] = free_technical[i] - 1 if free_technical[i] > 0 else 0

            if not customers_waiting_technicals.empty():
                for i in range(len(free_technical)):
                    if free_technical[i] == 0:
                        client_type = customers_waiting_technicals.get()
                        free_technical[i] = int(exponential(20))
                        gain += 0 if client_type == 1 else 350
                        if customers_waiting_technicals.empty():
                            break
                else:
                    for i in range(len(free_specialized_technicals)):
                        if free_specialized_technicals[i] == 0:
                            client_type = customers_waiting_technicals.get()
                            free_specialized_technicals[i] = int(exponential(15))
                            gain += 0 if client_type == 1 else 350
                            if customers_waiting_technicals.empty():
                                break

            # Update sellers details
            for i in range(len(free_sellers)):
                free_sellers[i] = free_sellers[i] - 1 if free_sellers[i] > 0 else 0

            if not customers_waiting_sellers.empty():
                for i in range(len(free_sellers)):
                    if free_sellers[i] == 0:
                        client_type = customers_waiting_sellers.get()
                        free_sellers[i] = int(normal(5, 2))
                        if client_type == 4:
                            gain += 750
                        else:
                            if client_type == 1 or client_type == 2:
                                customers_waiting_technicals.put(client_type)
                            else:
                                customers_waiting_specialized_technicals.put(client_type)
                        if customers_waiting_sellers.empty():
                            break

        return gain

    def estimated_gain(self, time_to_run):
        return sum([self.simulate() for _ in range(time_to_run)]) / time_to_run
