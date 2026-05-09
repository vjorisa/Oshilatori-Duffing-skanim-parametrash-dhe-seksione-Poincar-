
# File 1: src/models/duffing.py - Modeli matematikor i Duffing-ut

duffing_model = '''"""
Module: duffing.py
Përshkrimi: Implementimi i ekuacionit të Duffing-ut të detyruar dhe të amortizuar.
Ekuacioni: x'' + δx' + αx + βx³ = γcos(ωt)
"""

import numpy as np
from scipy.integrate import solve_ivp

def duffing_rhs(t, y, params):
    """
    Funksioni i anës së djathtë (RHS) për sistemin e Duffing-ut.
    
    Parametrat:
    -----------
    t : float
        Koha
    y : array_like, shape (2,)
        y[0] = x (pozicioni)
        y[1] = v (shpejtësia, dx/dt)
    params : dict
        Dictionary me parametrat:
        - 'delta': koeficienti i amortizimit
        - 'alpha': koeficienti linear i rigiditetit
        - 'beta': koeficienti jolinear (kubik)
        - 'gamma': amplituda e forcës së jashtme
        - 'omega': frekuenca e forcës së jashtme
    
    Kthen:
    ------
    dydt : array, shape (2,)
        [dx/dt, dv/dt]
    """
    x, v = y
    delta = params['delta']
    alpha = params['alpha']
    beta = params['beta']
    gamma = params['gamma']
    omega = params['omega']
    
    dxdt = v
    dvdt = -delta * v - alpha * x - beta * x**3 + gamma * np.cos(omega * t)
    
    return [dxdt, dvdt]


def simulate_duffing(t_span, y0, params, t_eval=None, method='RK45', 
                      max_step=None, rtol=1e-6, atol=1e-9):
    """
    Simulon oshilatorin Duffing duke përdorur solve_ivp.
    
    Parametrat:
    -----------
    t_span : tuple (t_start, t_end)
        Intervali kohor
    y0 : array_like, shape (2,)
        Kushtet fillestare [x0, v0]
    params : dict
        Parametrat e sistemit
    t_eval : array_like, optional
        Piket kohe për vlerësim
    method : str, default='RK45'
        Metoda e integrimit
    
    Kthen:
    ------
    sol : OdeResult
        Objekti i zgjidhjes nga solve_ivp
    """
    if t_eval is None:
        # Numër i mjaftueshëm pikash për vizualizim të mirë
        t_eval = np.linspace(t_span[0], t_span[1], 10000)
    
    sol = solve_ivp(
        fun=lambda t, y: duffing_rhs(t, y, params),
        t_span=t_span,
        y0=y0,
        t_eval=t_eval,
        method=method,
        max_step=max_step,
        rtol=rtol,
        atol=atol,
        dense_output=True
    )
    
    return sol


def compute_period_driving(params):
    """
    Llogarit periodën e forcës së jashtme.
    """
    omega = params['omega']
    return 2 * np.pi / omega


def effective_energy(x, v, params):
    """
    Llogarit energjinë efektive të sistemit.
    E = (1/2)v² + (1/2)αx² + (1/4)βx⁴
    
    Kini parasysh: Ky nuk është një invariant për shkak të 
    amortizimit dhe forcës së jashtme, por është një mjet diagnostik.
    """
    alpha = params['alpha']
    beta = params['beta']
    
    kinetic = 0.5 * v**2
    potential = 0.5 * alpha * x**2 + 0.25 * beta * x**4
    
    return kinetic + potential


def find_steady_state(sol, params, n_last_periods=10):
    """
    Gjen gjendjen stacionare duke analizuar periodat e fundit.
    Kthen indeksin e fillimit të regjimit stacionar.
    """
    T = compute_period_driving(params)
    t = sol.t
    
    # Gjej indeksin ku fillojnë periodat e fundit
    t_start_steady = t[-1] - n_last_periods * T
    idx_steady = np.searchsorted(t, t_start_steady)
    
    return idx_steady
'''

with open("/mnt/agents/output/duffing_poincare_project/src/models/duffing.py", "w") as f:
    f.write(duffing_model)

print("✓ src/models/duffing.py u krijua me sukses!")
