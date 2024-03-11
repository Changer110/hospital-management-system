# from django.test import TestCase
# Create your tests here.



# print('hello')

tomates = ['tom1', 'tom2', 'tom3']

tomates = {'tom1' : 10, 'tom2' : 20, 'tom3' : 15, 'tom4' : ['tom41', 'tom42']}
person = {
    'name':'bill',
    'age' : 20,
    'phone_number' : [122344545, 25152165]
}
#   == , > , < ,  <= ,>= 
list_person = [
    {'name':'bill','age' : 10,'phone_number' : [122344545, 25152165]},
    {'name':'kent','age' : 20,'phone_number' : [122344545, 25152165]},
    {'name':'brown','age' : 30,'phone_number' : [122344545, 25152165]},
    {'name':'kelly','age' : 20,'phone_number' : [122344545, 25152165]}
]
# print(person.get('phone_number'))
# for person in list_person:
#     if person['age'] < 20:
#         print(person)


def sum(number1, number2):
    res = number1 + number2
    return res

res1 = sum(10, 25)
print(res1)

def minus(a,b):
    res = a - b
    return res
res2 = minus(10,25)
print(res2)

res = sum(res1, res2)
print(res)





# def less(a,b):
#     res = 'All is equal'
#     if a < b:
#         res = a
#     elif b < a:
#         res = b
#     else:
#         res = res
#     return res
    
# res = less(23239,988988)
# print(res)
    
    