

def solution(s):
  # Your solution starts here.
  kata = s
  if kata == s[::-1]:
    return True
  else:
    frekuensi = {}
    for karakter in s:
      if karakter in frekuensi:
        frekuensi[karakter] +=1
      else:
        frekuensi[karakter] = 1
    
    karakter_ganjil = 0
    for nilai in frekuensi.values():
      if nilai % 2 != 0:
        karakter_ganjil += 1
    
    if karakter_ganjil <= 1:
      return True
  return False
