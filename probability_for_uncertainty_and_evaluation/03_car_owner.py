# Python Script: Conditional Probability of Car Ownership Given Woman
# Calculates P(Car | Woman) given P(Woman and Car) = 0.20

# Step 1: Define given probability
p_woman_and_car = 0.20  # Joint probability P(Woman ∩ Car)

# Step 2: Assume P(Woman) (probability an adult is a woman)
p_woman = 0.5  # Assumption: 50% of adults are women

# Step 3: Calculate conditional probability P(Car | Woman)
p_car_given_woman = p_woman_and_car / p_woman

# Step 4: Print result
print(f"P(Woman and Car): {p_woman_and_car * 100}%")
print(f"Assumed P(Woman): {p_woman * 100}%")
print(f"P(Car | Woman): {p_car_given_woman * 100:.1f}%")

# Optional: Test with different P(Woman) values
p_woman_alt = 0.4
p_car_given_woman_alt = p_woman_and_car / p_woman_alt
print(f"\nIf P(Woman) = {p_woman_alt * 100}%:")
print(f"P(Car | Woman): {p_car_given_woman_alt * 100:.1f}%")