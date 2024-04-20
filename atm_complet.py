def deposit(n,name):
    a=int(input('enter your amount to deposit'))
    print('ammount deposited sucessfully')
    print('the current balance is',n+a)
    update(n+a,name)
    # det[i][2]=n+a
    #  # print(det)
def withdraw(n,name):
    a=int(input('enter your amount to withdraw:'))
    if n<a:
        print('insufficient funds')
        return
    else:
        print('ammount withdrawn sucessfully')
        print('the current balance is',(n-a))
        update(n-a,name)
        # det[i][2] = n - a
def balance(n,name):
    print('your current balance is',n)
    return
def default():
    print('invalid input for default')


def option(fun,name):
    for i in enumerate(fun.values()):
        print(i)
    n = int(input('enter your choice and 0 to exit:'))
    if n == 0:
        return
    else:
        result = fun.get(n, default)
        result(user_data[name],name)
        option(fun,name)
def update(s,name):
    user_data[name] = s
    print(user_data)
    update_user_data(user_data)


def update_user_data(s):
    with open('test.txt', 'w') as f:
        for i, a in list(s.items()):
            s = str(i) + "," + str(a) + "\n"
            f.write(s)

def switch_case(det):
    fun = {1: withdraw, 2: deposit, 3: balance,0:0}
    name = input('enter your name:')
    # for i in range(len(det)):
    if name in det:
        # print(fun)
        # f = int(input('enter your input accordingly:'))
        # while True:
        #     if fun[f] == 0:
        #         break
        #     else:
        #
        #         result = fun[f]
        #         blc = float(bl)
        #         result(blc)
        option(fun,name)



user_data = {}
with open("test.txt", "r") as file:
    for line in file:
        username, bl = line.strip().split(',')
        user_data[username] = float(bl)
    # print(user_data)

switch_case(user_data)

















