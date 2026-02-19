def find_max_number(num1, num2, num3):
  if (num1>=num2 and num1>=num3):
    return num1
  if (num2>=num3):
    return num2
  return num3
def find_mean(num1, num2, num3):
    meanv = (num1+num2+num3)/3
    return meanv
def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    std = (((num1-mean)**2+(num2-mean)**2+(num3-mean)**2)/3)**0.5
    return mean,std

