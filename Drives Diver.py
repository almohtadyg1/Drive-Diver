import os
  
which = input("Which drive you have to open ? C , D or E:\n")
  
if "C" in which or "c" in which:
  os.system("C:")
    
elif "D" in which or "d" in which:
  os.system("D:")
  
elif "E" in which or "e" in which:
  os.system("E:")
  
else:
    print("Wrong Input")