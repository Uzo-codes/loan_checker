# Mojojo Loan Checker 

Welcome to **Mojojo Loan Checker**, a simple CLI Python tool that helps users determine their eligibility for different loan products based on age, income, and loan preferences.

## Features

- Checks user eligibility based on age, income, and loan type
- Covers Business Loans, Salary Advance, and SME Loans
- Re-apply as many times as you like
- Built with clean Python logic and user-friendly prompts

## Eligibility Logic

- Minimum age: 21  
- Minimum income: ₦30,000  
- Maximum loan: 5x monthly income  
- Young applicants under 25 will need a guarantor  
- Only supported products: *Business Loan*, *Salary Advance*, *SME Loan*

## How to Use

```bash
python loan_checker.py
