
# File 4: scripts/run_single.py - Simulim i vetëm

run_single = '''#!/usr/bin/env python3
"""
Script: run_single.py
Përshkrimi: Ekzekuton një simulim të vetëm të oshilatorit Duffing 
me parametra të paracaktuar.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from src.models.duffing import simulate_duffing, effective_energy
from src.visualization.phase_plots import (plot_time_series, plot_phase_portrait, 
                                            plot_energy, plot_combined_analysis)
from src.analysis.poincare import poincare_section_dense, plot_poincare


def main():
    # ============================================================
    # PARAMETRAT E SISTEMIT
    # ============================================================
    
    # Parametrat fizikë
    params = {
        'delta': 0.2,    # Amortizimi
        'alpha': -1.0,   # Koeficienti linear (negativ = dyqan i dyfishtë)
        'beta': 1.0,     # Koeficienti jolinear
        'gamma': 0.3,    # Amplituda e forcës së jashtme
        'omega': 1.2     # Frekuenca e forcës së jashtme
    }
    
    # Kushtet fillestare
    y0 = [1.0, 0.0]  # [x0, v0]
    
    # Intervali kohor (koha e gjatë për të eleminuar transientet)
    t_span = (0, 200)
    
    print("="*60)
    print("SIMULIMI I OSHILATORIT DUFFING")
    print("="*60)
    print(f"\\nParametrat:")
    print(f"  δ (amortizim)    = {params['delta']}")
    print(f"  α (linear)       = {params['alpha']}")
    print(f"  β (jolinear)     = {params['beta']}")
    print(f"  γ (forcë e jashtme) = {params['gamma']}")
    print(f"  ω (frekuencë)    = {params['omega']}")
    print(f"\\nKushtet fillestare: x₀ = {y0[0]}, v₀ = {y0[1]}")
    print(f"Intervali kohor: t ∈ {t_span}")
    print("="*60)
    
    # ============================================================
    # SIMULIMI
    # ============================================================
    
    print("\\n[1/5] Duke simuluar sistemin...")
    sol = simulate_duffing(t_span, y0, params, 
                         max_step=params['omega']/(20*2*np.pi))
    print(f"      Simulimi përfundoi. Numri i pikave: {len(sol.t)}")
    
    # ============================================================
    # VIZUALIZIMET
    # ============================================================
    
    results_dir = os.path.join(os.path.dirname(__file__), '..', 'results', 'figures')
    os.makedirs(results_dir, exist_ok=True)
    
    print("\\n[2/5] Duke krijuar seritë kohore...")
    fig1 = plot_time_series(sol, params, 
                            save_path=os.path.join(results_dir, '01_time_series.png'))
    
    print("[3/5] Duke krijuar portretin fazor...")
    fig2 = plot_phase_portrait(sol, params, 
                               save_path=os.path.join(results_dir, '02_phase_portrait_full.png'),
                               color_by_time=True)
    fig3 = plot_phase_portrait(sol, params, 
                               save_path=os.path.join(results_dir, '03_phase_portrait_steady.png'),
                               steady_state_only=True)
    
    print("[4/5] Duke krijuar grafikun e energjisë...")
    fig4 = plot_energy(sol, params, 
                       save_path=os.path.join(results_dir, '04_energy.png'))
    
    print("[5/5] Duke krijuar seksionin Poincaré...")
    x_p, v_p, t_p = poincare_section_dense(sol, params, 
                                           n_periods_skip=50, n_points=1000)
    fig5 = plot_poincare(x_p, v_p, params,
                         save_path=os.path.join(results_dir, '05_poincare_section.png'))
    
    # Analizë e shpejtë
    print("\\n" + "="*60)
    print("ANALIZË E REZULTATEVE")
    print("="*60)
    print(f"\\nSeksioni Poincaré:")
    print(f"  Numri i pikave: {len(x_p)}")
    print(f"  Gama e x: [{np.min(x_p):.4f}, {np.max(x_p):.4f}]")
    print(f"  Gama e v: [{np.min(v_p):.4f}, {np.max(v_p):.4f}]")
    
    # Vlerëso nëse dinamika është periodike apo kaotike
    n_unique = len(set([(round(x, 3), round(v, 3)) for x, v in zip(x_p, v_p)]))
    if len(x_p) > 0:
        ratio = n_unique / len(x_p)
        if ratio < 0.1:
            print(f"  Dinamika: PERIODIKE (raport unik/total = {ratio:.3f})")
        elif ratio < 0.5:
            print(f"  Dinamika: KOMPLIKUAR (raport unik/total = {ratio:.3f})")
        else:
            print(f"  Dinamika: KAOTIKE (raport unik/total = {ratio:.3f})")
    
    # Energjia
    E = effective_energy(sol.y[0], sol.y[1], params)
    print(f"\\nEnergjia efektive:")
    print(f"  Mesatarja: {np.mean(E):.4f}")
    print(f"  Devijimi standard: {np.std(E):.4f}")
    
    print("\\n" + "="*60)
    print("FIGURAT U RUAJTËN NË:")
    print(f"  {results_dir}")
    print("="*60)


if __name__ == "__main__":
    main()
'''

with open("/mnt/agents/output/duffing_poincare_project/scripts/run_single.py", "w") as f:
    f.write(run_single)

print("✓ scripts/run_single.py u krijua me sukses!")
