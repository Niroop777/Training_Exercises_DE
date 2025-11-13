#Ex 2

# Given a list of integers, write a function to identify even numbers

def evn_nums(num):

    evn=[]

    for n in num:
        if n%2==0:
            evn.append(n)

    evn.sort(reverse=True)

    return evn


n = [17,3,27,1,32,13,4,5,6,4,3,5,34,9,4,6,4,3,2,7,3,6]
print(evn_nums(n))


"""

This function takes a list of numbers and finds all the even ones.

It checks each number and adds it to a new list if it is even.

After collecting all even numbers, it sorts them in descending order.

Finally, it returns the sorted list of even numbers.

"""
