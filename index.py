try:
    age = int(input("Enter the age:"))
    if(age < 18):
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("The age is not valid")

if age % 2 == 0:
    print("The age is even.")
else:
    print("The age is odd.")
    

#------------------------------------------------------------------
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

for month in months:
    print(month)