import math
from multiprocessing import Pool
import cProfile
import io
import pstats

def f(x):
    return math.sqrt(1 - x * x)

def integrate_segment(start, end, delta_x):
    return sum(f(start + i * delta_x) * delta_x for i in range(int((end - start) / delta_x)))

def calculate_pi_parallel(N, processes=None):
    delta_x = 1.0 / N
    intervals = [(i * delta_x * N // processes, (i + 1) * delta_x * N // processes, delta_x) for i in range(processes)]
    
    with Pool(processes) as pool:
        areas = pool.starmap(integrate_segment, intervals)
    
    return sum(areas) * 4

def main():
    N = 1000000
    processes = 4

    pr = cProfile.Profile()
    pr.enable()

    pi_approx_parallel = calculate_pi_parallel(N, processes)

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    
    print(f"Approximate value of pi (parallel): {pi_approx_parallel}")
    with open('multiprocessing_profile.txt', 'w') as f:
        f.write(s.getvalue())

if __name__ == '__main__':
    main()
