def doSomeCheck(str1,str2):
  newPass=None
  for i in range(len(str1)):
    for j in range(i+1,len(str2)):
      if str1[i]==str2[j]:
        if not (i+j)%2:
          newPass=str2[0:i]+str2[j]+str2[i+1:j]+str2[i]+str2[j+1:]
          str2=newPass
          if str1==str2:
            return 1
  return 0

def checkPassword(n,arr):
  if n==1:
    return 1
  else:
    count=0
    for i in range(n):
      checkCount=0
      for j in range(i+1,n):
        if len(arr[i]) != len(arr[j]):
          checkCount+=1
          break;
        checkCount+=doSomeCheck(arr[i],arr[j])
      if checkCount>0:
        count+=1
  return n-count

if __name__=='__main__':
  str2='abcdefg'
  i,j=0,5
  newPass=str2[j]+str2[0:i]+str2[i+1:j]+str2[i]+str2[j+1:]
  print(newPass)
  val=checkPassword(7,['abcd','cbad','adcb','cdab','jklm','lkjm','mklo'])
  print(val)