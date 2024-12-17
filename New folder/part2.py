# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1959433
# Date:14.12.2022


progress_count = 0
Exclude_count = 0
module_trailer_count = 0
module_retriever_count = 0


progress_list = []
module_retriever_list = []
module_trailer_list = []
Exclude_list = []


def Histograme():
    print("-"*100)
    print("Histogram")
    print("progress", progress_count, ":", progress_count * "*")
    print("Trailer", module_trailer_count, ":", module_trailer_count * "*")
    print("Retriever", module_retriever_count, ":", module_retriever_count * "*")
    print("Excluded", Exclude_count, ":", Exclude_count * "*")

    total_counts = progress_count + module_trailer_count + module_retriever_count + Exclude_count
    print(total_counts, "Outcomes in total.")
    print("-"*100)



def list_print():
    for value1 in progress_list:
        print(f"Progress - {str(value1[0:])[1:-1]}")

    for value2 in module_trailer_list:
        print(f"Progress(module trailer) - {str(value2[0:])[1:-1]}")

    for value3 in Exclude_list:
        print(f"Exclude - {str(value3[0:])[1:-1]}")

    for value3 in module_retriever_list:
        print(f"Module retriever - {str(value3[0:])[1:-1]}")



def progression_outcome():
    global progress_count,module_retriever_count,module_trailer_count,Exclude_count
    if pass_credit == 120:
        print("Progress")
        progress_count = progress_count + 1
        progress_list.append([pass_credit, defer_credit, fail_credit])

    elif pass_credit == 100:
        print("Prgress(module trailer)")
        module_trailer_count = module_trailer_count + 1
        module_trailer_list.append([pass_credit, defer_credit, fail_credit])

    elif fail_credit >= 80 and defer_credit <= 40 and pass_credit <= 40:
        print("Exclude")
        Exclude_count = Exclude_count + 1
        Exclude_list.append([pass_credit, defer_credit, fail_credit])

    elif pass_credit <= 80 and fail_credit <= 60:
        print("Do not progress- module retriever")
        module_retriever_count = module_retriever_count + 1
        module_retriever_list.append([pass_credit, defer_credit, fail_credit])


Quit_continue = 'y'

while Quit_continue !="q":
    while True:
        while Quit_continue =='y':
            while True:
                try:
                    pass_credit = int(input("Enter your pass credits"))
                    if pass_credit in range(0,121,20):
                        break
                    else:
                        print("Out of range")
                        continue
                except:
                    print("Integer Required")
                    continue




            while True:
                try:
                    defer_credit = int(input("Enter your defer credits"))
                    if defer_credit in range(0, 121, 20):
                        break
                    else:
                        print("Out of range")
                        continue
                except:
                    print("Integer required")
                    continue




            while True:
                try:
                    fail_credit = int(input("Enter your fail credits"))
                    if fail_credit in range(0,121,20):

                        break
                    else:
                        print("Out of range")
                        continue
                except:
                    print("Integer required")
                    continue

            if pass_credit + fail_credit + defer_credit != 120:
                print("Total incorrect")
            else:
                progression_outcome()
            break
        break
    Quit_continue = input( "would you like to enter another set of data?,\n Enter 'y' for yes and 'q' for quit and view results")
    continue

Histograme()
list_print()





















