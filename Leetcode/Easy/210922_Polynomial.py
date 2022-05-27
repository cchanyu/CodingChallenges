def polynomial(px, c):
    px[c] = a0
    for i in n:
        pc += ai 


px = (11, 3, 7, 5)
c = 2
polynomial(px, 2)

'''
1+2+3+4+5+6 = 21
1*2*3*4*5*6 = 6! = 720

(n!)! >> 2^n

TSP

given: item weights: w1...wn
each trip: can only carry 100lbs
decide which items to carry when
goal: minimize number of trips

: 51, 30, 40, 30, 49

no (known) poly-time alg
O(n^k)
"bin packing"

*roughly* 2^n

2^n >> n^30 (2^n is way worse than n^30)

m procs:
T(n) -> T(n)/m

T(n) -> T(n)/log(m)

T(n)/m << T(n)/log(m) [1/m much smaller than 1/log(m)]

m >> log(m)

2^m vs. 2^(log_2(m)) = m


bin-packing, TSP in "NP-Complete"

Example1:
A = [4,6,4,40,36,60,43,36,7788,5655,43,7,...]
n=1000

S = sum of them
T = the rest
want: find an S and T so that sum(S) = sum(T)
sum(S) = 1/2 * sum(all)

suppose nums: A=[5,6]

new(simpler?) problem:
input: A
then you have to tell me: is it possible?

"decision problem" - I give you the instance and ask yes/no question. 

solvable in O(2^n) (brute force)
faster?? not if must be correct on all inputs


n=3  -> 2^3 ways

2^n diff poss ways to sep into 2 sets

n*2^n

n^4
'''