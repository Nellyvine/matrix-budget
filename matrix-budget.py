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

#  helper: draw a horizontal line
def line(char="─", width=60, color=CYAN):
    print(f"{color}{char * width}{RESET}")


#  helper: print a section header
def header(title):
    print()
    line("═", 60, CYAN)
    print(f"{BOLD}{CYAN}  {title}{RESET}")
    line("═", 60, CYAN)


#  helper: get a positive integer from the user
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


#  helper: get a positive float from the user
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


#  helper: get a non-empty category name
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

#  STEP 1 – welcome banner

def show_banner():
    print()
    line("═", 60, MAGENTA)
    print(f"{BOLD}{MAGENTA}{'Matrix-Based Budget Analysis System':^60}{RESET}")
    print(f"{DIM}{'Linear Algebra Application  |  Matrix Multiplication':^60}{RESET}")
    line("═", 60, MAGENTA)
    print()
    print(f"  {WHITE}This program uses matrix multiplication to compute{RESET}")
    print(f"  {WHITE}your spending totals across categories and weeks.{RESET}")
    print()

#  STEP 2 – collect category info

def get_categories():
    header("Step 1 │ Categories")
    n = get_positive_int("  How many spending categories do you have? : ")

    categories = []
    print()
    for i in range(n):
        name = get_category_name(f"  Name of category {i + 1}             : ")
        categories.append(name)

    return categories

#  STEP 3 – collect week count

def get_weeks():
    header("Step 2 │ Time Period")
    weeks = get_positive_int("  How many weeks do you want to track? : ")
    return weeks

#  STEP 4 – build the expense matrix E

def build_expense_matrix(categories, weeks):
    """
    I build matrix E where:
      - each ROW    = one spending category
      - each COLUMN = one week
    So E has shape  (num_categories × num_weeks).
    """
    header("Step 3 │ Enter Expenses")
    print(f"  {DIM}Enter the amount you spent in each category for each week.{RESET}")
    print()

    n_cat  = len(categories)
    # I initialise the matrix with zeros first
    E = np.zeros((n_cat, weeks))

    for i, cat in enumerate(categories):
        print(f"  {BLUE}{BOLD}► {cat}{RESET}")
        for j in range(weeks):
            prompt = f"      Week {j + 1} expense (Rs): "
            E[i][j] = get_positive_float(prompt)
        print()

    return E

#  STEP 5 – matrix multiplication  E × W = T

def compute_totals(E):
    """
    I create a weight vector W filled with 1s.
    When I multiply E × W the result T gives me
    the total spending per category (summing all weeks).

    Dimensions check:
      E  →  (n_categories × n_weeks)
      W  →  (n_weeks      × 1     )
      T  →  (n_categories × 1     )

    If the inner dimensions do not match numpy will
    raise an error automatically, but I also validate
    manually to give the user a clear message.
    """
    _, n_weeks = E.shape

    # I create the ones vector W
    W = np.ones((n_weeks, 1))

    # Dimension compatibility check (just to be explicit)
    if E.shape[1] != W.shape[0]:
        raise ValueError(
            f"Matrix multiplication error: E has {E.shape[1]} columns "
            f"but W has {W.shape[0]} rows. Dimensions are incompatible."
        )

    # I perform the actual matrix multiplication here
    T = E @ W          # shape: (n_categories, 1)
    return T, W

#  STEP 6 – get income and compute balance

def get_income():
    header("Step 4 │ Your Income")
    income = get_positive_float("  Enter your total income for this period (Rs): ")
    return income

#  STEP 7 – display results

def display_results(categories, E, W, T, income, weeks):
    header("Results │ Budget Analysis Report")

    #  7a: show the raw expense matrix
    print(f"  {BOLD}{WHITE}Expense Matrix  E  ({len(categories)} × {weeks}){RESET}")
    print(f"  {DIM}Rows = categories  |  Columns = weeks{RESET}")
    print()

    # Column headers
    col_header = f"  {'Category':<18}" + "".join(
        f"{'Week ' + str(j + 1):>10}" for j in range(weeks)
    )
    print(f"{CYAN}{col_header}{RESET}")
    line("─", 60, DIM)

    for i, cat in enumerate(categories):
        row_str = f"  {cat:<18}"
        for j in range(weeks):
            row_str += f"{E[i][j]:>10.2f}"
        print(f"{WHITE}{row_str}{RESET}")

    print()

    #  7b: show the weight vector W
    print(f"  {BOLD}{WHITE}Weight Vector  W  (all 1s → sums across all weeks){RESET}")
    w_display = "  W = [ " + "  ".join(str(int(w[0])) for w in W) + " ]ᵀ"
    print(f"{CYAN}{w_display}{RESET}")
    print()

    #  7c: show T = E × W  per category
    line("─", 60, CYAN)
    print(f"  {BOLD}{WHITE}Category Totals  T = E × W{RESET}")
    line("─", 60, CYAN)

    total_spent = 0.0
    for i, cat in enumerate(categories):
        cat_total = T[i][0]
        total_spent += cat_total
        bar_len = int((cat_total / (income or 1)) * 30)
        bar = "█" * min(bar_len, 30)
        print(
            f"  {GREEN}{cat:<18}{RESET} "
            f"{WHITE}Rs {cat_total:>10.2f}{RESET}  "
            f"{BLUE}{bar}{RESET}"
        )

    #  7d: summary
    print()
    line("─", 60, CYAN)
    balance = income - total_spent
    balance_color = GREEN if balance >= 0 else RED
    balance_label = "Surplus ✔" if balance >= 0 else "Deficit ✘"

    print(f"  {WHITE}{'Total Income':<24}Rs {income:>10.2f}{RESET}")
    print(f"  {WHITE}{'Total Spent':<24}Rs {total_spent:>10.2f}{RESET}")
    print(
        f"  {balance_color}{BOLD}{'Balance  (' + balance_label + ')':<24}"
        f"Rs {balance:>10.2f}{RESET}"
    )
    line("─", 60, CYAN)

    #  7e: quick analysis message
    print()
    pct = (total_spent / income * 100) if income > 0 else 0
    print(f"  {DIM}You spent {pct:.1f}% of your income this period.{RESET}")

    if balance < 0:
        print(f"  {RED}⚠  You have exceeded your income by Rs {abs(balance):.2f}.{RESET}")
    elif pct > 80:
        print(f"  {YELLOW}⚠  You are spending more than 80% of your income.{RESET}")
    else:
        print(f"  {GREEN}✔  Your spending looks manageable. Keep it up!{RESET}")

    print()
    line("═", 60, MAGENTA)
    print(f"{BOLD}{MAGENTA}{'End of Report':^60}{RESET}")
    line("═", 60, MAGENTA)
    print()

#  MAIN – I tie everything together here

def main():
    show_banner()

    try:
        # I collect all the inputs one section at a time
        categories = get_categories()
        weeks      = get_weeks()
        E          = build_expense_matrix(categories, weeks)

        # I perform the matrix multiplication E × W = T
        T, W = compute_totals(E)

        # I get the income last so the user has context
        income = get_income()

        # I show the full report
        display_results(categories, E, W, T, income, weeks)

    except KeyboardInterrupt:
        # I handle Ctrl+C gracefully so the terminal does not look broken
        print(f"\n\n  {YELLOW}Program interrupted by user. Goodbye!{RESET}\n")


# I only run main() when this file is executed directly
if __name__ == "__main__":
    main()
