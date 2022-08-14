# -*- conding: utf-8 -*-

# lanuched on 15th Sep in 1977
# on the 25th Aug in 2012 corssed the heliopause
# currently (6th Aug 2021) 22,982,855,000 km from the Sun
# traveling away from the Sun at 16,9995 km/sec

# one-way time for radio communication as 76436 sec
# round-trip time is twice of one-way time
# speed of radio waves 299,792,458 m/sec

import argparse

def round_trip_communication_time(t):
    distance_at_start = 22982855000
    velocity = 169995
    t_year_to_sec = t * 31536000
    distance = distance_at_start + velocity * t
    speed_of_light = 299792458 / 1000
    round_trip_communication_time = 2 * distance / speed_of_light
    return round_trip_communication_time


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t')
    args = parser.parse_args()

    print("rond-trip communication time (sec):", round_trip_communication_time(int(args.t)))


