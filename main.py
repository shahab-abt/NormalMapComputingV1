# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pathlib import Path

import perfektVektor


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
path = Path("data.npy")
if not path.is_file():
    perfektVektor.create_perfect_vector(950,950)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
