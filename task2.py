print('This Software calculates your BMI (Body mass index) based on your height and weight. \n Please enter with the following informations.')

# Verify if the user input is a float number
def isFloat(case):
    try:
        float(case)
        return True
    except:
        return False

userData=[]
# Name varification
while True:
    case=input('First Name: ')
    if case.isnumeric():
        print('\nPlease enter with a string!')
    else:
        userData.append(case)
        break
while True:
    case=input('Last Name: ')
    if case.isnumeric():
        print('\nPlease enter with a string!')
    else:
        userData.append(case)
        break

# Age verification
while True:
    case=input('Age: ')
    if case.isnumeric():
        userData.append(int(case))
        break
    else:
        print('\nPlease enter with a valible age!')
# Weight verification
while True:
    case=input('Weight (kg): ')
    if isFloat(case):
        userData.append(float(case))
        break
    else:
        print('\nPlease enter with a valible weight!')
# Height verification
while True:
    case=input('Height (m): ')
    if isFloat(case):
        userData.append(float(case))
        break
    else:
        print('\nPlease enter with a valible height!')

# calculate de BMI
bmi=(userData[3])/(userData[4]**2)

# categorzie the user BMI 
if bmi<18.5:
    categorie='Underweight'
elif bmi>=18.5 and bmi<=24.9:
    categorie='Normal weight'
elif bmi>=25 and bmi<=29.9:
    categorie='Overweight'
elif bmi>=30:
    categorie='Obesity'

print('Mr(s) {fName} {lName} born in {age}, your BMI is {bmi:.2f}, you are categorized as {cate}!'.format(fName=userData[0].capitalize(), lName=userData[1].capitalize(), age=2022-userData[2], bmi=bmi, cate=categorie))