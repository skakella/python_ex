#
# Example file for working with classes
#
class myClass():
   def method1(self):
       print("I am myClass - method1")

   def method2(self,str1):
       print("I am myClass - method2 " + str1)

class childClass(myClass):
   def method1(self):
       print("I am childClass - method1")

   def method2(self,str1):
       print("I am childClass - method2 " + str1)
       myClass.method1(self)
 


def main():
    c =  myClass()
    c.method1()
    c.method2("Hello")

    d = childClass()
    d.method1()
    d.method2("Hi")


if __name__ == "__main__":
    main()
