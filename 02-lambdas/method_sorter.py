def sorter(item):
    return item['name']

presenters = [
  {'name': 'Susan'},
  {'name': 'Christopher'}
]

presenters.sort(key=sorter)
print(presenters)
