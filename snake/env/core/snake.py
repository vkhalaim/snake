import numpy as np

from settings.constants import DIRECTIONS, SNAKE_BLOCK


class Snake:
    def __init__(self, head_position, direction_index, length):
        """
        @param head_position: tuple
        @param direction_index: int
        @param length: int
        """
        # Information snake need to know to make the move
        self.snake_block = SNAKE_BLOCK
        self.current_direction_index = direction_index
        # Alive identifier
        self.alive = True
        # Place the snake
        self.blocks = [head_position]
        current_position = np.array(head_position)
        for i in range(1, length):
            # Direction inverse of moving
            current_position = (
                current_position - DIRECTIONS[self.current_direction_index]
            )
            self.blocks.append(tuple(current_position))

    def is_opposite(self, action):
        if action == 0 and self.current_direction_index == 2:
            return True
        elif action == 1 and self.current_direction_index == 3:
            return True
        elif action == 2 and self.current_direction_index == 0:
            return True
        elif action == 3 and self.current_direction_index == 1:
            return True
        
        return False

    def step(self, action):
        """
        @param action: int
        @param return: tuple, tuple
        """
        # Check if action can be performed (do nothing if in the same direction or opposite)
        if action == self.current_direction_index or self.is_opposite(action): 
            pass
        else:
            self.current_direction_index = action
        # Remove tail
        tail = self.blocks[-1]
        self.blocks = self.blocks[:-1]
        # Check new head
        new_head = self.blocks[0] + DIRECTIONS[self.current_direction_index]
        # Add new head
        self.blocks = [tuple(new_head)] + self.blocks
        return new_head, tail
