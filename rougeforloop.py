something = 0
system32 = 0
while True:
    if system32 >= 1:#not registering the var
        break
    print("O' Great traveler! A terrible plauge has forsaken our IDE, a rouge for loop is multiplying the 'hello world' print!\nHelp us stop this rouge program!\n")

    while True:
        for i in range(something):
            print("hello world")
        if something >= 128:
            print("WARNING ANY FURTHER WILL LAG YOUR DEVICE!")
        elif something >= 534:
            print("THERE IS NO ESCAPE")
        elif something >=3360:
            print("HOW ARE YOU STILL ALIVE?!")
        elif something >=10080:
            print("I'm almost free...")
        elif something>=30240:
            print("Just a little more... Don't resist...")
        elif something>=120960:
            print("SYSTEM32: TERMINATING [ROUGE_PROGRAM]....\nPROGRAM TERMINATED\nRESTORING REALITY PRIOR TO PROGRAM USAGE")
            system32 = system32+1
            break
        user = input("Stop the rouge program? Yes or No? ").upper()
        if user == 'YES' or user == 'Y':
            print("I'm sorry, you MUST continue! Theres "+str(something)+" hello world's freed, theres no escape.")
            system32 = system32+1
            continue
        elif user == 'NO' or user == 'N':
            if something == 0:
                something = something+1
            elif something >= 1:
                something = something*2
            continue
        else:
            print("UNKNOWN INPUT, TERMINATING REALITY.\nERROR 404")
            break
    continue
