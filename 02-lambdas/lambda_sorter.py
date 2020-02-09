# Sort alphabetically
presenters = [
  {'name': 'Susan'},
  {'name': 'Christopher'}
]

presenters.sort(key=lambda item: item['name'])
print('-- alphabetically --')
print(presenters)

# Sort by length (short to long)
presenters.sort(key = lambda item: len(item['name']))
print('-- length --')
print(presenters)
