import pprint
import random
import copy


'''
    Method to generate a stable match between lists of m and w
    Basic implementation of Gale-Shapley algorithm
    Params:
        wPriority - list of the m preferences for each w (index i corresponds to w_i)
        mPriority - list of the w preferences for each m (index i corresponds to m_i)
        mlist - list of the matches of each m (-1 is unmatched)
        wlist - list of the matches of each w (-1 is unmatched)
'''
def StableMatch(wPriority, mPriority, mlist, wlist):
    while -1 in mlist:
        m = mlist.index(-1)
        w = mPriority[m][0]

        propose(m, w, mlist, wlist, wPriority)

        # don't want to propose to this girl again so remove her from m's priority list
        mPriority[m].remove(w)        
    
'''
    Helper function for StableMatch to check a possible proposal between an m and w
'''
def propose(m, w, mlist, wlist, wPriority):
    # if w is unmatched, match
    print(str(m) + ' proposes to ' + str(w))
    if wlist[w] == -1:
        mlist[m] = w
        wlist[w] = m
    # if w is matched, check priorities
    else:
        if wPriority[w].index(m) < wPriority[w].index(wlist[w]): # check the index thing here
            # unmatch current, match to m
            print(str(w) + ' is going from matching with ' + str(wlist[w]) + ' to matching with ' + str(m))
            mlist[wlist[w]] = -1
            mlist[m] = w
            wlist[w] = m        

''''
    Main method
    Params:
        n - input size (number of m/w)
'''
def main(n):
    # some hard coded lists
    #       vvv
    mPriority = [[2, 1, 3, 0], [0, 1 ,3, 2], [0, 1, 2, 3], [0, 1, 2, 3]]
    wPriority = [[0, 2, 1, 3], [2, 0, 3, 1], [3, 2, 1, 0], [2, 3, 1, 0]]

    # this is the random functionality lines 55-61
    #       vvv
    # mPriority = []
    # wPriority = []

    # for i in range(n):
    #     mPriority.append(permutation(n))
    #     wPriority.append(permutation(n))

    # copies to later calculate the goodness scores
    originalMPriority = copy.deepcopy(mPriority)
    originalWPriority = copy.deepcopy(wPriority)    

    # filling both lists with -1 which means no match yet
    mlist = [-1] * n
    wlist = [-1] * n


    StableMatch(wPriority, mPriority, mlist, wlist)

    print('terminated. this leaves with final mlist: ')
    pprint.pprint(mlist)

    # calculate the goodness
    print(' the goodness score for m is ' + str(matchGoodness(mlist, originalMPriority)))
    print(' the goodness score for w is ' + str(matchGoodness(wlist, originalWPriority)))


'''
    Generates random array of n integers between 0 and n - 1
    Used to populate random wPriority and mPriority lists
    Params:
        n - size of list (number of m/w)
'''
def permutation(n):
    arr = list(range(n))

    for i in range(n):
        j = random.randint(0, i)
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    return arr

def matchGoodness(xlist, xPriority):
    # check each index of xlist to see what x_i matched with
    # cross reference match with xPriority to get xGoodness
    res = 0
    for i, n in enumerate(xlist):
        # priority list for i, index (score) of i's result match
        res += xPriority[i].index(n)
    res = (res / len(xlist))
    return res


main(4)