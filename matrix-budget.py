# Matrix-Based Budget Analysis System
# Topic : Matrix Operations (Linear Algebra)
# Purpose : I use matrix multiplication to track and analyse spending across categories and weeks

#I import numpy so I can do proper matrix multiplication easily

import numpy as np

# ANSI colour codes (I used these to make the terminal output look clean and organised)

RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BLUE   = "\033[94m"
MAGENTA= "\033[95m"
WHITE  = "\033[97m"
DIM    = "\033[2m"

# ── helper: draw a horizontal line ──
def line(char="─", width=60, color=CYAN):
    print(f"{color}{char * width}{RESET}")


# ── helper: print a section header ──
def header(title):
    print()
    line("═", 60, CYAN)
    print(f"{BOLD}{CYAN}  {title}{RESET}")
    line("═", 60, CYAN)


# ── helper: get a positive integer from the user ──
def get_positive_int(prompt):
    """
    I keep asking until the user gives me a whole
    number that is greater than zero.
    """
    while True:
        try:
            value = int(input(f"{YELLOW}{prompt}{RESET}"))
            if value <= 0:
                print(f"  {RED}⚠  Please enter a number greater than 0.{RESET}")
            else:
                return value
        except ValueError:
            print(f"  {RED}⚠  That is not a valid number. Try again.{RESET}")


# ── helper: get a positive float from the user ──
def get_positive_float(prompt):
    """
    I use this whenever I need a monetary amount.
    I reject negative values and non-numeric text.
    """
    while True:
        try:
            value = float(input(f"{YELLOW}{prompt}{RESET}"))
            if value < 0:
                print(f"  {RED}⚠  Amount cannot be negative.{RESET}")
            else:
                return value
        except ValueError:
            print(f"  {RED}⚠  Please enter a valid number (e.g. 250.50).{RESET}")


# ── helper: get a non-empty category name ──
def get_category_name(prompt):
    """
    I make sure the user does not leave a category name blank.
    """
    while True:
        name = input(f"{YELLOW}{prompt}{RESET}").strip()
        if name == "":
            print(f"  {RED}⚠  Category name cannot be empty.{RESET}")
        else:
            return name
