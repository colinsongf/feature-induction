import math
import numpy as np


def l1(xi, yi):
    return abs(xi - yi)

def l2(xi, yi):
    return (xi - yi)**2


def lb_keogh(s1, s2, dist_f=l2, r=5):
    """
    >>> lb_keogh([0,2,1,1,1], [0,0,2,1.5,1,1], dist_f=l2, r=1)
    2.0615528128088303
    """
    LB_sum=0
    if len(s2) < len(s1):
        t = s1
        s1 = s2
        s2 = t

    for ind,i in enumerate(s1):
        lower_bound=min(s2[(ind-r if ind-r>=0 else 0):(ind+r)])
        upper_bound=max(s2[(ind-r if ind-r>=0 else 0):(ind+r)])

        if i>upper_bound:
            LB_sum=LB_sum + dist_f(i, upper_bound)
        elif i<lower_bound:
            LB_sum=LB_sum + dist_f(i, lower_bound)

    return np.sqrt(LB_sum)



class DTW(object):
    """
    >>> DTW(dist=l2, window=1e10).distance([0,2,1,1,1], [0,0,2,1.5,1,1])
    0.5
    >>> DTW(dist=l2, window=1).distance([0,2,1,1,1], [0,0,2,1.5,1,1])
    inf
    """
    def __init__(self, dist=l2, window=1e10):
        self.dist = dist
        self.window = window

    def distance(self, x, y):
        r, c = len(x), len(y)
        w = max(self.window, abs(r - c))
        D = np.ones((r + 1, c + 1)) * np.inf
        D[0, 0] = 0.

        for i in range(r):
            for j in range(max(0, i - w), min(c, i + w)):
                D[i+1, j+1] = self.dist(x[i], y[j])

        for i in range(r):  # why loop twice?!!
            for j in range(max(0, i - w), min(c, i + w)):
                D[i+1, j+1] += min(D[i, j], D[i, j+1], D[i+1, j])

        D = D[1:, 1:]
        return math.sqrt(D[-1, -1])

