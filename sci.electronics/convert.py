import os
for filename in os.listdir("."):
  if len(filename.split(".")) ==3:
    os.rename(filename,"/home/w/ml/sci.electronics.json/" +filename.split(".")[0]+".json")
