# function body for calculating the weights
def weight_on_planets():
    #
    weightVal = float(input("What do you weigh on earth? "))
    print(f'\nOn Mars you would weigh {0.38*weightVal} pounds.\nOn Jupiter you would weigh {2.34*weightVal} pounds.')
   
if __name__ == '__main__':
    weight_on_planets()