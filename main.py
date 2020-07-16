import sys
import os

from util import *

os.system("") # Needed to "trigger" coloured text
testArgs = ["-test", "-t"]
sPrintInfoArgs = ["-sprintinfo", "-spi"]
wrapTextArgs = ["-wrap", "-w"]
colorInfoArgs = ["-colorinfo", "-ci"]
allColorsArgs = ["-allcolors", "-ac"]
helpArgs = ["-help", "-h"]

class Main:
    def main():
        argC = len(sys.argv)
        argIndex = 1
        while argIndex < argC:
            arg = sys.argv[argIndex].lower()
            # print("arg: " + str(sys.argv[argIndex]))

            if(arg in testArgs):
                print(Util.wrapColor("test1", "OKBLUE"))
                print(Util.wrapColor("test2", 2))
                print(Util.wrapColor("test3", "\x1b[4;32;40m"))

                argIndex += 1
                continue

            if(arg in sPrintInfoArgs):
                booleanValue = True
                print("The following line uses sPrint() function:")
                Util.sPrint(1, 2, "Greetings", booleanValue)
                
                print("\nThe function takes in any number of arguments, converts them to string, and prints them.")
                print("This is much easier than doing print(str(x) + \" \" + str(y)) etc.")
                print("\nsPrint(*args)")

                argIndex += 1
                continue

            if(arg in wrapTextArgs):
                if(argC < 4):
                    print("Expected 3 arguments: [flag] [string] [string/int]")
                    argIndex += 1
                    continue
                    
                print(Util.wrapColor(sys.argv[argIndex + 1], sys.argv[argIndex + 2]))

                argIndex += 3
                continue

            if(arg in colorInfoArgs):
                print("'\\033[95m' and '\\x1b[95m' are the same.")
                print("'\\033[95m' and '\\x1b[95m' can be single quote (') or double (\").")
                print("'\\033[95m' + \"Text\" + \"\\033[95m\": " + '\033[95m' + "Text" + "\033[0m")
                print("'\\x1b[95m' + \"Text\" + \"\\033[95m\": " + '\x1b[95m' + "Text" + "\x1b[0m")
                print("'\\x1b[95m' + \"Text\" + \"\\x1b[95m\": " + '\x1b[95m' + "Text" + "\033[0m")
                print("")

                print("Python ?.??: " + Util.colors["WARNING"] + "Text" + Util.colors["ENDC"])
                print(f"Python 3.6+: {Util.colors['WARNING']}Text{Util.colors['ENDC']}")
                print("")

                print("Predefined Util colors:")
                print(Util.wrapColor("HEADER || 0", "HEADER"))
                print(Util.wrapColor("OKBLUE || 1", "OKBLUE"))
                print(Util.wrapColor("OKGREEN || 2", "OKGREEN"))
                print(Util.wrapColor("WARNING || 3", "WARNING"))
                print(Util.wrapColor("FAIL || 4", "FAIL"))
                print(Util.wrapColor("ENDC || 5", "ENDC"))
                print(Util.wrapColor("BOLD || 6", "BOLD"))
                print(Util.wrapColor("UNDERLINE || 7", "UNDERLINE"))

                print("Sources:")
                print("Different usage of colours, tips, libs, source of all colours function: \n\thttps://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python")
                print("Explain ANSI escape (\"\\033\", \"\\x1b\" = (ESC + [)): \n\thttps://stackoverflow.com/questions/15011478/ansi-questions-x1b25h-and-x1be")

                argIndex += 1
                continue

            if(arg in allColorsArgs):
                Main.printAllColours()
                argIndex += 1
                continue

            # Help
            elif(arg in helpArgs):
                Main.printHelp()
                quit()

            # Invalid, inform and quit
            else:
                print("Argument not recognized: \"" + arg + "\", please see documentation or run with \"-help\" for help.")

            argIndex += 1

        # No arguments, print all colours
        if(argC < 2):
            Main.printAllColours()

    # Functions

    # https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
    def printAllColours():
        """
        Prints all background/text colour combinations (it seems).
        """

        for style in range(8):
            for fg in range(30,38):
                s1 = ''
                for bg in range(40,48):
                    format = ';'.join([str(style), str(fg), str(bg)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                print(s1)
            print('\n')

    def printHelp():
        """
        A simple console print that informs user of program arguments.
        """

        print("--- Help ---")
        print("Arguments marked with ? are optional.")
        print("All arguments that triggers a function start with dash(-).")
        print("All arguments must be separated by space only.")
        print("\n")

        print(str(testArgs) + ": a method of calling experimental code (when you want to test if something works).")
        print(str(sPrintInfoArgs) + ": Print a small example of sPrint util function.")
        print(str(wrapTextArgs) + " \"[text]\" [color]: prints [text] in color [color].")
        print(str(colorInfoArgs) + ": Print a small explanation of what and how to use coloured text in terminal (with ASNI).")
        print(str(allColorsArgs) + ": prints all colours (see function description and link above it for more information).")
        print(str(helpArgs) + ": prints this information about input arguments.")

if __name__ == "__main__":
    Main.main()