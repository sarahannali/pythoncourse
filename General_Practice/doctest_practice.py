'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(x):
    """
    >>> last_element([1,2,3])
    3
    >>> last_element([1,2,3,'a',4,5,'b'])
    'b'
    """
    if x:
        y = len(x) - 1
        return (x[y])
    pass