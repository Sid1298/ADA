"""
title : Program for 0/1 Knapsack
author : $1D@1298
date : 28-10-2020
"""

captured = 0
capacity = eval(input("Enter max capacity of weight: "))
n = eval(input("Enter number of items: "))

items = []
values = []
weights = []
v_w = []

items_arranged = []
values_arranged = []
weights_arranged = []
v_w_arranged = []

items_captured = []
v_w_captured = []

for i in range(n):
    items.append(input("\nEnter Item name: "))
    values.append(int(input("Enter Item value: ")))
    weights.append(int(input("Enter Item weight: ")))
    v_w.append(values[i]/weights[i])

print(items, values, weights, v_w, sep='\n')
print('\n\n')

while len(v_w) > 0 and max(v_w) >= min(v_w):
    pop_index = v_w.index(max(v_w))
    v_w_arranged.append(v_w.pop(pop_index))
    items_arranged.append(items.pop(pop_index))
    values_arranged.append(values.pop(pop_index))
    weights_arranged.append(weights.pop(pop_index))

print(items_arranged, v_w_arranged, values_arranged, weights_arranged, sep='\n')
print('\n\n')

try:
    while capacity-min(weights_arranged) >= 0:

        if capacity - weights_arranged[0] >= 0:
            captured += values_arranged.pop(0)
            capacity -= weights_arranged.pop(0)
            items_captured.append(items_arranged.pop(0))
            v_w_captured.append(v_w_arranged.pop(0))
        else:
            values_arranged.pop(0)
            weights_arranged.pop(0)
            items_arranged.pop(0)
            v_w_arranged.pop(0)

except ValueError:
    print("List is now empty")

print(items_captured, captured)
