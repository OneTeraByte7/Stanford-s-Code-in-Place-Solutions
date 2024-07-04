"""Question : returns a nested list where each element is a list containing 
              the index of an element in the original list and the element itself. 
              These lists should appear in increasing order of indices.
"""

def enumerate(lst):
    enum_lsts = []
    for i in range(len(lst)):
    	val = lst[i]
        enum_lsts.append([i, val])
    return enum_lsts
