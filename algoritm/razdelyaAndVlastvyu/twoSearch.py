import sys
from bisect import bisect_left   #уже готовый двоичный поиск


def find_pos(xs,query):
    lo = bisect_left(xs,query)    # i<lo:xs[i]<query
                                  # i>lo:xs[i]>=query


    if lo<len(xs) and xs[lo] ==query:
        return lo+1
    else:
        return -1
    
    
    
   # lo,hi = 0,len(xs) -1

   # while lo<=hi:
   #     mid=(lo+hi)//2
   #     if query<xs[mid]:
   #         hi = mid -1
   #     elif query > xs[mid]:
   #         lo = mid+1
   #     else:
   #         return mid+1
   # return -1
    
def test():
    assert find_pos([],42) == -1
    assert find_pos([42],42) == 1
    assert find_pos([42],24) ==-1



def main():
    reader= (map(int,line.split()) for line in sys.stdin)
    n,*xs = next(reader)
    k,*queries = next(reader)
    for query in queries:
        print(find_pos(xs,query),end=" ")



if __name__ =='__main__':
    test()
    main()
