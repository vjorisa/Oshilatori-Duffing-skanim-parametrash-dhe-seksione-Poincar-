
# File 2: src/visualization/phase_plots.py - Vizualizimet

phase_plots = '''"""
Module: phase_plots.py
Përshkrimi: Vizualizime për oshilatorin Duffing - seritë kohore, 
portretet fazorë dhe grafikët e energjisë.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import matplotlib.gridspec as gridspec

# Cilësimet e stilit të grafikëve
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 200
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['legend.fontsize'] = 9


def plot_time_series(sol, params, save_path=None, title_suffix=""):
    """
    Vizualizon seritë kohore të pozicionit dhe shpejtësisë.
    """
    t = sol.t
    x = sol.y[0]
    v = sol.y[1]
    
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    
    # Pozicioni vs Koha
    axes[0].plot(t, x, 'b-', linewidth=0.8, alpha=0.9)
    axes[0].set_ylabel('$x(t)$')
    axes[0].set_title(f'Seritë Kohore - Oshilatori Duffing{title_suffix}')
    axes[0].grid(True, alpha=0.3)
    
    # Shpejtësia vs Koha
    axes[1].plot(t, v, 'r-', linewidth=0.8, alpha=0.9)
    axes[1].set_ylabel('$v(t) = \\dot{x}(t)$')
    axes[1].grid(True, alpha=0.3)
    
    # Forca e jashtme vs Koha
    gamma = params['gamma']
    omega = params['omega']
    F_ext = gamma * np.cos(omega * t)
    axes[2].plot(t, F_ext, 'g-', linewidth=0.8, alpha=0.7)
    axes[2].set_ylabel('$F_{ext}(t)$')
    axes[2].set_xlabel('$t$')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Figura u ruajt në: {save_path}")
    
    return fig


def plot_phase_portrait(sol, params, save_path=None, title_suffix="", 
                        color_by_time=False, steady_state_only=False):
    """
    Vizualizon portretin fazor (x vs v).
    """
    t = sol.t
    x = sol.y[0]
    v = sol.y[1]
    
    if steady_state_only:
        # Përdor vetëm periodat e fundit për regjimin stacionar
        from ..models.duffing import find_steady_state
        idx = find_steady_state(sol, params, n_last_periods=20)
        t = t[idx:]
        x = x[idx:]
        v = v[idx:]
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    if color_by_time:
        # Ngjyros sipas kohës për të parë evoluimin
        scatter = ax.scatter(x, v, c=t, cmap='viridis', s=1, alpha=0.6)
        plt.colorbar(scatter, ax=ax, label='$t$')
    else:
        ax.plot(x, v, 'b-', linewidth=0.5, alpha=0.7)
    
    ax.set_xlabel('$x$')
    ax.set_ylabel('$v$')
    title = 'Portreti Fazor'
    if steady_state_only:
        title += ' (Regjimi Stacionar)'
    title += title_suffix
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal', adjustable='box')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Figura u ruajt në: {save_path}")
    
    return fig


def plot_energy(sol, params, save_path=None, title_suffix=""):
    """
    Vizualizon energjinë efektive si funksion të kohës.
    """
    from ..models.duffing import effective_energy
    
    t = sol.t
    x = sol.y[0]
    v = sol.y[1]
    
    E = effective_energy(x, v, params)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, E, 'purple', linewidth=0.8)
    ax.set_xlabel('$t$')
    ax.set_ylabel('$E_{eff} = \\frac{1}{2}v^2 + \\frac{1}{2}\\alpha x^2 + \\frac{1}{4}\\beta x^4$')
    ax.set_title(f'Energjia Efektive vs Koha{title_suffix}')
    ax.grid(True, alpha=0.3)
    
    # Shto një shënim për energjinë mesatare në regjimin stacionar
    E_mean = np.mean(E[len(E)//2:])
    ax.axhline(y=E_mean, color='r', linestyle='--', alpha=0.5, 
               label=f'$\\langle E \\rangle = {E_mean:.3f}$')
    ax.legend()
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Figura u ruajt në: {save_path}")
    
    return fig


def plot_combined_analysis(sol, params, save_path=None, title_suffix=""):
    """
    Vizualizim i kombinuar: seritë kohore, portreti fazor dhe energjia.
    """
    t = sol.t
    x = sol.y[0]
    v = sol.y[1]
    
    fig = plt.figure(figsize=(14, 10))
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])
    
    # Seritë kohore
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(t, x, 'b-', linewidth=0.8, label='$x(t)$')
    ax1.plot(t, v, 'r-', linewidth=0.8, alpha=0.7, label='$v(t)$')
    ax1.set_xlabel('$t$')
    ax1.set_ylabel('Vlera')
    ax1.set_title(f'Seritë Kohore{title_suffix}')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Portreti fazor (plot i plotë)
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.plot(x, v, 'g-', linewidth=0.5, alpha=0.6)
    ax2.set_xlabel('$x$')
    ax2.set_ylabel('$v$')
    ax2.set_title('Portreti Fazor (i plotë)')
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal', adjustable='box')
    
    # Portreti fazor (regjimi stacionar)
    ax3 = fig.add_subplot(gs[1, 1])
    from ..models.duffing import find_steady_state
    idx = find_steady_state(sol, params, n_last_periods=20)
    ax3.plot(x[idx:], v[idx:], 'purple', linewidth=0.8)
    ax3.set_xlabel('$x$')
    ax3.set_ylabel('$v$')
    ax3.set_title('Portreti Fazor (stacionar)')
    ax3.grid(True, alpha=0.3)
    ax3.set_aspect('equal', adjustable='box')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Figura u ruajt në: {save_path}")
    
    return fig


def plot_multiple_ic(params, t_span, ic_list, labels=None, save_path=None):
    """
    Vizualizon portretet fazorë për kushte fillestare të ndryshme.
    """
    from ..models.duffing import simulate_duffing
    
    fig, ax = plt.subplots(figsize=(9, 9))
    
    colors = plt.cm.tab10(np.linspace(0, 1, len(ic_list)))
    
    for i, (y0, color) in enumerate(zip(ic_list, colors)):
        sol = simulate_duffing(t_span, y0, params)
        label = labels[i] if labels else f'IC: {y0}'
        ax.plot(sol.y[0], sol.y[1], color=color, linewidth=0.6, 
                alpha=0.7, label=label)
    
    ax.set_xlabel('$x$')
    ax.set_ylabel('$v$')
    ax.set_title('Portreti Fazor - Krahasim i Kushteve Fillestare')
    ax.legend(loc='best', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal', adjustable='box')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Figura u ruajt në: {save_path}")
    
    return fig
'''

with open("/mnt/agents/output/duffing_poincare_project/src/visualization/phase_plots.py", "w") as f:
    f.write(phase_plots)

print("✓ src/visualization/phase_plots.py u krijua me sukses!")
