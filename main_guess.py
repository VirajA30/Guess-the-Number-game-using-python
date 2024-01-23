import guess_number as ng

comp_num = ng.guess_number(0,1000)


score= 0

dt =ng.range_of_number(20)
ng.show_on_screen(comp_num,dt)

user_number = ng.take_user_input()

ng.check_user_input(comp_num,user_number)
