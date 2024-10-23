import json
class Geneva:
    def __init__(self):
        self.been_before = False
        self.has_done_intro = False
        with open('scripts/geneva.json', 'r') as f:
            self.script = json.load(f)

    def main_room(self):
        for string in self.script['main']['init']['print']:
            print(string)
        match input(self.script['question']).upper():
            case "BEDROOM":
                self.bedroom()
            case "HALL":
                self.hall()
            case "OPTIONS" | "PRINT":
                print(self.script['main']['init']['options'])
                self.main_room()
            case _:
                self.main_room()

    def bedroom(self):
        for string in self.script['bedroom']['init']['print']:
            print(string)
        match input(self.script['question']).upper():
            case "READ" | "DIARY":
                self.has_done_intro = True
                for string in self.script['bedroom']['diary']['print']:
                    print(string)
            case "HALL":
                self.hall()
            case "BACK" | "MAIN":
                self.main_room()
            case "OPTIONS" | "PRINT":
                self.bedroom()
            case _:
                self.bedroom()

    def hall(self):
        if self.has_done_intro:
            for string in self.script['hall']['print']:
                print(string)
            match input("What would you like to do:").upper():
                case "OPTIONS" | "PRINT":
                    print("""PARTY/GO: Go to the baths near Thonton
                    Bedroom: Go to the bedroom
                    Options/Print: Print options
                    Back/Main: Go to the main room
                    """)
                    self.hall()
                case "BACK" | "MAIN":
                    self.main_room()
                case "BEDROOM":
                    self.bedroom()
                case "PARTY" | "GO":
                    self.been_before = True
                case _:
                    self.hall()
        else:
            print(self.script['hall']['default'])
            match input("What would you like to do:").upper():
                case "OPTIONS" | "PRINT":
                    print("""Bedroom: Go to the bedroom
                    Options/Print: Print options
                    Back/Main: Go to the main room
                    """)
                    self.hall()
                case "BACK" | "MAIN":
                    self.main_room()
                case "BEDROOM":
                    self.bedroom()
                case _:
                    self.hall()

    def play(self):
        self.been_before = True
        self.main_room()