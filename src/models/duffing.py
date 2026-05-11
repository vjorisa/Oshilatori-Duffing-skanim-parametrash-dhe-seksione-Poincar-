import numpy as np

def duffing_rhs(t, y, params):
    """
    y[0] = x (pozicioni)
    y[1] = v (shpejtësia)
    """
    x, v = y
    delta = params['delta']
    alpha = params['alpha']
    beta = params['beta']
    gamma = params['gamma']
    omega = params['omega']
    
    dxdt = v
    dvdt = gamma * np.cos(omega * t) - delta * v - alpha * x - beta * x**3
    return [dxdt, dvdt]

def effective_energy(x, v, params):
    # E = Kinetike + Potenciale
    # U(x) = 0.5*alpha*x^2 + 0.25*beta*x^4
    return 0.5 * v**2 + 0.5 * params['alpha'] * x**2 + 0.25 * params['beta'] * x**4
