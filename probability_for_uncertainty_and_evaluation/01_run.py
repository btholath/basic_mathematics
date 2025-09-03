# Python Script: Step-by-Step Explanation of Probability Concepts
# This script provides a detailed, educational walkthrough of key probability concepts using comments and code examples.
# It covers basic probability, key terms, conditional probability, random variables, and random processes.
# We use Python's built-in libraries and numpy for simulations to illustrate concepts.
# Run this script to see outputs and explanations in the console.

# Step 1: Import Necessary Libraries
# We import random for basic randomness, numpy for numerical simulations, and scipy.stats for statistical functions.
import random
import numpy as np
from scipy import stats

# Step 2: Basic Probability Concepts
# Probability is the measure of the likelihood that an event will occur, quantified between 0 (impossible) and 1 (certain).
# Key components:
# - Sample Space (Ω): The set of all possible outcomes. E.g., for a coin flip: {'Heads', 'Tails'}.
# - Event (E): A subset of the sample space. E.g., 'Heads'.
# - Probability Measure (P): A function assigning probabilities to events, where P(Ω) = 1, and probabilities sum appropriately.

# Example: Simulating a fair coin flip
print("\n--- Basic Probability: Coin Flip Example ---")
sample_space = ['Heads', 'Tails']  # Sample space
event_heads = 'Heads'  # An event

# Probability of heads in a fair coin: 0.5 (classical probability, assuming equally likely outcomes)
p_heads = 1 / len(sample_space)
print(f"Sample Space: {sample_space}")
print(f"Event: Getting {event_heads}")
print(f"Probability of {event_heads}: {p_heads}")

# Simulation: Flip coin 1000 times to estimate empirical probability
flips = [random.choice(sample_space) for _ in range(1000)]
heads_count = flips.count('Heads')
empirical_p_heads = heads_count / 1000
print(f"Empirical Probability from 1000 flips: {empirical_p_heads}")

# Step 3: Usage of All Probability Terms
# Here we define and illustrate common probability terms:
# - Outcome: A single result from the sample space (e.g., 'Heads').
# - Experiment/Trial: The process generating an outcome (e.g., flipping a coin).
# - Complementary Event: The event not occurring (e.g., not Heads = Tails), P(complement) = 1 - P(E).
# - Union of Events (A ∪ B): Either A or B or both occurs. P(A ∪ B) = P(A) + P(B) - P(A ∩ B).
# - Intersection of Events (A ∩ B): Both A and B occur.
# - Mutually Exclusive Events: Cannot occur together, P(A ∩ B) = 0, so P(A ∪ B) = P(A) + P(B).
# - Independent Events: Occurrence of one doesn't affect the other, P(A ∩ B) = P(A) * P(B).
# - Exhaustive Events: Cover the entire sample space.
# - A Priori Probability: Theoretical, before experiment.
# - A Posteriori/Empirical: Based on observed data.
# - Relative Frequency: Approximation of probability from trials.

# Example: Dice Roll for Terms
print("\n--- Probability Terms: Dice Roll Example ---")
dice_space = [1, 2, 3, 4, 5, 6]  # Sample space for a fair die
event_even = [2, 4, 6]  # Event: Even number
event_odd = [1, 3, 5]   # Complementary event to even

p_even = len(event_even) / len(dice_space)  # 0.5
p_odd = 1 - p_even  # Complementary probability

print(f"Sample Space (Die): {dice_space}")
print(f"Event Even: {event_even}, Probability: {p_even}")
print(f"Complementary Event (Odd): {event_odd}, Probability: {p_odd}")

# Union and Intersection Example
event_less_than_4 = [1, 2, 3]  # Another event
intersection = set(event_even) & set(event_less_than_4)  # {2}
union = set(event_even) | set(event_less_than_4)  # {1,2,3,4,6}

p_intersection = len(intersection) / len(dice_space)
p_union = p_even + (len(event_less_than_4)/len(dice_space)) - p_intersection

print(f"Intersection (Even and <4): {intersection}, P: {p_intersection}")
print(f"Union (Even or <4): {union}, P: {p_union}")

# Mutually Exclusive: Even and Odd are mutually exclusive and exhaustive
print("Even and Odd are mutually exclusive (intersection empty) and exhaustive (union = sample space).")

# Independent Events: Example with two dice (independent trials)
# P(first even and second odd) = P(even) * P(odd)
p_independent = p_even * p_odd
print(f"Independent Events (Two Dice: First Even, Second Odd): P = {p_even} * {p_odd} = {p_independent}")

# Step 4: Conditional Probability
# Conditional Probability: P(A|B) = P(A ∩ B) / P(B), the probability of A given B has occurred.
# It measures dependency between events.
# Bayes' Theorem: P(A|B) = [P(B|A) * P(A)] / P(B), used for updating probabilities with new evidence.

# Example: Card Draw (Without Replacement, so dependent)
print("\n--- Conditional Probability: Card Draw Example ---")
deck = ['Red'] * 26 + ['Black'] * 26  # Standard deck: 26 red, 26 black

# P(Red on second draw | Black on first) = P(second Red | first Black)
# Simulate: Draw first card (assume Black), then probability second is Red.

# Theoretical Calculation
p_first_black = 26 / 52
p_second_red_given_first_black = 26 / 51  # 26 red left, 51 cards total

print(f"P(First Black): {p_first_black}")
print(f"Conditional P(Second Red | First Black): {p_second_red_given_first_black}")

# Bayes' Example: Disease Test (Hypothetical)
# P(Disease) = 0.01, P(Positive|Disease) = 0.99, P(Positive|No Disease) = 0.05
# Find P(Disease|Positive)
p_d = 0.01
p_pos_given_d = 0.99
p_pos_given_no_d = 0.05
p_no_d = 1 - p_d
p_pos = (p_pos_given_d * p_d) + (p_pos_given_no_d * p_no_d)  # Total P(Positive)
p_d_given_pos = (p_pos_given_d * p_d) / p_pos  # Bayes' Theorem

print(f"Bayes' Theorem Example: P(Disease|Positive Test) = {p_d_given_pos:.4f}")

# Step 5: Random Variables
# Random Variable (RV): A function mapping sample space to real numbers. Can be:
# - Discrete: Finite/countable values (e.g., dice roll).
# - Continuous: Infinite values in interval (e.g., height).
# Key Measures:
# - Expectation (Mean): E[X] = sum(x * P(x)) for discrete; integral for continuous.
# - Variance: Var(X) = E[(X - E[X])^2], measures spread.
# - Probability Mass Function (PMF) for discrete, Probability Density Function (PDF) for continuous.

# Example: Discrete RV - Dice Roll
print("\n--- Random Variables: Discrete Example (Dice) ---")
x_values = np.array(dice_space)
pmf = np.array([1/6] * 6)  # Uniform PMF

expectation = np.sum(x_values * pmf)
variance = np.sum((x_values - expectation)**2 * pmf)

print(f"Discrete RV (Die): Values {x_values}, PMF {pmf}")
print(f"Expectation E[X]: {expectation}")
print(f"Variance Var[X]: {variance}")

# Continuous RV - Normal Distribution
# Example: Heights ~ Normal(mu=170, sigma=10)
print("\n--- Random Variables: Continuous Example (Normal Distribution) ---")
mu, sigma = 170, 10
normal_rv = stats.norm(mu, sigma)

print(f"Continuous RV: Normal(mu={mu}, sigma={sigma})")
print(f"Expectation (Mean): {normal_rv.mean()}")
print(f"Variance: {normal_rv.var()}")
print(f"PDF at x=170: {normal_rv.pdf(170)}")  # Density at mean
print(f"CDF at x=180: {normal_rv.cdf(180)}")  # P(X <= 180)

# Step 6: Random Processes
# Random Process (Stochastic Process): A collection of random variables indexed by time or space.
# - Discrete Time: e.g., Sequence of coin flips.
# - Continuous Time: e.g., Stock prices.
# Examples:
# - Bernoulli Process: Sequence of independent binary trials (e.g., coin flips).
# - Poisson Process: Models rare events over time, with rate lambda.
# Properties: Stationary (distributions don't change over time), Markov (future depends only on present).

# Example: Bernoulli Process Simulation
print("\n--- Random Processes: Bernoulli Process Example ---")
p_success = 0.5  # Probability of success (e.g., Heads)
n_trials = 10
bernoulli_sequence = np.random.binomial(1, p_success, n_trials)  # 1=success, 0=failure

print(f"Bernoulli Process (10 Trials, p={p_success}): {bernoulli_sequence}")
print(f"Number of Successes: {np.sum(bernoulli_sequence)}")

# Poisson Process: Simulate events in time interval
# Poisson RV for count in fixed interval
lambda_rate = 3  # Average 3 events per interval
poisson_rv = stats.poisson(lambda_rate)
poisson_sample = poisson_rv.rvs(5)  # 5 simulations

print(f"Poisson Process (lambda={lambda_rate}): Samples {poisson_sample}")
print(f"Expectation: {poisson_rv.mean()}")
print(f"P(Exactly 2 events): {poisson_rv.pmf(2)}")

# End of Script
print("\n--- End of Probability Concepts Explanation ---")