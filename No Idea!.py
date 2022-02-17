#array of n ints, and a set A and B, each cotaining m integers
#Like all in set A and dislike all in set B
#if array has a number in set A then happiness +1, if array has number in set B happy-1
#The difficulty in this comes from efficiency. the ints can reach 10^9 and the sizes can reach 10^5
#naively for each element in array, would have to permute across entire of both sets each time to find if present
#one way to shorten would be to update each set disregarding elements which are in both A and B
#but that requires processing time of two permutations. and could also make set of array and find intersections with A and B,
#to weed out unwanted numbers. would it be worth the time to creat sorted list of A and B?

#this doesn't work

def bin_search(entry, point_change_list, low, high):
    mid = (high + low) // 2
    rangesize = high-low
    if point_change_list[mid] == entry:
        return True
    elif rangesize < 0:
        return False
    elif point_change_list[mid] > entry:
        bin_search(entry,point_change_list,low,mid)
    elif point_change_list[mid] < entry:
        bin_search(entry,point_change_list,mid+1,high)



if __name__=='__main__':
    happiness = 0
    nm = list(map(int,input().split()))
    n = nm[0]
    m = nm[1]
    array = list(map(int,input().split()))
    A_raw = set(map(int,input().split()))
    B_raw = set(map(int,input().split()))
    A = A_raw.difference(B_raw)
    B = B_raw.difference(A_raw)
    A_list = sorted(A)
    B_list = sorted(B)
    for j in range(len(A_list)):
        if bin_search(array[j],A_list,0,m-1):
            happiness += 1
    for k in range(len(B_list)):
        if bin_search(array[j],B_list,0,m-1):
            happiness -= 1
    print(happiness)
