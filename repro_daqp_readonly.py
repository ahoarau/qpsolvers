import numpy as np
import daqp
from qpsolvers import solve_qp

def test_daqp_readonly():
    P = np.array([[2.0, 0.0], [0.0, 2.0]])
    q = np.array([0.0, 0.0])
    G = np.array([[1.0, 0.0], [0.0, 1.0]])
    h = np.array([1.0, 1.0])
    
    # Make arrays read-only
    P.flags.writeable = False
    q.flags.writeable = False
    G.flags.writeable = False
    h.flags.writeable = False
    
    print("Testing daqp with read-only inputs...")
    try:
        x = solve_qp(P, q, G, h, solver="daqp")
        print("Success:", x)
    except Exception as e:
        print("Failed:", e)

if __name__ == "__main__":
    test_daqp_readonly()
