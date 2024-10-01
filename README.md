# MSCS-532-Assignment7

# Hash Table Performance Comparison

## Overview

This Python program compares the performance of two hash table collision resolution techniques:
1. **Open Addressing** 
2. **Separate Chaining**

The program evaluates:
- Insertion time
- Search time
- Memory usage

It generates graphs to visually compare the performance of these techniques and saves the graphs as image files. The results are also printed to the console for easy reference.

## How It Works

- **Open Addressing** resolves collisions by probing for the next available slot in the hash table.
- **Separate Chaining** resolves collisions by storing multiple items in a linked list at the same hash index.

### Features:
- Measures insertion and search times for both Open Addressing and Separate Chaining.
- Measures memory usage for each method.
- Outputs results to the console.
- Saves bar charts comparing:
  - Insertion times
  - Search times
  - Memory usage
  
### Graphs saved as:
- `insert_time_comparison.png`
- `search_time_comparison.png`
- `memory_usage_comparison.png`

## Requirements

- Python 3.x
- `matplotlib` for plotting graphs


## Running the Program

1. **Clone the Repository** or copy the source code into your local directory.
2. **Ensure you have Python 3.x** installed on your machine.
3. **Install the required dependencies** using the following command:
   ```bash
   pip install matplotlib
4. Run the Python script in your terminal or any Python IDE
python hash_table_comparison.py or python3 hash_table_comparison.py depending on your configuration



