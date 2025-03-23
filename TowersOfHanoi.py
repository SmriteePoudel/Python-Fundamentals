def towers_of_hanoi(n, source, auxiliary, target):
    """
    Solves the Towers of Hanoi problem recursively.
    
    Args:
        n: Number of disks
        source: Source rod (where disks start)
        auxiliary: Auxiliary rod (used as helper)
        target: Target rod (where disks should end up)
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
 
    towers_of_hanoi(n-1, source, target, auxiliary)
    
    
    print(f"Move disk {n} from {source} to {target}")
    
  
    towers_of_hanoi(n-1, auxiliary, source, target)

def visualize_towers(n):
    """
    Visualizes the step-by-step solution for the Towers of Hanoi problem.
    
    Args:
        n: Number of disks
    """

    towers = {
        'A': list(range(n, 0, -1)), 
        'B': [],                     
        'C': []                     
    }
    
    move_count = 0
    
    def display_towers():
        print("\nCurrent state of towers:")
        max_height = n
        
        # Display the towers row by row from top to bottom
        for i in range(max_height):
            row = ""
            for tower in ['A', 'B', 'C']:
                if i < max_height - len(towers[tower]):
                    row += "      |      "
                else:
                    disk = towers[tower][i - (max_height - len(towers[tower]))]
                    disk_str = str(disk).center(13)
                    row += disk_str
            print(row)
        
        # Display tower labels
        print("     A           B           C     ")
        print("-" * 39)
    
    def move_disk(source, target):
        nonlocal move_count
        move_count += 1
        
      
        disk = towers[source].pop()
        towers[target].append(disk)
        
        print(f"\nMove {move_count}: Disk {disk} from {source} to {target}")
        display_towers()
    
    def solve(n, source, auxiliary, target):
        if n == 1:
            move_disk(source, target)
            return
        
        solve(n-1, source, target, auxiliary)
        move_disk(source, target)
        solve(n-1, auxiliary, source, target)
    
  
    print("\nInitial state:")
    display_towers()
    
   
    solve(n, 'A', 'B', 'C')
    
    print(f"\nPuzzle solved in {move_count} moves!")


if __name__ == "__main__":
    print("Towers of Hanoi - Recursive Solution")
    print("------------------------------------")

    print("\nRecursive solution steps for 3 disks:")
    towers_of_hanoi(3, 'A', 'B', 'C')
    

    print("\n\nVisualized solution for 3 disks:")
    visualize_towers(3)
    
    
