from pycoin.ecdsa import generator_secp256k1 as g

p = 2**256 - 2**32 - 977

def isOnCurve(x, y):
	return y**2 % p == (x**3 + 7) % p

print(isOnCurve(g.x(), g.y()))
g_4 = 4 * g
g_5 = 5 * g
print('4g =', g_4)
print('5g =', g_5)
print(isOnCurve(g_4.x(), g_4.y()))
print(isOnCurve(g_5.x(), g_5.y()))

d = 922053
g_d = d * g
print('dg =', g_d)
print(isOnCurve(g_d.x(), g_d.y()))

31 =  11111: 4m + 4a or 5m + 1s
32 = 100000

a ^ b

31
1 10 100 1000 10000


0111100011100001100111110
1000000000000000000000000
0000100000000000000000000

 0110111

 1000000
-0010000
 0001000
-0000001


11110: 4m + 3a
11110: 4m + 2s

 011110

 100000
-000010


4m + 1s
