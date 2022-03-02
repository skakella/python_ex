#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop

  # while ( x < 5):
  #   print (x)
  #   x = x + 1


  # define a for loop
  # for i in range(3, 9) :
  #    print(i)

  # use a for loop over a collection
  # days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

  # for i, d in enumerate(days):
  #   print(i," " ,d)
  
  # use the break and continue statements
  for i in range(3, 9) :
    if i % 2 == 0: continue
    print(i)

  #using the enumerate() function to get index 
  
if __name__ == "__main__":
  main()
