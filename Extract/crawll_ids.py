def getID(urls):
  urlList = []
  ids = []
  for line in urls:
    urlList.append(line.rstrip())
  for url in urlList:
    ids.append(url.split("=")[1].split("&")[0])
  return ids