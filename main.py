#!/bin/python
import sys
import hash_operator as h_op
import btree_operator as b_op

arg_string = sys.argv

if len(arg_string) < 5:
	print("Arguments expected : name of relation, number of attributes, number of blocks, type_of_index ( hash or btree ) ")
	sys.exit(0)

R = arg_string[1]
n = int(arg_string[2])
M = int(arg_string[3])
type_of_index = arg_string[4]
B = 100
b=b_op.Btree_operator(B)
h=h_op.Hash_operator(B)

if type_of_index=='hash':
    h.main(R,n,M)
    print(h.time)

elif type_of_index == 'btree':
    b.main(R,n,M)
    print(b.time)