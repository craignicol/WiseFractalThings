import subprocess

def run_day(n):
  print("day {}".format(n))
  subprocess.call(["python", "./day.{}.py".format(n)])

# Yes, we could loop, but lets avoid re-running slow scripts by default
run_day('n')
run_day(1)
