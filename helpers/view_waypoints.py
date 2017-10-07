#!/opt/anaconda3/bin/python

import matplotlib.pyplot as plt
import csv
import numpy as np

w_p = np.array([])

def main():
    global w_p
    with open("../data/wp_yaw_const.csv") as wp_csv:
        csv_reader = csv.reader(wp_csv)
        for line in csv_reader:
            x,y,z,yaw = map(float, line)
            w_p = np.append(w_p, x+y*1j)
        print(len(w_p.real))
        print(len(w_p.imag))
        plt.scatter(w_p.real,w_p.imag)
        plt.grid('on')
        plt.show()

def get_closest_waypoint(pose):
    """
    First brute force version
    """
    dist = lambda w : np.linalg.norm((pose[0]+pose[1]*1j)-w)
    get_distance = np.vectorize(dist)

    return np.argmin(get_distance(w_p))


if __name__ == "__main__":
    main()
    print(w_p[get_closest_waypoint((2177.48,1814.41))])


