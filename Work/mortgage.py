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


# Exercise 1.9
def mortgage_calculator_ex_1_9(
    extra_payment_start_month,
    extra_payment_end_month,
    extra_payment,
):
    principal = 500_000.
    rate = 0.05
    payment = 2684.11
    total_paid = 0.
    num_month = 0

    while principal > 0:
        num_month += 1
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

        if extra_payment_start_month < num_month <= extra_payment_end_month:
            principal -= extra_payment
            total_paid += extra_payment

        # Exercise 1.10, 1.11 (add-on)
        if principal < 0:
            total_paid += principal
            principal = 0

        print(f"{num_month} {total_paid:.2f} {principal:.2f}")

    print(f"Total paid {total_paid:.1f} over {num_month} months.")


if __name__ == "__main__":
    mortgage_calculator_ex_1_9(60, 108, 1000)
