# mortgage.py
#
# Exercise 1.7
principal = 500_000.
rate = 0.05
payment = 2684.11
total_paid = 0.

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

print(f"Total paid {total_paid:.1f}")
