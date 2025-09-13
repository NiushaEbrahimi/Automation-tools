import os
from pathlib import Path

a="/Users/MSI/Downloads"

list = os.listdir(Path(a))
list_1 = a.split("/")
print("\n" , list_1[-1],":")
for f in list:
    print(f"\t-{f}")