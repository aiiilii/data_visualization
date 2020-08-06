import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    # Default size.
    fig, ax = plt.subplots()
    # Size to fill the screen.
    fig, ax = plt.subplots(figsize=(15,9))
     # 0 to 4999
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='None', s=1)

    # Emphasize the first and last points.
    # after the whole list scatters to display on top of the walk.
    ax.scatter(0, 0, c='green', edgecolors='None', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='None', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break