# Input function value will always be in string

# a = input("Please enter your name: \t")
# print(f'How are your Mr. {a}?')
# print(type(a))

# sys.argv
import sys

print('line1')
print('line2')

print(sys.argv) 

if sys.argv[1] == '-g':
    print(f"I will install {sys.argv[2]} package globally.")

# to execute sys.argv program type "& C:/Users/Danish/anaconda3/envs/python12/python.exe d:/coding/Github/Python/class9/class9.py '-g' 'pyth1'"

# resulte will be shown as:
# line1
# line2
# ['d:/coding/Github/Python/class9/class9.py', '-g', 'pyth1']"
# I will install pyth1 package globally.