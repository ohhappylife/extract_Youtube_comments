def getID(filename = 'link.txt'):
  urlList = []
  ids = []
  with open(filename) as file:
    for line in file:
      urlList.append(line.rstrip())
  for url in urlList:
    ids.append(url.split("=")[1].split("&")[0])
  return ids