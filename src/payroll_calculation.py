# Calculate gross pay based on hourly rate and hours worked
def calculate_gross_pay(hourly_rate, hours_worked):
    return hourly_rate * hours_worked

# Calculate tax deduction (simplified for illustration)
def calculate_tax_deduction(gross_pay, tax_rate):
    return gross_pay * tax_rate

# Calculate insurance deduction (simplified for illustration)
def calculate_insurance_deduction(gross_pay, insurance_rate):
    return gross_pay * insurance_rate

# Calculate net pay
def calculate_net_pay(gross_pay, tax_deduction, insurance_deduction):
    return gross_pay - tax_deduction - insurance_deduction

# Main payroll calculation function
def calculate_payroll():
    # Load employee data from a CSV file or database
    # (You would need to implement this part)

    # Loop through employee data and calculate payroll for each employee
    for employee in employee_data:
        gross_pay = calculate_gross_pay(employee["hourly_rate"], employee["hours_worked"])
        tax_deduction = calculate_tax_deduction(gross_pay, tax_rate)
        insurance_deduction = calculate_insurance_deduction(gross_pay, insurance_rate)
        net_pay = calculate_net_pay(gross_pay, tax_deduction, insurance_deduction)

        # Print or store payroll information (you can extend this)
        print(f"Employee: {employee['name']}")
        print(f"Gross Pay: ${gross_pay:.2f}")
        print(f"Tax Deduction: ${tax_deduction:.2f}")
        print(f"Insurance Deduction: ${insurance_deduction:.2f}")
        print(f"Net Pay: ${net_pay:.2f}")
        print("------------------------")
