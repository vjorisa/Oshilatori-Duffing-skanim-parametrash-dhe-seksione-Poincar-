import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from src.analysis.pointcare import solve_duffing, get_poincare_section

# Parametrat që shpesh shkaktojnë kaos
params = {'delta': 0.3, 'alpha': -1.0, 'beta': 1.0, 'gamma': 0.5, 'omega': 1.2}
y0 = [1.0, 0.0]

# 1. Zgjidhja kohore dhe Portreti Fazor
sol = solve_duffing(y0, 200, params)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(sol.t, sol.y[0])
ax1.set_title("Seria Kohore x(t)")
ax2.plot(sol.y[0], sol.y[1], lw=0.5)
ax2.set_title("Portreti Fazor")
plt.savefig("results/figures/basic_dynamics.png")

# 2. Seksioni Poincare
px, pv = get_poincare_section(y0, params, n_periods=2000)
plt.figure(figsize=(8, 8))
plt.scatter(px, pv, s=0.5, color='red')
plt.title(f"Seksioni Poincaré (gamma={params['gamma']})")
plt.xlabel("x")
plt.ylabel("v")
plt.savefig("results/figures/poincare_section.png")
plt.show()
