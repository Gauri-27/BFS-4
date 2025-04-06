from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Flatten board into a 1D list following the snake and ladder pattern
        def get_board_position(num):
            """Convert 1D index to 2D board coordinates correctly."""
            row = (num - 1) // n
            col = (num - 1) % n
            if row % 2 == 1:  # Reverse direction for odd rows
                col = n - 1 - col
            return n - 1 - row, col

        # Flatten board values
        nums = [-1] * (n * n)
        for i in range(n * n):
            r, c = get_board_position(i + 1)
            nums[i] = board[r][c] - 1 if board[r][c] != -1 else -1
        
        # BFS for shortest path
        queue = deque([0])  # Start from position 1 (index 0)
        moves = 0
        visited = set()
        visited.add(0)
        
        while queue:
            size = len(queue)
            moves += 1  # Each level in BFS represents a move
            
            for _ in range(size):
                curr = queue.popleft()
                
                for dice in range(1, 7):  # Simulate dice roll
                    child = curr + dice
                    if child >= n * n:
                        continue
                    
                    # Move to the destination if a ladder/snake exists
                    destination = nums[child] if nums[child] != -1 else child
                    
                    # Check if we reached the final square
                    if destination == n * n - 1:
                        return moves
                    
                    # Visit if not visited
                    if destination not in visited:
                        visited.add(destination)
                        queue.append(destination)
        
        return -1  # If no path to the end
# TC : O(n^2)
# SC : O(n^2)