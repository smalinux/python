
import termcolor
import pyfiglet


def main():
    x = pyfiglet.figlet_format("Sohaib")
    x = termcolor.colored(x, "red")
    print(x)

main()
