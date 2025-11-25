#Ex 3

def tup_Set(itm):

    tup = tuple(itm)

    set_tup = set(tup)

    return sorted(set_tup)


inp = ["Bat","Ball","Helmet","Stumps","Bat","Ball","Ball","Bat","Ball","Helmet","Stumps","Bat","Ball","Ball"]

print(tup_Set(inp))


"""

This function takes a list of strings and processes it in three steps:

1. Converts the list into a tuple.
2. Converts the tuple into a set to remove duplicate items.
3. Returns the unique items as a sorted list.

"""