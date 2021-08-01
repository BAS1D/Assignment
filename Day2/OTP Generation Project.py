#OTP Generation Project
import random as r
import string
length = 6
otp = ''
characters = string.ascii_letters + string.digits
for i in range(length):
    otp = otp + r.choice(characters)
print("OTP:", otp)
