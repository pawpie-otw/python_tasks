from plane2d import Plane2D
import numpy as np
from point import Point
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # generate sample data
    rand_coord = np.random.rand(20, 2)*20

    # create instance of main class
    plane2d = Plane2D([Point(*args)
                       for args in rand_coord])

    # calculate the correct order and total distance
    order, length = plane2d.polygonal_chain()

    # visualization of results using plt
    plt.plot(rand_coord[order, 0], rand_coord[order, 1])
    plt.scatter(rand_coord[order, 0], rand_coord[order, 1], c='r', marker='.')
    plt.title(f"length of the polygonal chain {length:.2f}")

    for p, o in zip(rand_coord[order], range(20)):
        plt.text(p[0], p[1], str(o+1))

    plt.show()
