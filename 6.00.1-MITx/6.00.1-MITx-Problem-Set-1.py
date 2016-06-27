# Problem 1:
# Count number of vowels within the string s
s = 'azcbobobegghakl'
count = 0
for char in s: 
    if char in 'aeoui':
        count +=1
    else: 
        count = count 
    
print('Number of vowels: ' + str(count))

# Problem 2: 
# Count the occurence of 'bob' within the string s - Method 1
s = 'azcbobobegghakl'
count = 0
i = 0
j = 3
while i < len(s):
    if s[i:j] == 'bob':
        count +=1
    else: 
        count = count 
    i = i + 1
    j = i + 3
    
print('Number of times bob occurs is: ' + str(count))

# Count the occurence of 'bob' within the string s - Method 2
s = 'azcboebakl'
count = 0
i = 0
j = 3
while i < len(s):    
    count += s.count('bob', i, j)
    i = i + 1
    j = i + 3

print('Number of times bob occurs is: ' + str(count))

# Problem 3: Counting & Grouping

def count_item(item, order):
    '''
    Function call returns number of a specific item in an order
    '''
    count = 0
    i = 0
    j = len(item)

    while i < len(order): 
        count += order.count(item, i, j)
        i = i +1 
        j = i + len(item)
        
    return count

def item_order(order):
    
    '''
    Write a function called item_order that takes as input a string named order. 
    The string contains only words for the items the customer can order separated by one space. 
    Returns a string that counts the number of each item and consolidates them
    '''

    numberSalad = count_item('salad', order)
    numberHamburger = count_item('hamburger', order)
    numberWater = count_item('water', order)
    return 'salad:'+ str(numberSalad) + ' hamburger:'+ str(numberHamburger) + ' water:' + str(numberWater)

