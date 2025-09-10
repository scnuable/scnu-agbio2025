
import numpy as np
import pandas as pd

def growing_degree_days(tmean_c, base=10.0, upper=None):
    """Compute simple daily GDD given mean temperature.
    If upper is provided, cap temperatures at that value.
    """
    t = np.array(tmean_c, dtype=float)
    if upper is not None:
        t = np.minimum(t, upper)
    return np.maximum(0.0, t - base)

def rolling_leaf_wetness_hours(lwh_series, window=3):
    s = pd.Series(lwh_series).astype(float)
    return s.rolling(window, min_periods=1).sum()

def zscore(x):
    x = pd.Series(x).astype(float)
    return (x - x.mean())/x.std(ddof=0)

def risk_index_rulebased(row, tmin=12, tmax=28, lwh_min=6, rh_min=85):
    """Toy rule-based risk index for infection suitability.
    Returns 1 if all conditions are met, else 0.
    """
    t = row.get('tmean_c', None)
    rh = row.get('rh_percent', None)
    lwh = row.get('leaf_wetness_hours', None)
    if t is None or rh is None or lwh is None:
        return 0
    return int((tmin <= t <= tmax) and (lwh >= lwh_min) and (rh >= rh_min))

def cost_benefit(incidence_reduction_pct, cost_treatment, expected_loss_without_treatment):
    benefit = (incidence_reduction_pct/100.0) * expected_loss_without_treatment
    return benefit - cost_treatment
