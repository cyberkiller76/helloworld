print("Welcome to E=mc2 calculator")
print()
while True:
    print(
        "Einstein\'s famous equation 'E=mc^2' shows that mass and energy are equivalent,and that the amount of energy contained within matter can be calculated using this equation...")
    print(
        "[Input a number to represent kilograms of mass, and this program will calculate the amount of energy contained in that amount of matter.]")

    m = int(input())
    # input mass (repersented by 'kg' or kilograms)

    c = int(299792458)
    # estimate equation for the speed of light by 'm/s' or meters per second

    e = (m * c ** 2)  # 'e' = energy ('j' or joules)
    # equation solves for the amount of energy required to create mass(or matter)/exists in an object with mass(or matter)

    print('\nUser Input = ' + str(m))
    print("The amount of energy required to form/sustain " + str(m) + "kg of mass/matter is equal to " + str(e) + "j.")

    break


input()