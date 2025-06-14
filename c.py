#这是一个二分查找买房题目
#此为首付款
target_down_payment = 200000
#此为首付款
initial_deposit = float( input("Enter the initial deposit: "))
step = 1
high_r = 1
low_r = 0
#二分查找
guess_r = (high_r+low_r)/2
amount_saved = initial_deposit*(1 + guess_r/12)**36
while abs(amount_saved - target_down_payment) > 100:
    if amount_saved < target_down_payment:
        low_r = guess_r
    else:
        high_r = guess_r
    guess_r = (high_r+low_r)/2
    amount_saved = initial_deposit*(1 + guess_r/12)**36
    #进行一次步数加一
    step += 1
#最后的出需要的步数，以及适合的利率    
print("the step binary search takes", step, "steps to save", target_down_payment, "down payment.")
print("The interest rate is", guess_r)
 
