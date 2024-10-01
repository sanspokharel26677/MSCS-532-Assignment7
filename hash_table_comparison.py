import time
import random
import sys
import matplotlib.pyplot as plt

"""
This Python program compares the performance of two hash table collision resolution techniques: 
1. Open Addressing 
2. Separate Chaining
The program measures:
    - Insertion time
    - Search time
    - Memory usage for each method
It then generates graphs to compare the performance of these techniques and prints the results to the console. 
The graphs are also saved as image files in the current directory.
"""

# Simple hash function for demonstration
def hash_function(key, size):
    return key % size

# Hash Table using Open Addressing
class HashTableOpenAddressing:
    def __init__(self, size):
        # Create a table with None values to represent empty slots
        self.size = size
        self.table = [None] * size
    
    def insert(self, key, value):
        # Get the hash value using our hash function
        hash_value = hash_function(key, self.size)
        # Keep probing (linear probing) until we find an empty slot
        while self.table[hash_value] is not None:
            hash_value = (hash_value + 1) % self.size  # Linear probing
        # Insert the key-value pair in the table
        self.table[hash_value] = (key, value)
    
    def search(self, key):
        # Get the hash value to locate the key
        hash_value = hash_function(key, self.size)
        # Continue searching until we find the key or an empty slot
        while self.table[hash_value] is not None:
            if self.table[hash_value][0] == key:
                return self.table[hash_value][1]  # Return the found value
            hash_value = (hash_value + 1) % self.size
        return None  # Key not found
    
    def get_memory_usage(self):
        # Calculate memory usage by getting the size of the table and its contents
        total_size = sys.getsizeof(self.table)
        for item in self.table:
            if item is not None:
                total_size += sys.getsizeof(item)
        return total_size

# Hash Table using Separate Chaining
class HashTableSeparateChaining:
    def __init__(self, size):
        # Initialize a list of lists (chains) at each index
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def insert(self, key, value):
        # Hash the key to determine which chain to use
        hash_value = hash_function(key, self.size)
        # Append the key-value pair to the appropriate chain
        self.table[hash_value].append((key, value))
    
    def search(self, key):
        # Hash the key to find the chain
        hash_value = hash_function(key, self.size)
        # Iterate over the chain to search for the key
        for pair in self.table[hash_value]:
            if pair[0] == key:
                return pair[1]  # Return the found value
        return None  # Key not found
    
    def get_memory_usage(self):
        # Calculate memory usage by adding sizes of chains and their contents
        total_size = sys.getsizeof(self.table)
        for chain in self.table:
            total_size += sys.getsizeof(chain)
            for item in chain:
                total_size += sys.getsizeof(item)
        return total_size

# Function to measure performance and memory usage
def measure_performance_and_memory(hash_table, num_elements):
    # Measure the time taken for insertions
    start_time = time.time()
    for i in range(num_elements):
        key = random.randint(1, 100000)
        hash_table.insert(key, f"value{i}")
    insert_time = time.time() - start_time
    
    # Measure the time taken for searches
    start_time = time.time()
    for i in range(num_elements // 2):
        key = random.randint(1, 100000)
        hash_table.search(key)
    search_time = time.time() - start_time
    
    # Calculate memory usage
    memory_usage = hash_table.get_memory_usage()
    
    return insert_time, search_time, memory_usage

# Function to plot the results and save images
def plot_results(results):
    # Unpack the results for plotting
    labels, insert_times, search_times, memory_usages = zip(*results)
    
    # Plot the insert times
    plt.figure()
    plt.bar(labels, insert_times, color='blue')
    plt.title("Insert Time Comparison")
    plt.ylabel("Time (seconds)")
    plt.savefig("insert_time_comparison.png")
    plt.show()

    # Plot the search times
    plt.figure()
    plt.bar(labels, search_times, color='green')
    plt.title("Search Time Comparison")
    plt.ylabel("Time (seconds)")
    plt.savefig("search_time_comparison.png")
    plt.show()

    # Plot the memory usages
    plt.figure()
    plt.bar(labels, memory_usages, color='red')
    plt.title("Memory Usage Comparison")
    plt.ylabel("Memory (bytes)")
    plt.savefig("memory_usage_comparison.png")
    plt.show()

# Experiment settings
table_size = 1000  # Size of the hash table
num_elements = 800  # 80% load factor (number of elements to insert)

# Test for Open Addressing
open_addressing_table = HashTableOpenAddressing(table_size)
open_addressing_insert_time, open_addressing_search_time, open_addressing_memory_usage = measure_performance_and_memory(open_addressing_table, num_elements)

# Test for Separate Chaining
separate_chaining_table = HashTableSeparateChaining(table_size)
separate_chaining_insert_time, separate_chaining_search_time, separate_chaining_memory_usage = measure_performance_and_memory(separate_chaining_table, num_elements)

# Collect the results for both strategies
results = [
    ("Open Addressing", open_addressing_insert_time, open_addressing_search_time, open_addressing_memory_usage),
    ("Separate Chaining", separate_chaining_insert_time, separate_chaining_search_time, separate_chaining_memory_usage)
]

# Plot the results
plot_results(results)

# Print the results to the console
for label, insert_time, search_time, memory_usage in results:
    print(f"{label} - Insert Time: {insert_time:.6f} seconds")
    print(f"{label} - Search Time: {search_time:.6f} seconds")
    print(f"{label} - Memory Usage: {memory_usage} bytes")
    print()

