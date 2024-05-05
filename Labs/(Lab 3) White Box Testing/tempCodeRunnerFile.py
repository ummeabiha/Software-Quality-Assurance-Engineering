x= int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
z=1

if (y<0): power = -y
else: power = y

while (power != 0):
    z*=x
    power-=1

if (y<0): z = 1/z
print("value of z : ", z)
