#Write a program that asks the user to enter a number. Keep asking (using a loop) until they enter a valid positive 
# integer. Handle non-numeric input gracefully using try/except.


# while True:
#     try:
#         raw_num = input("enter a number: ")
#         num = int(raw_num)
#         if num > 0:
#             print(f"you Entered: {num}")
#             break
#         else:
#             print("please enter a positive nunber")
    
#     except ValueError:
#         print("please Enter a valid number: try again.")
    
    
#Q21. Write a for loop that prints all numbers from 1 to 50 that are divisible by 7, 
# using continue to skip non-divisible numbers.

for num in range(1, 51):
    if num % 7 != 0:
        continue
    print(num)

        