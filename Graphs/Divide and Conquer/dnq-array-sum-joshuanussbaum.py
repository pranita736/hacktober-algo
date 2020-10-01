# Simple Divide & Conquer Algorithm!

def d_a_c(ar):
	# Base Case:
	if len(ar) < 2:
		return ar[0]
	# Recursive Steps
	l_ar = ar[:(len(ar) / 2)]
	r_ar = ar[(len(ar) / 2):]
	return (d_a_c(l_ar) + d_a_c(r_ar))
