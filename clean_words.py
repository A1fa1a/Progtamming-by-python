def cleanWords(words):
  if len(words) == 1:
    return words

  if words[0] == words[1]:
    return cleanWords(words[1:])

  return words[0] + cleanWords(words[1:])

print(cleanWords("wwworlld"))
