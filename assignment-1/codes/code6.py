import numpy as np
import matplotlib.pyplot as plt

def lissajous_curve(A, B, omega_x, omega_y, delta_y,delta_x, t_max=2*np.pi, num_points=1000):
    t = np.linspace(0, t_max, num_points)
    y = A * np.sin(omega_y * t + delta_y) #ch1
    x = B * np.sin(omega_x * t + delta_x) #ch2
    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.xlabel('x(t)')
    plt.ylabel('y(t)')
    plt.title('Lissajous Figure')
    plt.grid(True)
    plt.axis('equal')
    plt.savefig('../figs/fig6_verify.png')
    plt.show()

# Example: A = 1, B = 1, omega_x = 3, omega_y = 2, delta = pi/2
lissajous_curve(A=5, B=5, omega_y=2*np.pi, omega_x=2*np.pi, delta_y=0,delta_x=0)
