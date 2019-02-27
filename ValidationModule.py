#regex module
import re
#function to validate each password input 
def checkPass(str):
    if(len(str)<6 or len(str)>12):
        print(str + " Failure password must be 6-12 characters.\n")
        return
    if not re.search("[a-z]", str):
        print(str + " Failure password must contain at least one letter from a-z \n")
        return
    if not re.search("[A-Z]", str):
        print(str + " Failure password must contain at least one letter from A-Z \n")
        return
    if not re.search("[0-9]", str):
        print(str + " Failure password must contain at least one number 0-9 \n")
        return
    if not re.search("[*$_#=@]", str):
        print(str + " Failure password must contain at least one letter from *$_#=@! \n")
        return
    if re.search("[%!)(]", str):
        print(str + " Failure password cannot contain %!)( \n")
        return
    print(str+" Success\n")
    return
#main function
if __name__ == '__main__':
    password = input("Enter Password: ")
    arr = password.split(',')
    print("\n")
    for i in arr:
        checkPass(i)
