from mpi4py import MPI
import numpy as np
import cProfile
import io
import pstats

def f(x):
    return np.sqrt(1 - x * x)

def calculate_pi_mpi(N):
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    delta_x = 1.0 / N
    local_n = N // size

    x_values = np.linspace(rank * local_n * delta_x, 
                           (rank + 1) * local_n * delta_x, 
                           local_n, endpoint=False)
    local_sum = np.sum(f(x_values) * delta_x)

    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

    if rank == 0:
        pi_approx = total_sum * 4
        return pi_approx

def main():
    N = 1000000
    pr = cProfile.Profile()
    pr.enable()
    
    pi_approx = calculate_pi_mpi(N)
    
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()

    with open(f'profile_rank_{MPI.COMM_WORLD.Get_rank()}.txt', 'w') as f:
        f.write(s.getvalue())
    
    if pi_approx is not None:
        print(f"Approximate value of pi (distributed): {pi_approx}")

if __name__ == "__main__":
    main()