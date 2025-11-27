import sys

if len(sys.argv) >= 3:
  script_name = sys.argv[0]
  intial = sys.argv[1]
  deposit = sys.argv[1]
else:
  script_name = sys.argv[0]
  initial  = 15000
  deposit = 2000

balance=intial+deposit
print("initial:",initial)
print("deposit:",deposit)
print(" balance amount:",balance)
