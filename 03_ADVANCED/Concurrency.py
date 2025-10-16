# This script demonstrates advanced concurrency techniques including:
# 1. Threading for lightweight parallelism
# 2. Multiprocessing for CPU-bound tasks
# 3. Asyncio for asynchronous I/O tasks
# Each section includes detailed comments and examples.

# 1. THREADING
# --------------------------------------------------------------------------------------------------------
    import threading
    import time

    def print_numbers(name, n):
        # Prints numbers from 1 to n with a small delay.
        # Demonstrates running tasks concurrently using threads.
        for i in range(1, n + 1):
            print(f"[{name}] Number: {i}")
            time.sleep(0.5)

    # Create two threads
    thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 5))
    thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 5))

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for threads to complete
    thread1.join()
    thread2.join()


# 2. MULTIPROCESSING (WINDOWS SAFE EXAMPLE)
# --------------------------------------------------------------------------------------------------------
    # This example demonstrates how to run CPU-bound tasks in parallel using the multiprocessing module
    # and is guaranteed to work on Windows.

    # multiprocessing_example.py
    # from multiprocessing import Process, current_process
    # import time

    # def compute_square(n):
    #     print(f"[{current_process().name}] Computing square of {n}")
    #     time.sleep(1)
    #     print(f"[{current_process().name}] Result: {n**2}")

    # if __name__ == "__main__":
    #     numbers = [2, 4, 6, 8]
    #     processes = []

    #     for num in numbers:
    #         p = Process(target=compute_square, args=(num,)) # Note: Tuples in Python require a comma if they have a single element
    #         processes.append(p)
    #         p.start()

    #     for p in processes:
    #         p.join()

    #     print("All processes have finished.")

    # Execute with CMD like: python multiprocessing_example.py

# 3. ASYNCIO
# --------------------------------------------------------------------------------------------------------
import asyncio

async def async_task(name, delay):
    # Asynchronous task that waits for `delay` seconds and prints a message.
    # Demonstrates non-blocking I/O with asyncio.
    await asyncio.sleep(delay)
    print(f"[Async] Task {name} finished after {delay} seconds")

async def main():
    # Run multiple asynchronous tasks concurrently using asyncio.gather.
    tasks = [
        async_task("A", 2),
        async_task("B", 1),
        async_task("C", 3)
    ]
    await asyncio.gather(*tasks)

# Run the asyncio event loop
asyncio.run(main())