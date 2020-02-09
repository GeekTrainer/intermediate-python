with open('output.txt', 'wt') as stream:
	stream.write('Lorem ipsum dolar')

"""
Same as this code:
try:
	stream = open('output.txt', 'wt')
	stream.write('Lorem ipsum dolar')
finally:
	stream.close() # THIS IS REALLY IMPORTANT!!
"""