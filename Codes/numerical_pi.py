import math
import cProfile
import pstats

def f(x):
    return math.sqrt(1 - x * x)

def calculate_pi(N):
    delta_x = 1.0 / N
    total_area = sum(f(i * delta_x) * delta_x for i in range(N))
    return total_area * 4  

def main():
    N = 1000000
    pr = cProfile.Profile()
    pr.enable()  # Start profiling
    
    pi_approx = calculate_pi(N)
    
    pr.disable()  # Stop profiling
    # Save the profiling results to a text file
    with open('profiling_results.txt', 'w') as file:
        ps = pstats.Stats(pr, stream=file)
        ps.sort_stats('cumulative').print_stats()
    
    print(f"Approximate value of pi by numerical integration: {pi_approx}")

if __name__ == '__main__':
    main()