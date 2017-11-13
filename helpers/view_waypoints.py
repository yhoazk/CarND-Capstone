#!/opt/anaconda3/bin/python
"""
Helper functions to show map, other utilities and TOCs
"""
import csv
import matplotlib.pyplot as plt
import numpy as np

w_p = np.array([])
dist = lambda w: np.linalg.norm((pose[0]+pose[1]*1j)-w)
# points to translate
t_x, t_y = 909.48,1128.67

translated_x = []
translated_y = []
translated_w = []
def main():
    """
    Get all the points into an array, and show them
    """
    global w_p
    #with open("../data/wp_yaw_const.csv") as wp_csv:
    with open("../data/churchlot_with_cars.csv") as wp_csv:
        csv_reader = csv.reader(wp_csv)
        for line in csv_reader:
            x_p, y_p, _z, _yaw, _ = map(float, line)
            translated_x.append(x_p + t_x)
            translated_y.append(y_p + t_y)
            translated_w.append(_yaw)
            w_p = np.append(w_p, complex(x_p, y_p))
        print(len(w_p.real))
        print(len(w_p.imag))
        #plt.scatter(w_p.real, w_p.imag)
        plt.scatter(translated_x, translated_y)

        for x,y,w in zip(translated_x, translated_y, translated_w):
            print("%1.3f, %1.3f, %1.3f, %1.3f" % (x,y,0,w))

        plt.grid('on')
        plt.show()

def get_closest_waypoint(pose):
    """
    First brute force version
    """

    get_distance = np.vectorize(dist)

    return np.argmin(get_distance(w_p))


if __name__ == "__main__":
    main()
    print(w_p[get_closest_waypoint((2177.48, 1814.41))])
