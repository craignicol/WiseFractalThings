import subprocess

# Advent of Code 2019

def run_day(n):
  print("day {}".format(n))
  subprocess.call(["python", "./day.{}.py".format(n)])

# Yes, we could loop, but lets avoid re-running slow scripts by default

# run_day('n')
# run_day(1)
# run_day(2)
# run_day(3)
# run_day(4)
# run_day(5)
# run_day(6)
# run_day(7)
# run_day(8)
### skip a few
run_day(14)