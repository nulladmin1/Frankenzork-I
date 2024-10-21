class AnsiiEscapes:
    class fg:
        black = "\033[30m"
        white = "\033[37m"
        red = "\033[31m"
        yellow = "\033[33m"
        green = "\033[32m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"
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
        self.message = f"""
         {AnsiiEscapes.fg.black}█████████████{AnsiiEscapes.clear} {AnsiiEscapes.fg.green}FRANKENZORK {AnsiiEscapes.fg.red}I{AnsiiEscapes.clear}: The creation of Frankenstein's monster.
         {AnsiiEscapes.fg.black}█████████████{AnsiiEscapes.clear} Made by {AnsiiEscapes.fg.green}nulladmin1{AnsiiEscapes.clear}: {AnsiiEscapes.fg.cyan}https://github.com/nulladmin1{AnsiiEscapes.clear} 
         {AnsiiEscapes.fg.black}█{AnsiiEscapes.fg.green}█{AnsiiEscapes.fg.black}█{AnsiiEscapes.fg.green}█{AnsiiEscapes.fg.black}█{AnsiiEscapes.fg.green}█{AnsiiEscapes.fg.black}█{AnsiiEscapes.fg.green}█{AnsiiEscapes.fg.black}█{AnsiiEscapes.fg.green}█

        """

def main():
    welcomeScreen = WelcomeScreen()
    print(welcomeScreen.message)

if __name__ == "__main__":
    main()
