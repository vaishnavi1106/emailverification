email = input("Enter your Email: ")
k = 0
j = 0
d = 0

if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if (email[-4] == "." or email[-3] == "."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Invalid Syntax")
                else:
                    print("The Email is Correct")
            else:
                print("Wrong Email")
        else:
            print("Invalid @")
    else:
        print("First Letter should be an Alphabet")
else:
    print("Must use @")
