import os
import platform

def clear_console():
    # Check the operating system
    if platform.system() == "Windows":
        os.system('cls')  # Clear console for Windows
    else:
        os.system('clear')  # Clear console for Unix/Linux/MacOS

# Example usage
print("This is the first output")
input("Press Enter to clear the screen...")
clear_console()
print("The screen has been cleared!")

