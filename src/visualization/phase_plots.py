import matplotlib.pyplot as plt
import numpy as np

def plot_dynamics(sol, params, title_suffix=""):
    t = sol.t
    x = sol.y[0]
    v = sol.y[1]
    
    # Kalkulojmë energjinë gjatë kohës
    energy = 0.5 * v**2 + 0.5 * params['alpha'] * x**2 + 0.25 * params['beta'] * x**4

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))
    
    # Seria kohore
    ax1.plot(t, x, color='blue')
    ax1.set_title(f"Seria Kohore x(t) {title_suffix}")
    ax1.set_xlabel("Koha (t)")
    
    # Portreti fazor
    ax2.plot(x, v, lw=0.5, color='black')
    ax2.set_title("Portreti Fazor (v vs x)")
    
    # Energjia Efektive
    ax3.plot(t, energy, color='green')
    ax3.set_title("Energjia Efektive vs Koha")
    ax3.set_xlabel("Koha (t)")
    
    plt.tight_layout()
    return fig
