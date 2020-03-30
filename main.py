from argparse import ArgumentParser

from happy_computing import HappyComputing
import sys


def start_simulation(hours,  time_to_run, sellers=2, technicals=3, specialized_technicals=1):
    simulation_gain = HappyComputing(hours, sellers, technicals, specialized_technicals)
    print(f'Average of gain on {time_to_run} day(s) => {simulation_gain.estimated_gain(time_to_run)}')


def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Insert number of days to simulate as params")
        return
    days = int(sys.argv[1])
    print(f"Number of days to simulate {days}")

    start_simulation(8, days)


if __name__ == '__main__':
    main()
