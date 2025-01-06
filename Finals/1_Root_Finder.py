import numpy as np
import matplotlib.pyplot as plt

#Function
def f(x):
    return x ** 3 + np.log(x)

#Derivative
def df(x):
    return 3 * x ** 2 + 1 / x

#Bisection Method
def bisection_method(a, b, tol=1e-6, max_iter=100):
    iterations = []
    errors = []
    x_prev = a

    for i in range(max_iter):
        c = (a + b) / 2
        iterations.append(i)
        errors.append(abs(c - x_prev))
        x_prev = c
        if abs(f(c)) < tol:
            return c, iterations, errors
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c, iterations, errors

#Newton-Raphson Method
def newton_raphson(x0, tol=1e-6, max_iter=100):
    iterations = []
    errors = []
    x = x0
    x_prev = x0

    for i in range(max_iter):
        x = x - f(x) / df(x)
        iterations.append(i)
        errors.append(abs(x - x_prev))
        x_prev = x
        if abs(f(x)) < tol:
            return x, iterations, errors
    return x, iterations, errors


#Function Plot
x = np.linspace(0.1, 2, 1000)
y = f(x)
plt.figure(figsize=(15, 5))
plt.subplot(131)
plt.plot(x, y, 'r-', label='f(x)')
plt.grid(True)
plt.legend()
plt.title('f(x) = x³ + ln(x)')
plt.xlabel('x')
plt.ylabel('f(x)')

# A marker for roots
root_nr, iter_nr, err_nr = newton_raphson(1)
plt.plot(root_nr, 0, 'ro', label='Newton Root', markersize=8)

# Add annotations with coordinates
plt.annotate(f'({root_nr:.4f}, 0)',
            (root_nr, 0),
            xytext=(8, -8),
            textcoords='offset points')

#Bisection Method
root_bis, iter_bis, err_bis = bisection_method(0.1, 2)

plt.subplot(132)
plt.semilogy(iter_bis, err_bis, 'g.-', label='Bisection')
plt.grid(True)
plt.legend()
plt.title('Bisection Method Convergence')
plt.xlabel('Iteration')
plt.ylabel('Absolute Error')

#Newton-Raphson Method
root_nr, iter_nr, err_nr = newton_raphson(1.0)

plt.subplot(133)
plt.semilogy(iter_nr, err_nr, 'b.-', label='Newton-Raphson')
plt.grid(True)
plt.legend()
plt.title('Newton-Raphson Method Convergence')
plt.xlabel('Iteration')
plt.ylabel('Absolute Error')

plt.tight_layout()
plt.show()

# Print results and analysis
print(f"Bisection Method:")
print(f"Root: {root_bis:.10f}")
print(f"Number of iterations: {len(iter_bis)}")
print(f"Final error: {err_bis[-1]:.10e}")
print("\nNewton-Raphson Method:")
print(f"Root: {root_nr:.10f}")
print(f"Number of iterations: {len(iter_nr)}")
print(f"Final error: {err_nr[-1]:.10e}")