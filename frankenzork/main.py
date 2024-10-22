import json


class AnsiEscapes:
    class fg:
        black = "\033[30m"
        white = "\033[37m"
        red = "\033[31m"
        yellow = "\033[33m"
        green = "\033[32m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"

        class intense:
            black = "\033[90m"
            white = "\033[97m"
            red = "\033[91m"
            yellow = "\033[93m"
            green = "\033[92m"
            blue = "\033[94m"
            purple = "\033[95m"
            cyan = "\033[96m"

    class bg:
        black = "\033[40m"
        white = "\033[47m"
        red = "\033[41m"
        yellow = "\033[43m"
        green = "\033[42m"
        blue = "\033[44m"
        purple = "\033[45m"
        cyan = "\033[46m"

    clear = "\033[0m"

class Geneva:
    def __init__(self):
        self.been_before = False
        self.has_done_intro = False
        with open('scripts/geneva.json', 'r') as f:
            self.script = json.load(f)

    def main_room(self):
        for string in self.script['main']['init']['print']:
            print(string)
        match input("Where would you like to do: ").upper():
            case "BEDROOM":
                self.bedroom()
            case "HALL":
                self.hall()
            case "OPTIONS" | "PRINT":
                print("""Hall: Go to the hall\nBedroom: Go to the bedroom\nOptions/Print: Print options""")
                self.main_room()
            case _:
                self.main_room()

    def bedroom(self):
        for string in self.script['bedroom']['init']['print']:
            print(string)
        match input("What would you like to do:").upper():
            case "READ" | "DIARY":
                self.has_done_intro = True
                for string in self.script['bedroom']['diary']['print']:
                    print(string)
            case "HALL":
                self.hall()
            case "BACK" | "MAIN":
                self.main_room()
            case "OPTIONS" | "PRINT":
                print("Read/Diary: Read the diary\nMain room: Go to the main room\nHall: Go to the hall\nOptions/Print: Print options")
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


class Game:
    def __init__(self):
        geneva = Geneva()
        self.rooms = (geneva,)

    def start(self):
        for room in self.rooms:
            room.play()


class WelcomeScreen:
    def __init__(self) -> None:
        self.logo = f"""
          {AnsiEscapes.fg.black}████████████{AnsiEscapes.clear}
         {AnsiEscapes.fg.black}█████████████{AnsiEscapes.clear} \t{AnsiEscapes.fg.green}         /‾‾‾‾‾‾/                           |‾|              {AnsiEscapes.fg.blue}        |‾‾‾‾‾‾|                  |‾|
         {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.red}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.black}█  \t   {AnsiEscapes.fg.green}  |   __|  _ _____  ____ _   _ ___   | | ___   ____   _ ___  {AnsiEscapes.fg.blue}  ‾‾‾/ /   ____    _ _____ | | ___    
         {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}███████{AnsiEscapes.fg.red}█{AnsiEscapes.fg.yellow}███{AnsiEscapes.fg.black}█\t    {AnsiEscapes.fg.green}     |  |__  | |    / /  _ | | | '__ \\  | |/  /  /    \\ | '__ \\  {AnsiEscapes.fg.blue}   / /   /    \\  | |    / | |/  /    
         {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}██{AnsiEscapes.fg.intense.white}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.intense.white}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.intense.white}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.intense.white}█{AnsiEscapes.fg.yellow}██{AnsiEscapes.fg.black}█\t   {AnsiEscapes.fg.green}      |   __| |   /‾‾ |  ( |  | | |  \\ | |    <  |  ‾‾ / | |  \\ |  {AnsiEscapes.fg.blue} / /   | |‾‾| | |   /‾‾  |    <            
          {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█████████{AnsiEscapes.fg.black}█\t       {AnsiEscapes.fg.green}  |  |    |  |    |   ‾   | | |  | | | |\\  \\ |  ‾‾‾| | |  | | {AnsiEscapes.fg.blue} / /__  |  ‾‾  | |  |     | |\\  \\        
          {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}███{AnsiEscapes.bg.yellow}{AnsiEscapes.fg.black}▬▬▬{AnsiEscapes.fg.yellow}██{AnsiEscapes.fg.black}█{AnsiEscapes.clear}\t    {AnsiEscapes.fg.green}     /__|    |__|     \\____|_| |_|  |_| |_| \\__\\ \\____/ |_|  |_| {AnsiEscapes.fg.blue}|_____|  \\____/  |__|     |_| \\__\\     
           {AnsiEscapes.fg.black}██{AnsiEscapes.fg.yellow}█████{AnsiEscapes.fg.black}██
           {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}████{AnsiEscapes.fg.black}██
        """

        self.message = f"""
        \t\t\t\t\t\t{AnsiEscapes.fg.green}FRANKENZORK {AnsiEscapes.fg.red}I{AnsiEscapes.clear}: The creation of Frankenstein's monster.
        \t\t\t\t\t\tMade by {AnsiEscapes.fg.intense.green}nulladmin1{AnsiEscapes.clear}: {AnsiEscapes.fg.cyan}https://github.com/nulladmin1{AnsiEscapes.clear} \n
        \tFrankenstein is often subject to misconception. The biggest example arguably is the fact that Frankenstein isn't
        \teven the name of the monster in the book: rather is the name of the doctor to created the being. The monster 
        \tisn't given a name. Frankenstein also, in society, is thought of to be a monstrous villain with green skin and 
        \tbolts in his neck, which this couldn't be further from the truth: Mary Shelley, the author of the novel, 
        \tintended the character's detail to be sparse, and all she told use was that the figure was meant to have stitches
        \tall over his body, be humongous in size, and have a pale yellow skin. This is why the figure in this message
        \tis yellow.\n\n"""

        self.welcome_message = self.logo + self.message

    def __str__(self):
        return self.welcome_message

    def run(self, game_instance: Game):
        print(self.welcome_message)
        action = input("""What do you want to do? 
                            1) Start the game
                            2) Exit
                            3) Print the welcome screen again""")
        match action:
            case '1':
                print("Remember that you can always ask what you can do by entering in 'options' or 'print'. All the options bolded valid options.")
                game_instance.start()
            case '3':
                self.run(game_instance)
            case _:
                pass


def main():
    welcome_screen = WelcomeScreen()
    print(welcome_screen)
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
