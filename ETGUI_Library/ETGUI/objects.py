class Objects:
    def __init__(self, x, y, obj_type, state):
        self.x = x
        self.y = y
        self.type = obj_type
        self.state = state

    def tp(self, x, y):
        Graphics.change(self.x, self.y, "_")
        Graphics.change(x, y, self.state)

    def object_draw(self):
        Graphics.change(self.x, self.y, self.state)

    def move(self, direction):
        global line_length, ground_tile, lines
        dx, dy = 0, 0
        
        if direction == "d":
            dy = 1
        elif direction == "u":
            dy = -1
        elif direction == "l":
            dx = -1
        elif direction == "r":
            dx = 1

        new_x = self.x + dx
        new_y = self.y + dy

        # Ensure movement is within bounds
        if 0 <= new_x < line_length and 0 <= new_y < lines:
            # Restore the ground tile where the object was
            Graphics.change(self.x, self.y, ground_tile)
            
            # Move the object
            self.x, self.y = new_x, new_y

            # Update the ground tile at the new position
            ground_tile = Graphics.what_at(self.x, self.y)

            # Redraw the object
            Graphics.change(self.x, self.y, "\U0001f600")  # Emoji or custom state
