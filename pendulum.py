#Credit to 3blue1brown!!
import numpy as np
import matplotlib.pyplot as plt
import sys

#Constants
g = 9.8
L = 2
mu = 0.1
theta_0 = np.pi /3
theta_dot_0 = 0
x = []
y = []

#Defining the ODE
def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g/L) * np.sin(theta)

def theta(t):
    theta = theta_0
    theta_dot = theta_dot_0
    delta_t = 0.01
    z = 0
    for time in range(0, int(t / delta_t)):
        theta_double_dot = get_theta_double_dot(theta, theta_dot)
        theta += theta_dot * delta_t
        x.append(theta)
        theta_dot += theta_double_dot * delta_t
        y.append(theta_dot)
        z+=1
    return theta

try:
   a = int(input("Please enter the amount of turns: "))
except ValueError:
   print("\nPlease only use integers")
theta(a)
fig, ax = plt.subplots(figsize=(19.2,10.8))
ax.plot(x, y)
ax.set_xlabel('angular displacement')
ax.set_ylabel('angular velocity')
ax.set_title('ODE computing pendulum motion considering air resistance')
fig.set_facecolor('lightsteelblue')
plt.savefig('ODE.png')
