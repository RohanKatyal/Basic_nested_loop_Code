#--------^v^-------#

def main_code(n_i, n_j, n):
    for i in range(n,n_i):
        print(f">> for i = {i}\n")
        if i>= 0 :
            for j in range(n,n_j):
                print(f" -> 'j = {j}'")
            print("\n#--------^v^-------#\n")

        print(f"Loop stopped at {i}")
        print("#--------_^_-------#\n")
                
    print(">>End_of_Loop<<")    
    
#--------^v^-------#
        
def parent_code():

    n = int(input("Enter the value of i : "))
    n1 = int(input("Enter the value of j : "))
    print("To select start value")
    option = input("Press Y/y : ")
    a = "-> Loop ended with error <-"
    
    try :
        
        if option.lower() == "y":
            value = int(input("Enter the start value : "))
            if value < (n or n1):
                main_code(n, n1, value)
            else:
                print("Start value is greater than i or j")
        else:
            print("#>------Wrong_Input------<#\n>>Rerun_Code!!<<")

    except ValueError:
        print(f">>ValueError<<\n{a}")
    except TypeError:
        print(f">>TypeError<<\n{a}")
    except KeyboardInterrupt:
        print(f">>KeyboardInterrupt<<\n{a}")

#--------^v^-------#

parent_code()
