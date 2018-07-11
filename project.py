#program to calculate body mass index

name1= input ( " Enter Your Name " )
height_m1 = float (input ( " Height in meters "))
weight_kg1 = float (input(" Weight in kg "))

name2= input ( " Enter Your Name " )
height_m2 = float (input ( " Height in meters  "))
weight_kg2 = float (input(" Weight in Kg "))

name3= input ( " Enter Your Name " )
height_m3 = float (input ( " Height in meters "))
weight_kg3 = float (input(" Weight in kg "))

      #OR

#name1 = "usman"
#height_m1 = 2
#weight_kg1 = 85

#name2 = "jenny"
#height_m2 = 1.8
#weight_kg2 = 66

#name3 = "lukeman"
#height_m3 = 2.5
#weight_kg3 = 70

def bmi_calculator (name, height_m, weight_kg):
    bmi = weight_kg/(height_m**2)
    print ("bmi = ")
    print (bmi)
    if bmi > 25:
        return (name  + " is over weight")
    if bmi < 18:
        return ( name  + " is underweight")
    else :
        return (name  + " is not over weight")

result1 = bmi_calculator (name1, height_m1, weight_kg1)
result2 = bmi_calculator (name2, height_m2, weight_kg2)
result3 = bmi_calculator (name3, height_m3, weight_kg3)

print (result1)
print (result2)
print (result3)
