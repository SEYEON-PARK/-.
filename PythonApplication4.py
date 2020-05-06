
a = 'My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.'

#과제 2-3 주민번호를 뒷자리 1자리만 남기고 지워라

a = a.replace("!"," ");
a = a.replace(".", " ")
a = a.rstrip()
a = a+'.'
print(a)