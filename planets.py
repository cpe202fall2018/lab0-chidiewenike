# function body for calculating the weights
def weight_on_planets():

    # assign float-casted input value to weigh_val
    weight_val = float(input("What do you weigh on earth? "))

    # print the contents to the screen which as string concatenated with two expressions for calculating weight 
    print(f'\nOn Mars you would weigh {0.38*weight_val} pounds.\nOn Jupiter you would weigh {2.34*weight_val} pounds.')
   
# the main function
if __name__ == '__main__':

    # the function call for the weight_on_planets function
    weight_on_planets()