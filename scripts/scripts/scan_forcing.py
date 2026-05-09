
# File 5: scripts/scan_forcing.py - Skanimi i forcës së jashtme

scan_forcing = '''#!/usr/bin/env python3
"""
Script: scan_forcing.py
Përshkrimi: Skanon forcën e jashtme γ dhe vizualizon ndryshimin e dinamikës.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import matplotlib.pyplot as plt
from src.models.duffing import simulate_duffing
from src.analysis.poincare import (poincare_section_dense, plot_multiple_poincare,
                                    scan_parameter, plot_bifurcation_diagram)
from src.visualization.phase_plots import plot_phase_portrait


def main():
    # ============================================================
    # PARAMETRAT BAZË
    # ============================================================
    
    params_base = {
        'delta': 0.2,
        'alpha': -1.0,
        'beta': 1.0,
        'gamma': 0.3,  # Do të ndryshohet
        'omega': 1.2
    }
    
    y0 = [1.0, 0.0]
    
    print("="*60)
    print("SKANIMI I FORCËS SË JASHTME (γ)")
    print("="*60)
    print(f"\\nParametrat bazë:")
    print(f"  δ = {params_base['delta']}, α = {params_base['alpha']}")
    print(f"  β = {params_base['beta']}, ω = {params_base['omega']}")
    print(f"  Kushtet fillestare: x₀ = {y0[0]}, v₀ = {y0[1]}")
    
    results_dir = os.path.join(os.path.dirname(__file__), '..', 'results', 'figures')
    os.makedirs(results_dir, exist_ok=True)
    
    # ============================================================
    # EKSPERIMENTI 1: Tre vlera karakteristike të γ
    # ============================================================
    
    print("\\n" + "-"*60)
    print("EKSPERIMENTI 1: Seksionet Poincaré për 3 vlera të γ")
    print("-"*60)
    
    gamma_values = [0.2, 0.35, 0.5]
    t_span_long = (0, 300)  # Kohë më e gjatë për transientë
    
    fig1 = plot_multiple_poincare(gamma_values, params_base, t_span_long, y0,
                                   save_path=os.path.join(results_dir, 'scan_gamma_3values.png'),
                                   n_periods_skip=100)
    
    print("  ✓ Figura u krijua për 3 vlera të γ")
    
    # ============================================================
    # EKSPERIMENTI 2: Skanim i hollësishëm i γ
    # ============================================================
    
    print("\\n" + "-"*60)
    print("EKSPERIMENTI 2: Skanim i hollësishëm i γ (diagram bifurkacioni)")
    print("-"*60)
    
    gamma_scan = np.linspace(0.15, 0.6, 30)
    t_span_scan = (0, 400)
    
    print(f"  Skanimi: {len(gamma_scan)} vlera nga {gamma_scan[0]} deri {gamma_scan[-1]}")
    
    results = scan_parameter('gamma', gamma_scan, params_base, t_span_scan, y0,
                             n_periods_skip=150, n_poincare_points=300)
    
    # Ekstrakto të dhënat për diagramin e bifurkacionit
    x_p_list = [x_p for _, x_p, _ in results]
    
    fig2 = plot_bifurcation_diagram(gamma_scan, x_p_list, param_name='gamma',
                                     save_path=os.path.join(results_dir, 'bifurcation_gamma.png'))
    
    print("  ✓ Diagrami i bifurkacionit u krijua")
    
    # ============================================================
    # EKSPERIMENTI 3: Krahasim me oshilatorin pa forcë të jashtme
    # ============================================================
    
    print("\\n" + "-"*60)
    print("EKSPERIMENTI 3: Krahasim me oshilatorin pa forcë të jashtme")
    print("-"*60)
    
    from src.analysis.poincare import compare_with_harmonic
    
    t_span_compare = (0, 100)
    fig3 = compare_with_harmonic(params_base, t_span_compare, y0,
                                  save_path=os.path.join(results_dir, 'comparison_harmonic.png'))
    
    print("  ✓ Krahasimi u krijua")
    
    # ============================================================
    # EKSPERIMENTI 4: Dy kushte fillestare shumë të afërta (sensitivitet)
    # ============================================================
    
    print("\\n" + "-"*60)
    print("EKSPERIMENTI 4: Sensitivitet ndaj kushteve fillestare")
    print("-"*60)
    
    eps = 1e-4
    ic_list = [[1.0, 0.0], [1.0 + eps, 0.0]]
    labels = [f'$x_0 = 1.0$', f'$x_0 = 1.0 + {eps}$']
    
    from src.visualization.phase_plots import plot_multiple_ic
    
    t_span_sens = (0, 80)
    fig4 = plot_multiple_ic(params_base, t_span_sens, ic_list, labels=labels,
                            save_path=os.path.join(results_dir, 'sensitivity_ic.png'))
    
    # Llogarit diferencën në kohën e fundit
    sol1 = simulate_duffing(t_span_sens, ic_list[0], params_base)
    sol2 = simulate_duffing(t_span_sens, ic_list[1], params_base)
    
    diff_x = np.abs(sol1.y[0][-1] - sol2.y[0][-1])
    diff_v = np.abs(sol1.y[1][-1] - sol2.y[1][-1])
    
    print(f"  Diferenca në t={t_span_sens[1]}: Δx = {diff_x:.6f}, Δv = {diff_v:.6f}")
    print(f"  Rritja relative: {diff_x/eps:.1f}x (tregon sensitivitetin)")
    print("  ✓ Figura e sensitivitetit u krijua")
    
    # ============================================================
    # SKANIMI I PARAMETRAVE TË TJERË
    # ============================================================
    
    print("\\n" + "-"*60)
    print("EKSPERIMENTI 5: Skanimi i ω (frekuenca)")
    print("-"*60)
    
    omega_values = np.linspace(0.8, 2.0, 15)
    t_span_omega = (0, 300)
    
    results_omega = scan_parameter('omega', omega_values, params_base, 
                                    t_span_omega, y0,
                                    n_periods_skip=100, n_poincare_points=300)
    
    x_p_omega = [x_p for _, x_p, _ in results_omega]
    fig5 = plot_bifurcation_diagram(omega_values, x_p_omega, param_name='omega',
                                     save_path=os.path.join(results_dir, 'bifurcation_omega.png'))
    
    print("  ✓ Diagrami i bifurkacionit për ω u krijua")
    
    print("\\n" + "-"*60)
    print("EKSPERIMENTI 6: Skanimi i δ (amortizimi)")
    print("-"*60)
    
    delta_values = np.linspace(0.05, 0.5, 15)
    t_span_delta = (0, 300)
    
    results_delta = scan_parameter('delta', delta_values, params_base, 
                                    t_span_delta, y0,
                                    n_periods_skip=100, n_poincare_points=300)
    
    x_p_delta = [x_p for _, x_p, _ in results_delta]
    fig6 = plot_bifurcation_diagram(delta_values, x_p_delta, param_name='delta',
                                     save_path=os.path.join(results_dir, 'bifurcation_delta.png'))
    
    print("  ✓ Diagrami i bifurkacionit për δ u krijua")
    
    print("\\n" + "="*60)
    print("TË GJITHA EKSPERIMENTET PËRFUNDUAN!")
    print("="*60)
    print(f"\\nFigurat u ruajtën në: {results_dir}")
    print("\\nPërmbledhje e figurave:")
    print("  1. scan_gamma_3values.png - Seksionet Poincaré për 3 vlera γ")
    print("  2. bifurcation_gamma.png - Diagrami i bifurkacionit për γ")
    print("  3. comparison_harmonic.png - Krahasim me oshilatorin pa forcë")
    print("  4. sensitivity_ic.png - Sensitivitet ndaj kushteve fillestare")
    print("  5. bifurcation_omega.png - Diagrami i bifurkacionit për ω")
    print("  6. bifurcation_delta.png - Diagrami i bifurkacionit për δ")
    print("="*60)


if __name__ == "__main__":
    main()
'''

with open("/mnt/agents/output/duffing_poincare_project/scripts/scan_forcing.py", "w") as f:
    f.write(scan_forcing)

print("✓ scripts/scan_forcing.py u krijua me sukses!")
