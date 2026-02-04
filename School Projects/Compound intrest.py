def cic(cash,rates,time_compounded,years):
#This calculates the compound intrest by using this formula Great! Compound interest is the interest on a deposit or loan that is calculated based on both the initial principal and the accumulated interest from previous periodsamount= cash*(1+rates/time_compounded)**(time_compounded*years)
##
##where:
##  A  is the amount of money accumulated after \( n \) years, including interest.
##  P  is the principal amount (the initial amount of money).
##  r  is the annual interest rate (decimal).
##  n  is the number of times that interest is compounded per year.
##  t  is the time the money is invested or borrowed for, in     amount= cash*(1+rates/time_compounded)**(time_compounded*years)
#This is where the intrest is calculated
    interest_earned = amount - cash
    return amount, intrest_earned
    
