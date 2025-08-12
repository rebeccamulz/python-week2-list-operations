# Week Two Assignment - List Operations 
"""
Week Two Assignment - List Operations
Author: [Your Name]
Description: This program demonstrates various list operations including 
append, insert, extend, remove, sort, and index methods.
"""

def main():
    print("=== Week 2 Assignment - List Operations ===\n")
    
    # Step 1: Create an empty list called my_list
    my_list = []
    print("1. Created empty list:")
    print(f"   my_list = {my_list}\n")
    
    # Step 2: Append the following elements to my_list: 10, 20, 30, 40
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print("2. After appending 10, 20, 30, 40:")
    print(f"   my_list = {my_list}\n")
    
    # Step 3: Insert the value 15 at the second position in the list
    my_list.insert(1, 15)  # Index 1 is the second position
    print("3. After inserting 15 at second position (index 1):")
    print(f"   my_list = {my_list}\n")
    
    # Step 4: Extend my_list with another list: [50, 60, 70]
    my_list.extend([50, 60, 70])
    print("4. After extending with [50, 60, 70]:")
    print(f"   my_list = {my_list}\n")
    
    # Step 5: Remove the last element from my_list
    removed_element = my_list.pop()  # pop() removes and returns last element
    print("5. After removing the last element:")
    print(f"   Removed element: {removed_element}")
    print(f"   my_list = {my_list}\n")
    
    # Step 6: Sort my_list in ascending order
    my_list.sort()
    print("6. After sorting in ascending order:")
    print(f"   my_list = {my_list}\n")
    
    # Step 7: Find and print the index of the value 30 in my_list
    index_of_30 = my_list.index(30)
    print("7. Finding index of value 30:")
    print(f"   Index of 30: {index_of_30}")
    print(f"   Verification: my_list[{index_of_30}] = {my_list[index_of_30]}\n")
    
    # Final result
    print("=== Final Result ===")
    print(f"my_list = {my_list}")
    print(f"Length of list: {len(my_list)}")

if __name__ == "__main__":
    main()