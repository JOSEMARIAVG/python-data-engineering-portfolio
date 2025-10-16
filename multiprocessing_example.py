from multiprocessing import Process, current_process
import time

def compute_square(n):
    print(f"[{current_process().name}] Computing square of {n}")
    time.sleep(1)
    print(f"[{current_process().name}] Result: {n**2}")

if __name__ == "__main__":
    numbers = [2, 4, 6, 8]
    processes = []
    for num in numbers:
        p = Process(target=compute_square, args=(num,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes have finished.")