# Python Script: Step-by-Step Explanation of Basic Algebra Concepts
# This script explains key algebra topics: Basic Algebra, Exponents, Logarithms, Polynomials, Factoring, and Quadratic Equations.
# It uses numpy for numerical computations and sympy for symbolic algebra (factoring, solving equations).
# Each section includes definitions, formulas, and Python examples with comments.
# Run this script to see outputs and learn through examples.

# Step 1: Import Necessary Libraries
# numpy for numerical computations (logarithms, polynomials)
# sympy for symbolic algebra (factoring, solving equations)
import numpy as np
import sympy as sp

# Step 2: Basic Algebra
# Basic Algebra involves operations with numbers and variables (e.g., x, y) to solve equations and model relationships.
# Key concepts:
# - Variables: Symbols representing numbers (e.g., x).
# - Constants: Fixed numbers (e.g., 5).
# - Expressions: Combinations of variables and constants (e.g., 2x + 3).
# - Equations: Statements that two expressions are equal (e.g., 2x + 3 = 7).
# - Linear Equations: Equations of degree 1 (e.g., ax + b = 0).

# Example: Solve a linear equation 2x + 3 = 7
print("\n--- Basic Algebra: Solving Linear Equation ---")
# Equation: 2x + 3 = 7
# Isolate x: 2x = 7 - 3 => 2x = 4 => x = 2
x = (7 - 3) / 2
print(f"Solving 2x + 3 = 7")
print(f"x = {x}")

# Step 3: Exponents
# Exponents represent repeated multiplication: a^n = a * a * ... * a (n times).
# Key properties:
# - Product Rule: a^m * a^n = a^(m+n)
# - Quotient Rule: a^m / a^n = a^(m-n)
# - Power Rule: (a^m)^n = a^(m*n)
# - Zero Exponent: a^0 = 1 (a ≠ 0)
# - Negative Exponent: a^(-n) = 1 / a^n
# Real-world: In P&C insurance, exponents model compound interest or exponential growth in claims costs.

# Example: Compute 2^3, 2^(-2), and product rule
print("\n--- Exponents: Basic Operations ---")
base = 2
exp1 = 3
exp2 = -2
product_exp = exp1 + exp2  # Product rule: 2^3 * 2^(-2) = 2^(3 + (-2)) = 2^1

print(f"2^{exp1} = {base ** exp1}")  # 2^3 = 8
print(f"2^{exp2} = {base ** exp2}")  # 2^(-2) = 1/4
print(f"Product Rule: 2^{exp1} * 2^{exp2} = 2^{product_exp} = {base ** product_exp}")

# Step 4: Logarithms
# Logarithms are the inverse of exponents: if a^b = c, then log_a(c) = b.
# Key types:
# - Natural Log: ln(x) = log_e(x), base e ≈ 2.718
# - Common Log: log(x) = log_10(x)
# - Properties:
#   - Product: log(a * b) = log(a) + log(b)
#   - Quotient: log(a / b) = log(a) - log(b)
#   - Power: log(a^b) = b * log(a)
# Real-world: In insurance, logarithms model decay (e.g., depreciation) or transform data for risk models.

# Example: Compute ln(10), log_10(100), and apply product rule
print("\n--- Logarithms: Basic Operations ---")
x = 10
y = 100
print(f"Natural log ln({x}) = {np.log(x):.4f}")  # ln(10) ≈ 2.3026
print(f"Common log log_10({y}) = {np.log10(y):.4f}")  # log_10(100) = 2
print(f"Product Rule: log({x} * {y}) = log({x}) + log({y}) = {np.log10(x * y):.4f}")

# Step 5: Polynomials
# Polynomials are expressions with terms of the form ax^n, where a is a coefficient and n is a non-negative integer.
# - Degree: Highest exponent (e.g., 3x^2 + 2x + 1 has degree 2).
# - Operations: Addition, subtraction, multiplication, division.
# Real-world: In P&C insurance, polynomials model cost functions or risk curves (e.g., claim severity over time).

# Example: Evaluate and manipulate polynomial 2x^2 + 3x + 1
print("\n--- Polynomials: Evaluation and Operations ---")
# Define polynomial: 2x^2 + 3x + 1
coeffs = [2, 3, 1]  # Coefficients for x^2, x, constant
x_val = 2
poly_value = np.polyval(coeffs, x_val)  # Evaluate at x = 2
print(f"Polynomial 2x^2 + 3x + 1 at x = {x_val} = {poly_value}")

# Add two polynomials: (2x^2 + 3x + 1) + (x^2 + 2x + 4)
coeffs2 = [1, 2, 4]
sum_coeffs = np.polyadd(coeffs, coeffs2)
print(f"Sum of 2x^2 + 3x + 1 and x^2 + 2x + 4 = {sum_coeffs.tolist()} (3x^2 + 5x + 5)")

# Step 6: Factoring
# Factoring: Expressing a polynomial as a product of simpler polynomials or factors.
# - Common methods: Factor out GCF, factor quadratics (ax^2 + bx + c), or use roots.
# - Real-world: In insurance, factoring can simplify models for premium calculations or solve for break-even points.

# Example: Factor x^2 - 5x + 6 using sympy
print("\n--- Factoring: Quadratic Example ---")
x = sp.Symbol('x')
poly = x**2 - 5*x + 6
factored = sp.factor(poly)
print(f"Polynomial x^2 - 5x + 6 factors as: {factored}")  # (x - 2)(x - 3)

# Verify by finding roots
roots = sp.solve(poly, x)
print(f"Roots of x^2 - 5x + 6 = 0: {roots}")

# Step 7: Quadratic Equations
# Quadratic Equation: ax^2 + bx + c = 0
# - Solutions via Quadratic Formula: x = [-b ± √(b^2 - 4ac)] / (2a)
# - Discriminant (Δ = b^2 - 4ac): Determines number of real roots (Δ > 0: two, Δ = 0: one, Δ < 0: none).
# Real-world: In P&C insurance, quadratics model cost curves or optimize claim reserve allocations.

# Example: Solve x^2 - 5x + 6 = 0
print("\n--- Quadratic Equations: Solving Example ---")
a, b, c = 1, -5, 6  # Coefficients
discriminant = b**2 - 4*a*c
root1 = (-b + np.sqrt(discriminant)) / (2*a)
root2 = (-b - np.sqrt(discriminant)) / (2*a)
print(f"Quadratic x^2 - 5x + 6 = 0")
print(f"Discriminant: {discriminant}")
print(f"Roots: x = {root1}, x = {root2}")

# Symbolic solution with sympy for verification
quad_eq = a*x**2 + b*x + c
solutions = sp.solve(quad_eq, x)
print(f"Symbolic solutions: {solutions}")

# Step 8: Real-World Application (P&C Insurance Context)
# Example: Model claim cost growth as a quadratic function in P&C insurance
# Suppose claim costs grow as C(t) = 100t^2 + 200t + 500, where t is time in years
print("\n--- P&C Insurance Application: Quadratic Cost Model ---")
t = np.array([0, 1, 2, 3])  # Time points
claim_costs = 100 * t**2 + 200 * t + 500
print(f"Claim costs over time (C(t) = 100t^2 + 200t + 500): {claim_costs.tolist()}")

# End of Script
print("\n--- End of Basic Algebra Concepts Explanation ---")