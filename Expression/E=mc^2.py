"""Question : Write a program that continually reads in mass from the user and then outputs the equivalent energy 
              using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, 
              and C is the speed of light:
              E = m * c**2
"""

C = 299792458

def main():
    mass = float(input("Enter kilos of mass: "))

    energy = mass * ( C ** 2)

    print("e = m * C^2...")
    print("m = " + str(mass) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy) + "joules of energy!")
    

if __name__ == '__main__':
    main()