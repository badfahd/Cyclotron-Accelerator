# 🌀 3D Cyclotron Accelerator Simulation

An interactive 3D particle accelerator simulation built using **Python** and **VPython**. This project models the fundamental physics of a classical cyclotron—visualizing how charged particles gain energy through an alternating electric field while being guided into expanding circular orbits by a uniform magnetic field, culminating in beam extraction toward a target.

---

## 📚 Physics Theory & Working Principles

A cyclotron is a type of particle accelerator invented by Ernest Lawrence and M. Stanley Livingston. It accelerates charged particles outward from the center along a spiral path. The operation relies on the interplay between two fundamental forces: a constant magnetic field and an alternating electric field.

### 1. The Lorentz Force
The total force $\vec{F}$ acting on a particle of charge $q$ moving with velocity $\vec{v}$ in an electric field $\vec{E}$ and a magnetic field $\vec{B}$ is given by the Lorentz force equation:
$$\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$$

### 2. Magnetic Bending and Cyclotron Frequency
Inside the hollow D-shaped electrodes ("Dees"), the electric field is zero ($\vec{E} = 0$). The uniform magnetic field $\vec{B}$ (directed along the $y$-axis) exerts a magnetic force perpendicular to the velocity, forcing the particle into a circular trajectory due to centripetal acceleration:
$$q v B = \frac{m v^2}{r}$$

Solving for the orbital radius $r$:
$$r = \frac{m v}{q B}$$

From this equation, a crucial property emerges: **as the particle's velocity $v$ increases, its orbital radius $r$ increases proportionally**. This causes the particle to spiral outward in widening semicircles.

The angular frequency of this rotation (known as the cyclotron frequency $\omega$) is:
$$\omega = \frac{q B}{m}$$
Notice that $\omega$ is independent of the radius and velocity (for non-relativistic speeds), meaning the time spent completing a semicircle remains constant regardless of how fast or wide the particle is moving.

### 3. The Accelerating Gap and Resonance
The particle crosses the central gap between the two Dees twice per orbit. Inside this narrow gap, an alternating electric field $\vec{E}$ is applied. Because the cyclotron frequency $\omega$ is constant, the electric field is synchronized to alternate its polarity at that exact frequency. This ensures that every time the particle crosses the gap, the electric field pushes it forward, imparting an accelerating kick that increases its velocity and energy.

### 4. Beam Ejection & Target
Once the particle reaches the maximum radius of the Dees ($r \approx R_{\max}$), it enters an electrostatic deflector region. The magnetic field is turned off for the outgoing path, and the particle is directed down a green beamline extension straight into a red target.

---

## ✨ Features

* **3D Visual Chamber:** Includes a cylindrical vacuum chamber, visible magenta Dee structure, and a central accelerating gap slit.
* **Numerical Integration:** Solves the equations of motion step-by-step using Euler-Cromer integration ($\Delta t = 0.005$).
* **Resonant Electric Field:** Flips polarity dynamically upon crossing the center line.
* **Beam Ejection & Target:** Automatically triggers an extraction path once the particle reaches the upper-right boundary, sending it shooting down a green beamline toward a red target before seamlessly looping back to restart.

---

## 🛠️ Prerequisites & Dependencies

To run this simulation, ensure you have Python installed along with the required libraries:

```bash
pip install vpython numpy
```

---

## 🚀 How to Run

1. Save your Python script as `Cyclotron Accelerator.py`.
2. Run the script from your terminal or IDE:
   ```bash
   python "Cyclotron Accelerator.py"
   ```
3. A browser window will automatically launch rendering your interactive 3D cyclotron simulation. Use your mouse to rotate, zoom, and pan around the chamber!