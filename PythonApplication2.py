#과제 2-1 공백2개를 1개로 바꾸고 :는 ,로 바꾼다. 단, 모든 함수는 1번만 사용가능

a = 'My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.'
a = a.split("  ")
a = " ".join(a)
a = a.replace(":",",")
print(a);