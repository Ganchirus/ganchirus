main_string = input("Enter your main string: ")
sub_string = input("Enter your sub string: ")

if main_string=="" and sub_string=="":
    print("Please enter non-empty strings. ")
elif main_string=="" or sub_string=="":
    print("One of the strings is empty. ")
else:
    command = input("Enter you command:")
    if command !="cat" and command !="find" and command !="beatbox":
        print("usage: command find | cat | beatbox")
    elif command=="cat":
        print("You string is:",main_string,sub_string)
    elif command=="find":
        print(bool(main_string==sub_string))
    else:
        command=="beatbox"
        a = int(input("Enter your first beatbox number: "))
        b = int(input("Enter your second beatbox number: "))
        if 0>=int(a) or 0<=int(a) or 0>=int(b) or 0<=int(b):
            print("usage: number must be > 0 and <= 10")
        elif a==b:
            print("usage: numbers must be not equal")
        else:
            print(main_string*a+sub_string*b)


