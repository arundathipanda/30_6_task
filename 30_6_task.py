#From the list nums = [10, 25, 30, 45, 50, 60], create a set of numbers where the number is divisible by 5 but not divisible by 10 using set comprehension.
nums={10,25,30,45,50,60}
result={ x for x in nums if x%5==0 and x%10!=0 }
print(result)
#Write a program to sum the digits of all numbers in a list.
#    Example: [12, 34, 5] ➞ 1+2 + 3+4 + 5 = 15
a={12,34,5}
s=0
for num in a:
    for i in str(num):
        s+=int(i) 
print(s)
#Create a new list by repeating elements of a list n times.
#             Example: [1, 2, 3], n = 2 ➞ [1, 2, 3, 1, 2, 3]
b=[1,2,3]
n=int(input("Enter how many times you wanna print: "))
final_b= []
for _ in range(n):
    final_b.extend(b)
print(final_b)
#Write a function to count frequency of each element in a list (return as dictionary).
c= [1,2,3,4,54,4,3,3,3,32,1,1,1,1,1,1,1]
dic={}
for item in c:
    if item in dic:
        dic[item]+=1
    else:
        dic[item]=1
print(dic)
#Write a function to count how many prime numbers exist in a given range.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def count_primes(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

print(count_primes(10, 30))  
#Sum digits until single-digit
def sum_to_single_digit(num):
    while num >= 10:
        num = sum(int(d) for d in str(num))
    return num
print(sum_to_single_digit(9875))