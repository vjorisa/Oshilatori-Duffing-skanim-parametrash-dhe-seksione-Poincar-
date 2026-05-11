import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from src.models.duffing import duffing_rhs

params = {'delta': 0.1, 'alpha': -1.0, 'beta': 1.0, 'omega': 1.4, 'gamma': 0.0}
gammas = [0.2, 0.3, 0.5] # Skanimi i forcës së jashtme
y0 = [1.0, 0.0]
t_span = [0, 200]

for g in gammas:
    params['gamma'] = g
    sol = solve_ivp(duffing_rhs, t_span, y0, args=(params,), t_eval=np.linspace(0, 200, 2000))
    
    plt.figure(figsize=(6,4))
    plt.plot(sol.y[0], sol.y[1], lw=0.5)
    plt.title(f"Skanimi: Gamma = {g}")
    plt.savefig(f"results/figures/scan_gamma_{g}.png")
    plt.close()
