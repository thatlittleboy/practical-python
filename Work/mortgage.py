# mortgage.py
#
# Exercise 1.8
def mortgage_calculator_ex_1_8():
    principal = 500_000.
    rate = 0.05
    payment = 2684.11
    total_paid = 0.
    num_month = 0

    while principal > 0:
        num_month += 1
        extra_payment = 1_000 if num_month <= 12 else 0
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment

    print(f"Total paid {total_paid:.1f} over {num_month} months.")


