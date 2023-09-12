import random
from time import sleep

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numb = "1234567890"
simb = "!/@:;#$%&"

char = lower + upper + numb + simb

print("=-"*22)
print("Welcome to Password Generator - brunols7")
print("=-"*22)

sleep(1)

pas_length = int(input("Enter the length of the password: "))
print("=-"*20)

sleep(1)

print("Generating password...")
print("=-"*20)

sleep(1)

password = "".join(random.sample(char, pas_length))
print("Your password: ", password)
print("=-"*20)
