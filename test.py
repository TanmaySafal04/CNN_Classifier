from pathlib import Path
import os

filepath="src/CNNClassifier/components/__init__.py"
filedir, filename = os.path.split(filepath)
print(filedir,' ', filename)
print()
print(os.path.split(filepath))