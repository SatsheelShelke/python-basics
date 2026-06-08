def my(nm,per,r,grd):
    print(nm,'has scored ',round(per,2),'%.Remark:',r,".Grade:",grd)


nm=str(input("enter name:"))
s1=float(input('Enter sub 1 marks:'))
o1=int(input('out of:'))
if s1>o1:
    print('out of marks cannot be bigger than obtained marks')
    exit()
s2=float(input('Enter sub 2 marks:'))
o2=int(input('out of:'))
if s2>o2:
    print('out of marks cannot be bigger than obtained marks')
    exit()
s3=float(input('Enter sub 3 marks:'))
o3=int(input('out of:'))
if s3>o3:
     print('out of marks cannot be bigger than obtained marks')
     exit()
s4=float(input('Enter sub 4 marks:'))
o4=int(input('out of:'))
if s4>o4:
    print('out of marks cannot be bigger than obtained marks')
    exit()
s5=float(input('Enter sub 5 marks:'))
o5=int(input('out of:'))
if s5>o5:
     print('out of marks cannot be bigger than obtained marks')
     exit()
tm=s1+s2+s3+s4+s5
to=o1+o2+o3+o4+o5
per=(tm/to)*100
per = (tm / to) * 100
print(round(per, 2), "%")
if per>90:
    r="Excellent"
    grd=("A+")
elif per>75:
    r="Very Good"
    grd=("A")
elif per>60:
    r="Good"
    grd=("B")
elif per>45:
    r="Average"
    grd=("C")
elif per>35:
    r="Bad"
    grd=("D")
else:
    r="Fail"
    grd=("F")

(my(nm,per,r))
