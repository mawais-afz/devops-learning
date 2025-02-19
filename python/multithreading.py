import threading
import time
from concurrent.futures import ThreadPoolExecutor

def worker_function(thread_id, delay):
    """Worker function that simulates some work"""
    print(f"Thread {thread_id} starting")
    time.sleep(delay)
    print(f"Thread {thread_id} finished")

def cpu_intensive_task(numbers):
    """Function that performs a CPU-intensive calculation"""
    result = sum(n ** 2 for n in numbers)
    print(f"Calculated sum of squares: {result}")

def main():
    # Example 1: Basic threading with ThreadPoolExecutor using map
    print("\nExample 1: Basic threading")
    thread_params = [(i, 2) for i in range(3)]
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(lambda p: worker_function(*p), thread_params)

    # Example 2: Threading with shared data
    print("\nExample 2: Threading with shared data")
    counter = 0
    counter_lock = threading.Lock()

    def increment_counter():
        nonlocal counter
        for _ in range(100000):
            with counter_lock:
                counter += 1

    with ThreadPoolExecutor(max_workers=2) as executor:
        list(executor.map(lambda x: increment_counter(), range(2)))

    print(f"Final counter value: {counter}")

    # Example 3: CPU-intensive tasks using map
    print("\nExample 3: CPU-intensive tasks")
    number_ranges = [range(1, 5000), range(5000, 10000)]

    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        list(executor.map(cpu_intensive_task, number_ranges))

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
