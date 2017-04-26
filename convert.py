import os
for filename in os.listdir("."):
  if len(filename.split(".")) ==3:
    os.rename(filename,"/home/w/ml/sci.space.json/" +filename.split(".")[0]+".json")
