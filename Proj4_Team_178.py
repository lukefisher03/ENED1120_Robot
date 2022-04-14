# This program is used to predict the deviation from the target point given a distance for the PMR to travel.
#

valid_input = False

while valid_input == False: 
    dist = float(input("What is the travel distance: "))
    if dist <= 0:
        print("Please input a postitive number")
    else:
        valid_input = True

#plug values into our polynomial models
x_dev = 0.0001*(pow(dist,2))+0.0046*dist+0.0483
y_dev = 3e-05*pow(dist,2)+ 0.0003*dist + 0.1346

print("The x-deviation will be: {} inches".format(x_dev))
print("The y-deviation will be: {} inches".format(y_dev))
print("Please note: This program is only suitable for predicting error for reasonable distances. \n Since the function modeling the error is a polynomial, at a certain point it will become \nunreasonably high. Aim for values under 2000 inches.")