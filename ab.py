#这是一个梦想之家的储蓄基金项目，根据用户输入的年收入、年化利率、预期的房价，计算出最佳的年度储蓄计划。
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, use percentage sign: "))
cost_of_dream_home = float(input("enter your dream price about home:"))
semi_annual_raise =float(input("Enter the semi-annual raise, use percentage sign:"))
portion_down_payment = 0.25*cost_of_dream_home
amount_saved = 0
#r为年利率
r = 0.05
#年薪
every_month_salary = yearly_salary/12
x = portion_saved*every_month_salary
n = 1
while True:
    x = x*(1+r/12)+every_month_salary*portion_saved
    n += 1
    if n%6 == 0:
        #代表半年加一次薪水
        every_month_salary += every_month_salary*semi_annual_raise
    if x >= portion_down_payment:
        break
print("Number of months:",n)
print("Amount saved:",x-portion_down_payment)
