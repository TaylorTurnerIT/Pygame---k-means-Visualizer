### k-means-Visualizer

## Overview
The k-Means Visualizer is a Python program that visually demonstrates the k-means clustering algorithm using Pygame and NumPy. It creates a graphical representation of data points and clusters, offering a clear and intuitive understanding of how k-means clustering works.

## Features
- **Dynamic Data Generation:** Generates data points and clusters dynamically in a 2D space.
- **Anomaly Generation:** Option to include anomalous data points outside of the normal clusters.
- **Interactive Visualization:** Users can interact with the visualization through keyboard commands.
- **Performance Metrics:** Tracks and displays data generation time for performance analysis.

## Requirements
- Python 3.x
- Pygame
- NumPy

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install Pygame and NumPy using pip:
   ```bash
   pip install pygame numpy
   ```
3. Clone or download this repository to your local machine.

## Usage
Run the script using Python:
```bash
python k_means_visualizer.py
```

### Controls
- **ESC:** Exit the program.
- **G:** Toggle grid visibility.
- **1:** Regenerate the data set.

## Classes and Functions
- **Point:** Represents individual data points in the visualization.
- **DataCreator:** Handles the generation and management of data points and clusters.

## How it Works
1. **Initialization:** Initializes Pygame and screen settings.
2. **Data Generation:** Generates clusters and data points within those clusters, with options for anomalies.
3. **Visualization:** Draws and updates the visualization based on user interactions.
4. **Interaction:** Allows users to regenerate data and toggle grid visibility.

## Contributing
Contributions to improve k-Means Visualizer are welcome. Please ensure to follow the best practices for Python and Pygame development.

## License
This project is open source and available under the [MIT License](LICENSE.md).

---

*This README is a guide to the k-Means Visualizer and provides instructions on installation, usage, and contribution. For more detailed documentation, please refer to the source code.*
