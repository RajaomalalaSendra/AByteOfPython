print ('{0:.3f}'.format(1.0/3))
print('{0} / {1} = {2:.3f}'.format(3, 4,3/4 ))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print ('{0:_^9}'.format('hello'))
def variable(name=''):
    print('{0:*^12}'.format(name))
variable()
print('{0:*^12}'.format('sendra'))
variable()
# keyword-based 
print ('{name} read {book} now.'.format(name='My Lovely Friend Sendra', book='A Byte of Python'))