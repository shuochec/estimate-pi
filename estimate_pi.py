import random
import concurrent.futures

def estimate_pi(n):
    num_circle = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x ** 2 + y ** 2
        if distance <= 1:
            num_circle += 1
    return 4 * num_circle / n

pi, num_worker = 0, 100
with concurrent.futures.ThreadPoolExecutor(max_workers = num_worker) as executor:
    futures = [executor.submit(estimate_pi, 100000) for _ in range(num_worker)]
    for future in concurrent.futures.as_completed(futures):
        try:
            data = future.result()
        except Exception as exc:
            print('Generated an exception: %s' % (exc))
        else:
            print(data)
            pi += data

print(pi / num_worker)