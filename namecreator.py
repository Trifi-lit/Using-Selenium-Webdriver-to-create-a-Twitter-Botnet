import random
import string

f = open("names.txt", "r")
name=[]
for i in range(100):
  A=f.readline().strip()
  A=A.replace(" ", "")
  name.append(A)
print(name)
f.close()

#for passwords
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    #print("Random string of length", length, "is:", result_str)
    return result_str

b="#EktelionArmy"

with open('data.txt', 'w') as f:
  for i in range(12):

    n=random.randrange(1, 100)
    m=random.randrange(100, 999)
    myname=name[n]
    myname=myname+str(m)


    p=get_random_string(8)
    password=str(p)+str(m)

    month=str(random.randrange(1, 12))
    day=str(random.randrange(1, 28))
    year=str(random.randrange(1960,2000))
    bio=b

    f.write(myname)
    f.write('\n')
    f.write(password)
    f.write('\n')
    f.write(month+'\t'+day+'\t'+year)
    f.write('\n')
    f.write(bio)
    f.write('\n\n')