"""
import queue

def tree(index):
    fifo_queue = queue.Queue()
    fifo_queue.put("11")
    for i in range(index):
        parent = fifo_queue.get()
        leaf_one = parent[0]+str(int(parent[0])+int(parent[1]))
        leaf_two = str(int(parent[0])+int(parent[1]))+parent[1]
        fifo_queue.put(leaf_one)
        fifo_queue.put(leaf_two)   
    return fifo_queue.get()
    

def find_leaf(round, index):
    leaf = tree(index-1)
    return str(round)+" "+leaf[0]+"/"+leaf[1]

inputs = "4\n1 1\n2 4\n3 11\n4 1431655765"
listed = inputs.split()
for i in range(1, len(listed), 2):
    print(find_leaf(int(listed[i]), int(listed[i+1])))
"""
import sys

def calculate_leaf(index):
    p, q = 1, 1
    
    for bit in bin(index)[3:]:
        if bit == '0':
            q = p + q
        else:
            p = p + q
    
    return p, q

def find_leaf(round, index):
    p, q = calculate_leaf(index)
    return f"{round} {p}/{q}"


input = sys.stdin.read
inputs = input().split()

num_cases = int(inputs[0])
for i in range(1, num_cases * 2, 2):
    round_num = int(inputs[i])
    index = int(inputs[i + 1])
    print(find_leaf(round_num, index))