A = 4
B = 11

# Bitwise OR
C =A|B
print('n-----------OR-------------')
print('nilai: ', A, ', Binary: ', format(A,'08b'))
print('nilai: ', B, ', Binary: ', format(B,'08b'))
print('-----------------------------(|)')
print('nilai: ', C, ', Binary: ', format(C,'08b'))

# Bitwise right shift
C = A>>B
print('--------------RIGHT SHIFT-------------')
print('nilai: ', A, ', Binary: ', format(A,'08b'))
print('nilai: ', B, ', Binary: ', format(B,'08b'))
print('------------------------------(>>)')
print('nilai: ', C, ', Binary: ', format(C,'08b'))

# Bitwise XOR
C = A^B
print('--------------XOR-------------')
print('nilai: ', A, ', Binary: ', format(A,'08b'))
print('nilai: ', B, ', Binary: ', format(B,'08b'))
print('------------------------------(^)')
print('nilai: ', C, ', Binary: ', format(C,'08b'))

# Bitwise NOT
C = ~A
print('--------------NOT-------------')
print('nilai: ', A, ', Binary: ', format(A,'08b'))
print('nilai: ', B, ', Binary: ', format(B,'08b'))
print('------------------------------(~)')
print('nilai: ', C, ', Binary: ', format(C,'08b'))

#bitwise AND
C = A & B
print('--------------AND-------------')
print('nilai: ', A, ', Binary: ', format(A,'08b'))
print('nilai: ', B, ', Binary: ', format(B,'08b'))
print('------------------------------(&)')
print('nilai: ', C, ', Binary: ', format(C,'08b'))