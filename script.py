# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# display the value of the insurance_cost using the above information in an informative way 
print("This person's insurance cost is " + str(insurance_cost) + " " + "dollars.")

# Age Factor

# increase age by 4
age += 4

# new insurance_cost when age is increased by 4
new_insurance_cost =  250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# find the difference between our new insurance cost and the old insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost

# display a new line
print("\n")

# display the value of change_in_insurance_cost in an informative way
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " " + "dollars.")


# BMI Factor

#set age to its initial value
age = 28

#increase bmi value by 3.1
bmi += 3.1

# calculate the new insurance cost when bmi is increased by 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# find the change in insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost

# display a new line
print("\n")

# display the change in estimated insurance cost after increasing bmi by 3.1
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " " + "dollars.")

# Male vs. Female Factor

# reassign bmi varible back its original value
bmi = 26.2

# for a male individual
sex = 1

# estimate a new insurance cost for a male individual
new_insurance_cost =  250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# find the change in insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost

# display a new line
print("\n")

# display the value of change in estimated cost for being a male
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " " + "dollars.")

# Extra Practice

# female smoker vs female non-smoker factor
sex = 0
smoker = 1

# estimate a new insurance cost for a female smoker
new_insurance_cost =  250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# find the change in insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost

# display a new line
print("\n")

# display the value of change in estimated cost for being a female smoker
print("The change in estimated cost for being a female smoker is " + str(change_in_insurance_cost) + " " + "dollars.")

# male smoker vs male non-smoker factor
sex = 1
smoker = 1

# estimate a new insurance cost for a male smoker
new_insurance_cost =  250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# find the change in insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost

# display a new line
print("\n")

# display the value of change in estimated cost for being a male smoker
print("The change in estimated cost for being a male smoker is " + str(change_in_insurance_cost) + " " + "dollars.")

# initializing the original data
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# a female with no children

# set num_of_children to 0
num_of_children = 0

# estimate a new insurance cost for a female with no children
new_insurance_cost =  250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# find the change in insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost

# display a new line
print("\n")

# display the value of change in estimated cost for being a female with no children
print("The change in estimated cost for being a female with no children is " + str(change_in_insurance_cost) + " " + "dollars.")

# a male with no children

# set sex to 1
sex = 1
# set num_of_children to 0
num_of_children = 0

# estimate a new insurance cost for a male with no children
new_insurance_cost =  250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# find the change in insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost

# display a new line
print("\n")

# display the value of change in estimated cost for being a male with no children
print("The change in estimated cost for being a male with no children is " + str(change_in_insurance_cost) + " " + "dollars.")