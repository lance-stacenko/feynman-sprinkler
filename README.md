# Feynman Sprinkler Simulation

## Overview
This project simulates the behavior of the Feynman sprinkler, a classical physics problem that explores the motion of a sprinkler when water is sucked inward rather than expelled outward. The project demonstrates key principles of fluid dynamics and mechanics and provides a numerical solution to analyze the sprinkler's angular velocity over time.

## Features
- Numerical simulation of the Feynman sprinkler using Python.
- Visualization of the sprinkler's angular velocity over time.
- Modular structure for extending the simulation to 3D models or adding more complex fluid dynamics (e.g., turbulence).
- Easy-to-run Python script with detailed outputs.

## Project Structure
```plaintext
feynman_sprinkler_project/
|
├── main.py                 # Main script for running the simulation
├── requirements.txt        # Python dependencies for the project
├── README.md               # Project documentation
|
├── src/                    # Source code directory
│   ├── simulation.py       # Core simulation logic
│   ├── plotting.py         # Visualization functions
│   ├── utils.py            # Utility functions for calculations
|
├── data/                   # Input and output data
│   ├── inputs/             # Placeholder for input files (if needed)
│   ├── outputs/            # Directory for generated simulation results
|
├── figures/                # Directory for saved plots and figures
│   ├── angular_velocity.png  # Example output of the simulation
|
├── tests/                  # Unit tests for code validation
│   ├── test_simulation.py  # Unit tests for simulation module
│   ├── test_plotting.py    # Unit tests for plotting functions
|
└── docs/                   # Documentation and references
    ├── theory.md           # Notes on the physics of the Feynman sprinkler
    └── references.md       # Links to related papers and resources
```

## How It Works
1. **Torque Calculation**:
   - The torque on the sprinkler is calculated based on the flow of water through the nozzles and the length of the sprinkler arms.
   - Frictional forces are included to simulate real-world conditions.

2. **Numerical Integration**:
   - The equations of motion are solved numerically using Python's `scipy.integrate.solve_ivp`.

3. **Visualization**:
   - Results are plotted to show the angular velocity of the sprinkler over time.

## Requirements
- Python 3.8 or later
- Required Python libraries:
  - `numpy`
  - `matplotlib`
  - `scipy`

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/feynman_sprinkler_project.git
   cd feynman_sprinkler_project
   ```

2. Run the simulation:
   ```bash
   python main.py
   ```

3. View the results:
   - The simulation will generate a plot of angular velocity over time.
   - Plots will be saved in the `figures/` directory.

## Physics Behind the Feynman Sprinkler
The Feynman sprinkler problem examines whether the sprinkler rotates in the opposite direction when water is sucked inward. Key principles include:
- Conservation of momentum.
- Interaction between fluid flow and mechanical forces.
- The role of friction and external asymmetries in real-world setups.

## Extending the Project
- **3D Modeling:** Add 3D geometry for a more realistic sprinkler simulation.
- **Advanced Fluid Dynamics:** Incorporate turbulence and pressure variations using computational fluid dynamics (CFD) tools.
- **Experimental Validation:** Compare simulation results with data from physical experiments.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## References
- [Feynman's Original Experiment](https://en.wikipedia.org/wiki/Feynman_sprinkler)
- [Navier-Stokes Equations Overview](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations)

---

Feel free to contribute or suggest improvements to this project!


