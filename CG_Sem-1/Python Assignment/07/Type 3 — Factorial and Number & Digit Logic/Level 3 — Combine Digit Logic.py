# Question 52
# N = int(input())
# N_copy = N
# N_reverse = 0
# while N_copy > 0:
#     N_reverse = (N_reverse * 10) + N_copy % 10
#     N_copy //= 10
# if N_reverse == N:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Question 53
# N = int(input())
# D = int(input())
# count = 0
# if N == 0 and D == 0:
#     count = 1
# while N > 0:
#     if (N % 10) == D:
#         count += 1
#     N //= 10
# print(count)


# Question 54
# N = int(input())
# are_digit_same = "Yes"
# prev_digit = N % 10
# N //= 10
# while N > 0:
#     curr_digit = N % 10
#     if curr_digit != prev_digit:
#         are_digit_same = "No"
#     prev_digit = curr_digit
#     N //= 10
# print(are_digit_same)


# Question 55
# import math
# N = int(input())
# last_digit = N % 10
# first_digit = N % 10
# N //= 10
# digits = int(math.log10(N)+1)
# middle_total = 0
# while N > 0:
#     first_digit = N % 10
#     if digits > 1:
#         middle_total += N % 10
#     N //= 10
#     digits -= 1
# print("First and last digits sum:", (first_digit + last_digit))
# print("Middle digits sum:", middle_total)
