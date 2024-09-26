import os

class Graphics:
    @staticmethod
    def clear_screen():
        # Check the operating system and clear the terminal screen
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For macOS, Linux, Chromebook, etc.
            os.system('clear')

    @staticmethod
    def draw():
        # Draws the ground and objects to the screen
        global line_length, lines
        hold = ""
        Graphics.clear_screen()  # Clear the screen first
        i = 0
        while i < len(ground):
            if ground[i] != "*":
                hold += ground[i]  # Collect characters until end of line
            else:
                print(hold)  # Print one line at a time
                hold = ""
            i += 1
        print(hold)  # Print any remaining line content

    @staticmethod
    def lengths():
        # Calculates the length of each line and number of lines
        global line_length, lines
        hold = ""
        i, lines = 0, 0
        while i < len(ground):
            if ground[i] != "*":
                hold += ground[i]
            else:
                lines += 1
                if line_length == 0:
                    line_length = i  # Set line length only once on the first line
                hold = ""
            i += 1

    @staticmethod
    def find(x, y):
        # Converts (x, y) coordinates into an index for the `ground` array
        return (y * line_length) + x

    @staticmethod
    def what_at(x, y):
        # Returns the character at a specific (x, y) position
        return ground[Graphics.find(x, y)]

    @staticmethod
    def change(x, y, thing):
        # Changes the content at a specific (x, y) position
        ground[Graphics.find(x, y)] = thing

    @staticmethod
    def input_wait(group, button):
        # Waits for user input based on the group (e.g., "arrowkeys", "wasd", or "none")
        if group == "none":
            inputed = ""
            while inputed != button:
                inputed = input("")
            return "pressed"
        elif group == "arrowkeys":
            groups = ["l", "r", "u", "d"]
            inputed = ""
            while inputed not in groups:
                inputed = input("")
                if inputed == "print":
                    print(ground)  # Typing "print" outputs the ground list for debugging
            return inputed
        elif group == "wasd":
            # Converts WASD input to arrow-like direction controls
            groups = ["w", "a", "s", "d"]
            inputed = ""
            while inputed not in groups:
                inputed = input("")
                if inputed == "print":
                    print(ground)  # Typing "print" outputs the ground list for debugging
            # Convert WASD input to corresponding arrow key directions
            if inputed == "w":
                return "u"  # Up
            elif inputed == "a":
                return "l"  # Left
            elif inputed == "s":
                return "d"  # Down
            elif inputed == "d":
                return "r"  # Right
