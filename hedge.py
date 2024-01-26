import random
import math

N, T = map(int, input().split())

weights = [1] * N
epsilon = 0.05
euler_numer = math.e

for _ in range(T):
    predictions = list(map(int, input().split()))
    sum_prob = sum(weights)
    random_value = random.random() * sum_prob

    model = -1

    for ind in range(N):
        random_value -= weights[ind]
        if random_value <= 0: 
            model = ind
            break

    print(predictions[model], flush=True)

    actual_outcome = int(input())

    for ind in range(len(weights)):
        weights[ind] *= euler_numer ** (-epsilon * abs(predictions[ind] - actual_outcome))
