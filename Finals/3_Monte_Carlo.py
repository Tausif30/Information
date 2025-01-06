import numpy as np
import matplotlib.pyplot as plt

def sampling(x, y):
    # Point must be below both quarter circles
    left_circle = (x-0) ** 2 + (y-0) ** 2 <= 1
    right_circle = (x-1) ** 2 + (y-0) ** 2 <= 1
    return left_circle and right_circle

def monte_carlo_estimation(n=10000):
    # Generate random points
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)
    points_inside = sum(sampling(x[i], y[i]) for i in range(n))
    estimated_area = points_inside / n
    return estimated_area

def visualize_simulation(n=10000):
    # Generate random points
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)
    inside = [sampling(x[i], y[i]) for i in range(n)]
    plt.figure(figsize=(10, 10))
    plt.scatter(x[~np.array(inside)], y[~np.array(inside)],
               c='red', alpha=0.6, label='Outside')
    plt.scatter(x[np.array(inside)], y[np.array(inside)],
               c='green', alpha=0.6, label='Inside')
    theta = np.linspace(0, np.pi/2, 100)
    plt.plot(np.cos(theta), np.sin(theta), 'b-')
    plt.plot(1 + np.cos(theta+np.pi/2), np.sin(theta+np.pi/2), 'b-')
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.title('Monte Carlo Simulation')
    plt.show()

#Monte Carlo Estimation
n_simulations = 5
results = []
for i in range(n_simulations):
    area = monte_carlo_estimation()
    results.append(area)

# Area =   (√3/4) + 2*(π/6 - √3/4) = π/3 - √3/4
exact_area = np.pi/3 - np.sqrt(3)/4

#Results
print(f"\nMonte Carlo Estimation Results:")
print(f"Average estimated area: {np.mean(results):.6f}")
print(f"Exact area (π/3 - √3/4): {exact_area:.6f}")
print(f"Relative error: {abs(np.mean(results) - exact_area)/exact_area * 100:.4f}%")
print("\n")
# Visualize simulation
visualize_simulation()