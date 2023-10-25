# Tian and Aaron
# Aaron's code
def encode(password):
    password = list(password)
    for i in range(0,len(password)):
        password[i] = (int(password[i]) + 3) % 10
    password = "".join(map(str, password))
    return password

if __name__ == "__main__":
    while True:
        password = ""
        encoded_password = ""
        print("\nMenu")
        print("-"*13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        user_choice = int(input("Please enter an option: "))

        if (user_choice == 1):
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoded_password = encode(password)
        elif (user_choice == 2):
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")
        elif (user_choice == 3):
            break
