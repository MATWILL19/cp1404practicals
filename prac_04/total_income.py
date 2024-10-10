"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_report(incomes, number_of_months)

def print_report(incomes, number_of_months):
    """Print the income report"""
    print("\nIncome Report\n-------------")
    total_income = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total_income = calculate_total_income(total_income, income)
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total_income))

def calculate_total_income(total_income, income):
    """Calculate the total income"""
    total_income += income
    return total_income

main()