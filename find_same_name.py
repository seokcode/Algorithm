def solution(name: list):
  result = set()

  for i in range(len(name)-1):
    for j in range(i+1, len(name)):
      if name[i] == name[j]:
        result.add(name[i])
  return result
