# name="yashpatil" #strings are immutable

# # #you cannot do this.

# a=len(name)  
# print(a)

# s="hello world"

# a=len(s)
# print(a)
# # print(s.upper())
# # print(s.lowercase())
# print(s.capitalize())
# print(s.title())

#strips in string

# text=" hello world "
# print(text.strip()) #output:"hello world"
# print(text.lstrip()) #output: "hello world "
# print(text.rstrip())#output:" hello world"


# finding and replacing

# text="python is fun is fun is fun is fun"
# print(text.find("is")) #output will be 7
# print(text.replace("fun","awesome"))



# text="Apples,Bananas,Pineapple"
# print(text.split(",")) #convert is a string to list
# print(",".join(['Apples', 'Bananas', 'Pineapple']))

text="python123"
print(text.isalpha()) #output:false
print(text.isdigit()) #output:false
print(text.isalnum()) #output:true
print(text.isspace()) #output:false