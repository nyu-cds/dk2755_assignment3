
"""
    N-body simulation.
   
    The original optimized script execution time =  28.6s 
    Execution time with numba = 10.5s
    The relative speedup(R)= 28.6 / 10.5  = 2.72
    
    The results in both these versions are the same
"""

import numpy as np
import timeit    
import itertools
from numba import jit, int32, float64,vectorize

   
@vectorize([float64(float64, float64)])
def vec_deltas(a, b):
    return np.subtract(a,b)
    
    
@jit('void(f8[:,:,:],f8, i4, i4)')
def advance(BODIES,dt,loops,iterations):
    '''
        advance the system one timestep
    '''
    
    # Get BODIES pair
    bodies_pair = list(itertools.combinations(BODIES.keys(), 2))
    
    for _ in range(loops):
        for _ in range(iterations):
            for (body1, body2) in bodies_pair:
                (x1, v1, m1) = BODIES[body1]
                (x2, v2, m2) = BODIES[body2]
                (dx, dy, dz) = vec_deltas(x1, x2)
                iVal = dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
                v1[0] -= dx * m2 * iVal
                v1[1] -= dy * m2 * iVal
                v1[2] -= dz * m2 * iVal
                v2[0] += dx * m1 * iVal
                v2[1] += dy * m1 * iVal
                v2[2] += dz * m1 * iVal
        
            for body in BODIES.keys():
                (r, [vx, vy, vz], m) = BODIES[body]
                r[0] += dt * vx
                r[1] += dt * vy
                r[2] += dt * vz
                
        print(report_energy(BODIES, bodies_pair))
  
@jit('f8(f8[:,:,:], i4[:,:], f8)')
def report_energy(BODIES, bodies_pair,e=0.0):
    '''
        compute the energy and return it so that it can be printed
    '''
    for (body1, body2) in bodies_pair:
        (x1, v1, m1) = BODIES[body1]
        (x2, v2, m2) = BODIES[body2]
        (dx, dy, dz) = vec_deltas(x1, x2)
        e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)
        
    for body in BODIES.keys():
        (r, [vx, vy, vz], m) = BODIES[body]
        e += m * (vx * vx + vy * vy + vz * vz) / 2.
        
    return e

@jit('void(f8[:,:,:], char, f8, f8, f8)')
def offset_momentum(BODIES, ref, px=0.0, py=0.0, pz=0.0):
    '''
        ref is the body in the center of the system
        offset values from this reference
    '''
    for (body, (r, [vx, vy, vz], m)) in BODIES.items():
        px -= vx * m
        py -= vy * m
        pz -= vz * m
        
    (r, v, m) = BODIES[ref]
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m

@jit('void(i4, char, i4)')
def nbody(loops, reference, iterations):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    
    # Define BODIES dictionary
    PI = 3.14159265358979323
    SOLAR_MASS = 4 * PI * PI
    DAYS_PER_YEAR = 365.24
    
    BODIES = {
        'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),

        'jupiter': ([4.84143144246472090e+00,
                     -1.16032004402742839e+00,
                     -1.03622044471123109e-01],
                    [1.66007664274403694e-03 * DAYS_PER_YEAR,
                     7.69901118419740425e-03 * DAYS_PER_YEAR,
                     -6.90460016972063023e-05 * DAYS_PER_YEAR],
                    9.54791938424326609e-04 * SOLAR_MASS),

        'saturn': ([8.34336671824457987e+00,
                    4.12479856412430479e+00,
                    -4.03523417114321381e-01],
                   [-2.76742510726862411e-03 * DAYS_PER_YEAR,
                    4.99852801234917238e-03 * DAYS_PER_YEAR,
                    2.30417297573763929e-05 * DAYS_PER_YEAR],
                   2.85885980666130812e-04 * SOLAR_MASS),

        'uranus': ([1.28943695621391310e+01,
                    -1.51111514016986312e+01,
                    -2.23307578892655734e-01],
                   [2.96460137564761618e-03 * DAYS_PER_YEAR,
                    2.37847173959480950e-03 * DAYS_PER_YEAR,
                    -2.96589568540237556e-05 * DAYS_PER_YEAR],
                   4.36624404335156298e-05 * SOLAR_MASS),

        'neptune': ([1.53796971148509165e+01,
                     -2.59193146099879641e+01,
                     1.79258772950371181e-01],
                    [2.68067772490389322e-03 * DAYS_PER_YEAR,
                     1.62824170038242295e-03 * DAYS_PER_YEAR,
                     -9.51592254519715870e-05 * DAYS_PER_YEAR],
                    5.15138902046611451e-05 * SOLAR_MASS)}
    

    # Set up global state
    offset_momentum(BODIES, reference)
 
    advance(BODIES,0.01,loops,iterations)

if __name__ == '__main__':
    print(timeit.timeit("nbody(100, 'sun', 20000)", setup="from __main__ import nbody", number=1))
