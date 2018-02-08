def computepay(ph,pr):
    otpay=((ph - 40) * 1.5 * pr)
    return otpay

hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)

if h > 40 :
    pay = (40 * r ) +  computepay(h,r)
else :
    pay = h * r

print (pay)
