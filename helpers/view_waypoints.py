#!/opt/anaconda3/bin/python

import matplotlib.pyplot as plt
import csv


def main():
    with open("../data/wp_yaw_const.csv") as wp_csv:
        csv_reader = csv.reader(wp_csv)
        x_p = []
        y_p = []
        for line in csv_reader:
            x,y,z,yaw = map(float, line)
            x_p.append(x)
            y_p.append(y)

        plt.scatter(x_p,y_p)
        plt.grid('on')
        plt.show()

if __name__ == "__main__":
    main()


