N1= float(input("enter number 1--->  "))
N2= float(input("enter number 2 -->"))
choice = input("select opration : + , - , % , **, *:  --->")

if choice == '+':
    print(f" additon : {N1+N2}")

elif choice == '-':
    print(f" subration : {N1-N2}")
elif choice == '%':
    print(f"mode {N1%N2}")
elif choice=='* *':
    print(f"multiply is {N1*N2}")
elif choice=='**':
    print(f"suqare is {N1**N2}")