import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.cluster import KMeans

# Field parameters
field_length = 10
field_width = 10
n_robots = 5  # Number of robots

# Step 1: Generate random initial positions for robots
def generate_random_robot_positions(n_robots, field_length, field_width):
    return np.random.rand(n_robots, 2) * [field_width, field_length]

# Step 2: Apply K-Means clustering for sector division
def divide_field_with_kmeans(robot_positions, n_robots):
    kmeans = KMeans(n_clusters=n_robots, random_state=42).fit(robot_positions)
    clusters = kmeans.cluster_centers_  # Cluster centers are the target points
    labels = kmeans.labels_             # Labels for each robot's cluster
    return clusters, labels

# Step 3: Motion planning to move robots to their cluster centers and inspect within the cluster
def motion_plan(robot_positions, cluster_centers, labels, steps=100):
    paths = [[] for _ in range(n_robots)]
    velocities = np.zeros((n_robots, 2))  # Velocity for each robot

    for t in range(steps):
        for i in range(n_robots):
            x, y = robot_positions[i]
            # Move towards the center of the assigned cluster
            target = cluster_centers[labels[i]]
            direction = target - robot_positions[i]
            distance = np.linalg.norm(direction)

            # Simple proportional controller to move towards the target
            speed = min(0.1, distance)
            if distance > 0:
                velocities[i] = (direction / distance) * speed

            # Update position based on velocity, avoiding collisions
            new_position = robot_positions[i] + velocities[i]

            # Check for collisions and adjust position to avoid overlaps
            for j in range(n_robots):
                if i != j and np.linalg.norm(new_position - robot_positions[j]) < 0.2:
                    # If a collision is detected, modify the position slightly
                    new_position += np.random.rand(2) * 0.1 - 0.05

            robot_positions[i] = new_position
            paths[i].append(list(robot_positions[i]))

    return paths

# Step 4: Visualization using matplotlib
def visualize_motion(paths, clusters, robot_positions):
    fig, ax = plt.subplots()
    ax.set_xlim(0, field_width)
    ax.set_ylim(0, field_length)

    robots = [plt.plot([], [], 'ro')[0] for _ in range(n_robots)]
    lines = [plt.plot([], [], 'g')[0] for _ in range(n_robots)]

    # Plot the cluster centers (targets)
    for cluster in clusters:
        ax.plot(cluster[0], cluster[1], 'bo', markersize=10, label='Cluster center')

    def init():
        for i, robot in enumerate(robots):
            robot.set_data([], [])
            lines[i].set_data([], [])
        return robots + lines

    def update(frame):
        for i, robot in enumerate(robots):
            x, y = paths[i][frame]
            robot.set_data(x, y)
            line_x = [p[0] for p in paths[i][:frame+1]]
            line_y = [p[1] for p in paths[i][:frame+1]]
            lines[i].set_data(line_x, line_y)
        return robots + lines

    ani = FuncAnimation(fig, update, frames=len(paths[0]), init_func=init, blit=True, interval=100)
    plt.show()

# Main execution
robot_positions = generate_random_robot_positions(n_robots, field_length, field_width)
cluster_centers, labels = divide_field_with_kmeans(robot_positions, n_robots)
paths = motion_plan(robot_positions, cluster_centers, labels)
visualize_motion(paths, cluster_centers, robot_positions)
