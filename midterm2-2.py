# Author: CMOB 12/14/2021

initial_velocity =input("What is the initial velocity? ")
final_velocity = input("what is the final velocity? ")
time = input("What is the total time it takes? ")

change_velocity = int(final_velocity) - int(initial_velocity)

average_acceleration = change_velocity / int(time)

print("The average acceleration is {0} mps".format(average_acceleration))