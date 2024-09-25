class Graph:
    def __init__(self, nodes):
        self.nodes = nodes  

    def add_neighbour(node):
        return True

class Node:
    def __init__(self, name: str, neighbours: list):
        self.name = name
        self.neighbours = neighbours
    
    def add_neighbour(self, neighbour: str):
        self.neighbours.append(neighbour)
    
    def get_neighbours(self) -> list:
        return self.neighbours

def search_for_stuffed_animal(input):
    lists = sort_input(input)
    store_inventory = lists[0]
    bought_items = lists[1]
    possible = True
    stores = []
    number_of_stores = 1
    for items in store_inventory:
        stores.append(Node(items, []))
        number_of_stores += 1
    


def sort_input(input):
    line_number = 1
    K = 0
    store_inventory = []
    bought_items = []
    with open(input, 'r') as file:
        for line in file:
            if line_number == 2:
                K = int(line)
            elif line_number > 2 and line_number <= 2+K:
                store_inventory.append(line[2:].strip())
            elif line_number > 3+K:
                bought_items.append(line.strip())
            line_number += 1
    return store_inventory, bought_items


file = "eksterne_filer\sample-testcase1.in"

#search_for_stuffed_animal(file)
sort_input(file)