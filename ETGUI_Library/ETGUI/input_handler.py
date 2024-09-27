class InputHandler:
    @staticmethod
    def input_wait(group, button):
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
                    print(ground)
            return inputed
