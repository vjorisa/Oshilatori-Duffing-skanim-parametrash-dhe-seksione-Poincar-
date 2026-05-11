import numpy as np
from scipy.integrate import solve_ivp
from src.models.duffing import duffing_rhs

def solve_duffing(y0, t_max, params, n_points=10000):
    t_eval = np.linspace(0, t_max, n_points)
    sol = solve_ivp(duffing_rhs, [0, t_max], y0, args=(params,), t_eval=t_eval, method='RK45', rtol=1e-9)
    return sol

def get_poincare_section(y0, params, n_periods=500, skip_periods=100):
    omega = params['omega']
    T = 2 * np.pi / omega
    
    # Koha totale duke përfshirë tranzientet që do fshijmë
    t_total = (n_periods + skip_periods) * T
    t_eval = np.arange(skip_periods * T, t_total, T)
    
    sol = solve_ivp(duffing_rhs, [0, t_total], y0, args=(params,), t_eval=t_eval, method='RK45', rtol=1e-10)
    return sol.y[0], sol.y[1]
