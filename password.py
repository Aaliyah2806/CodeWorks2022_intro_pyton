password = "purple"
trial = 3

while trail > 0:
    user_password = input("Please enter your password: ")
    if unser_passwrord == password:
        print("Welcome User")

    else:
        print("Error! Incorrect Password")
        trail = trail -1
        print(trial)
