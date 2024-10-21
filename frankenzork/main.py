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
        black ="\033[40m"
        white = "\033[47m"
        red = "\033[41m"
        yellow = "\033[43m"
        green = "\033[42m"
        blue = "\033[44m"
        purple = "\033[45m"
        cyan = "\033[46m"
    clear = "\033[0m"
class WelcomeScreen():
    def __init__(self) -> None:
        self.logo = r"""
        /‾‾‾‾‾‾/                           |‾|                      |‾‾‾‾‾‾|                  |‾|     
        |   __|  _ _____  ____ _   _ ___   | | ___   ____   _ ___    ‾‾‾/ /   ____    _ _____ | | ___ 
        |  |__  | |    / /  _ | | | '__ \  | |/  /  /    \ | '__ \     / /   /    \  | |    / | |/  / 
        |   __| |   /‾‾ |  ( |  | | |  \ | |    <  |  ‾‾ / | |  \ |   / /   | |‾‾| | |   /‾‾  |    <  
        |  |    |  |    |   ‾   | | |  | | | |\  \ |  ‾‾‾| | |  | |  / /__  |  ‾‾  | |  |     | |\  \ 
        /__|    |__|     \____|_| |_|  |_| |_| \__\ \____/ |_|  |_| |_____|  \____/  |__|     |_| \__\
        """

        self.figure = f"""
          {AnsiEscapes.fg.black}████████████{AnsiEscapes.clear}
         {AnsiEscapes.fg.black}█████████████{AnsiEscapes.clear}
         {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.red}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.black}█\t
         {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}███████{AnsiEscapes.fg.red}█{AnsiEscapes.fg.yellow}███{AnsiEscapes.fg.black}█\t
         {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}██{AnsiEscapes.fg.intense.white}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.intense.white}█{AnsiEscapes.fg.yellow}█{AnsiEscapes.fg.intense.white}█{AnsiEscapes.fg.black}█{AnsiEscapes.fg.intense.white}█{AnsiEscapes.fg.yellow}██{AnsiEscapes.fg.black}█\t
          {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}█████████{AnsiEscapes.fg.black}█\t
          {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}███{AnsiEscapes.bg.yellow}{AnsiEscapes.fg.black}▬▬▬{AnsiEscapes.fg.yellow}██{AnsiEscapes.fg.black}█{AnsiEscapes.clear}\t
           {AnsiEscapes.fg.black}██{AnsiEscapes.fg.yellow}█████{AnsiEscapes.fg.black}██\t
           {AnsiEscapes.fg.black}█{AnsiEscapes.fg.yellow}████{AnsiEscapes.fg.black}██
        """

        self.message = f"""
        \t{AnsiEscapes.fg.green}FRANKENZORK {AnsiEscapes.fg.red}I{AnsiEscapes.clear}: The creation of Frankenstein's monster.
        \tMade by {AnsiEscapes.fg.intense.green}nulladmin1{AnsiEscapes.clear}: {AnsiEscapes.fg.cyan}https://github.com/nulladmin1{AnsiEscapes.clear} 
          """
def main():
    welcomeScreen = WelcomeScreen()
    print(welcomeScreen.message)
    print(welcomeScreen.logo)
    print(welcomeScreen.figure)
if __name__ == "__main__":
    main()
