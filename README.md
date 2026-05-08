# Matrix-Based Budget Analysis System

A terminal-based Python program that uses matrix multiplication to track and analyse personal spending across categories and weeks.

## Overview

This program models a budgeting problem using Linear Algebra. Spending data is stored in an expense matrix, a weight vector of ones is used to sum across weeks, and matrix multiplication produces category totals in a single operation.

Mathematical model:

    E  (m x n)  --  expense matrix  (rows = categories, columns = weeks)
    W  (n x 1)  --  weight vector of ones
    T  = E x W  --  total spending per category
    Balance     = Income - sum(T)

## Requirements

- Python 3.8 or higher
- NumPy

Install the dependency:
```
pip install numpy
```

## Usage

Run the program from the terminal:
```
python matrix-budget.py
```

The program will guide you through:

1. Number of spending categories
2. Category names
3. Number of weeks to track
4. Expenses for each category per week
5. Your total income for the period

Results are displayed as a formatted report showing the expense matrix, category totals, and remaining balance.

## Sample Output

![Example Output](https://i.imgur.com/EmhdlIZ.png)
![Example Output](https://i.imgur.com/qjbq5Jt.png)
![Example Output](https://i.imgur.com/SfhtF7M.png)

## Project Structure

```
matrix-budget/
└── matrix-budget.py              # main program
```

## Notes

- All input is validated. The program rejects non-numeric values, negative amounts, zero counts, and blank names.
- Terminal colours require a terminal that supports ANSI escape codes. Most modern terminals on Linux, macOS, and Windows 10+ support this by default.
- Press Ctrl+C at any time to exit cleanly.

## Author

[Tako Nellyvine Mizero](https://github.com/Nellyvine)