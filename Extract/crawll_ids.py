def getID(urls):
  urlList = []
  ids = []
  for url in urls:
    urlList.append(str(url))
  for url in urlList:
    ids.append(url.split("=")[1].split("&")[0])
  return ids