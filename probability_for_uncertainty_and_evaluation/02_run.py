# Python Script: Annuity Terms Section for Annuity Insurance
# This is a focused version of the annuity terms section to fix the np.pv error.
# It calculates present values for ordinary annuity, annuity due, perpetuity, and monthly compounded annuity.
# Ensure numpy-financial is installed: pip install numpy-financial

# Step 1: Import Necessary Libraries
import numpy as np
import numpy_financial as npf  # Correct import for financial functions

# Step 2: Annuity Terms - Present Value Example
print("\n--- Annuity Terms: Present Value Example ---")
pmt = 1000  # Annual payment
r = 0.05   # Annual interest rate (5%)
n = 10     # Number of years

# Present Value (PV) of ordinary annuity: PV = PMT * [1 - (1 + r)^(-n)] / r
pv_ordinary = pmt * (1 - (1 + r)**(-n)) / r
print(f"Ordinary Annuity PV: ${pv_ordinary:.2f}")

# Annuity Due PV: Ordinary PV multiplied by (1 + r), since payments start earlier
pv_due = pv_ordinary * (1 + r)
print(f"Annuity Due PV: ${pv_due:.2f}")

# Perpetuity PV: PV = PMT / r (infinite periods)
pv_perpetuity = pmt / r
print(f"Perpetuity PV: ${pv_perpetuity:.2f}")

# Monthly Compounded Annuity: Adjust for monthly payments
monthly_r = r / 12
monthly_n = n * 12
monthly_pmt = pmt / 12

# Present value with monthly compounding using numpy-financial
pv_monthly = npf.pv(rate=monthly_r, nper=monthly_n, pmt=-monthly_pmt, fv=0)  # npf.pv returns negative, we use absolute
print(f"Monthly Compounded Ordinary Annuity PV: ${abs(pv_monthly):.2f}")

# End of Section
print("\n--- End of Annuity Terms Section ---")