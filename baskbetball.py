apple_three= int(input())
apple_two= int(input())
apple_one= int(input())
banana_three= int(input())
banana_two= int(input())
banana_one= int(input())

apples_ttl = (apple_three * 3) + (apple_two * 2) + apple_one

bananas_ttl = (banana_three * 3) + (banana_two * 2) + banana_one

if apples_ttl > bananas_ttl: 
	print('A')
elif apples_ttl < bananas_ttl: 
	print('B')
elif apples_ttl == bananas_ttl:
	print('T')
