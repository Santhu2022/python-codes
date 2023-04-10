def both_from_front(expensive_toy_index, cheap_toy_index):
    min_toys = max(expensive_toy_index, cheap_toy_index) + 1
    return min_toys
def both_from_back(expensive_toy_index, cheap_toy_index, prices):
    min_toys = len(prices) - min(expensive_toy_index, cheap_toy_index) 
    return min_toys
def third_Case_oneFront_oneBack(expensive_toy_index, cheap_toy_index, prices):
    toy1 = min(expensive_toy_index, cheap_toy_index) + 1 #front
    toy2 = len(prices) - max(expensive_toy_index, cheap_toy_index) #back
    return toy1 + toy2

prices = list(map(int, input().split()))

expensive_toy_index = prices.index(max(prices))
cheap_toy_index = prices.index(min(prices))
min_toys = []

min_toys.append(both_from_front(expensive_toy_index, cheap_toy_index))
min_toys.append(both_from_back(expensive_toy_index, cheap_toy_index, prices))
min_toys.append(third_Case_oneFront_oneBack(expensive_toy_index, cheap_toy_index, prices))

print(len(prices) - min(min_toys))
