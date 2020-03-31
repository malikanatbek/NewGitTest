# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
s1=input()
s2=input()

new_s1=s2[:2]+s1[2:]
new_s2=s1[:2]+s2[2:]

print(new_s1+' '+new_s2)

# Example

a='abc'
b='xyz'

print(a)
print(b)

new_a=b[:2]+a[2:]
new_b=a[:2]+b[2:]

print(new_a)
print(new_b)

d=new_a+' '+new_b
print(d)

# Write a Python program to remove nth index character from a Non-Empty string.

string=input("Enter string")
index=int(input("Enter index"))
first_part=string[:index]
last_part=string[index+1]
print(first_part+last_part)

# Example

str="Python"
n=3
print(str[3])

first_part=str[:n]
last_part=str[n+1:]

print(first_part)
print(last_part)

remove_h=first_part+last_part
print(remove_h)






