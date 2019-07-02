def asterisco(a):
	if(a == 1):
		print('*', end = '')
	else:
		print('*', end = '')
		asterisco(a - 1)

def underscore(u, a):
	if(u == 0):
		asterisco(a)
	else:
		print('_', end = '')
		underscore(u - 1, a)
		print('_', end = '')

def impressao(n, i):
    if n > 0:
        underscore(n-1, i)
        print()
        impressao(n-1, i+2)

def piramide(n):
    i = 1
    impressao(n, i)

piramide(6)