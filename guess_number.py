import random

def guess_number(num1,num2):
    return random.randint(num1,num2)

def range_of_number(range_var):
    df = {}
    df['min'] = random.randint(1,range_var)
    df['max'] = random.randint(1,range_var)

    return df

def show_on_screen(c_num,df):
    min_number = c_num - df.get('min')
    max_number = c_num + df.get('max')

    print('hey ur number should be between ',min_number,'to ',max_number)

def take_user_input():
    user_input = int(input('enter a number '))
    return user_input


def check_user_input(c_num,u_num):
    if(c_num==u_num):
        print('yay u have got the right guess')
        return 10
    else:
        print('sorry u lost the number was ',c_num)
        return 0
    
  
