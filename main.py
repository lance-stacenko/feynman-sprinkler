import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
fluid_density = 1000  # Density of water (kg/m^3)
nozzle_radius = 0.01  # Radius of the sprinkler nozzle (m)
nozzle_count = 3  # Number of nozzles
flow_rate = -0.01  # Flow rate into the sprinkler (negative for suction, m^3/s)
arm_length = 0.1  # Length of each sprinkler arm (m)
sprinkler_mass = 0.5  # Mass of the sprinkler (kg)
friction_coeff = 0.01  # Rotational friction coefficient (N·m·s)

# Torque calculation due to fluid flow
def calculate_torque(angular_velocity):
    flow_velocity = flow_rate / (np.pi * nozzle_radius**2)  # Fluid velocity (m/s)
    force_per_nozzle = fluid_density * flow_velocity**2 * np.pi * nozzle_radius**2
    torque_per_nozzle = arm_length * force_per_nozzle
    total_torque = nozzle_count * torque_per_nozzle
    # Apply frictional torque (opposite to angular velocity)
    friction_torque = -friction_coeff * angular_velocity
    return total_torque + friction_torque

# Equation of motion: d(angular_velocity)/dt = torque / moment_of_inertia
def equation_of_motion(t, y):
    angular_velocity = y[0]
    moment_of_inertia = (1/3) * sprinkler_mass * arm_length**2  # Approximation
    torque = calculate_torque(angular_velocity)
    angular_acceleration = torque / moment_of_inertia
    return [angular_acceleration]

# Solve the system over time
time_span = (0, 10)  # Simulate for 10 seconds
initial_conditions = [0]  # Start with no angular velocity
solution = solve_ivp(equation_of_motion, time_span, initial_conditions, t_eval=np.linspace(0, 10, 100))

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(solution.t, solution.y[0], label="Angular Velocity (rad/s)")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (rad/s)")
plt.title("Feynman Sprinkler Angular Velocity Over Time")
plt.legend()
plt.grid()
plt.show()
