class add:
    def sum(self,a=0,b=0,c=0):
        if b>0:
            print("a+b+c = {} ".format(a+b+c))
        else:
            print("a+b ={} ".format(a+b))

c1=add()
c1.sum(10,20,30)
c1.sum(20,30)

#-----------------------------------Several Arguments-----------------------------------
class calculate:
    def add(self,*args):
        result =0
        for param in args:
            result+= param
        print("Result :{}".format(result))

a1=calculate()
a1.add(12,13,14,15,16)
a1.add(5,6)