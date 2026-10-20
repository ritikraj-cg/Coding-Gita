# Question 46
# N = int(input())
# last_digit = N % 10
# first_digit = N % 10
# while N > 0:
#     first_digit = N % 10
#     N //= 10
# print("First digit:", first_digit)
# print("Last digit:", last_digit)


# Question 47
# N = int(input())
# count = 0
# if N == 0:
#     count = 1
# while N > 0:
#     if (N % 10) % 2 == 0:
#         count += 1
#     N //= 10
# print(count)


# Question 48
# N = int(input())
# count = 0
# while N > 0:
#     if (N % 10) % 2 == 1:
#         count += 1
#     N //= 10
# print(count)


# Question 49
# N = int(input())
# total = 0
# while N > 0:
#     if (N % 10) % 2 == 0:
#         total += N % 10
#     N //= 10
# print(total)


# Question 50
# N = int(input())
# largest_digit = N % 10
# while N > 0:
#     if (N % 10) > largest_digit:
#         largest_digit = N % 10
#     N //= 10
# print(largest_digit)


# Question 51
# N = int(input())
# smallest_digit = N % 10
# while N > 0:
#     if (N % 10) < smallest_digit:
#         smallest_digit = N % 10
#     N //= 10
# print(smallest_digit)
