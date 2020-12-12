from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from tkinter import *
from tkinter.filedialog import askopenfilename
from pathlib import Path




Tk().withdraw()
path = askopenfilename(title="Select your PDF document")


reader = PdfFileReader(path)
writer = PdfFileWriter()


root = Tk()
root.title("PDF PAGE DELETER")
root.geometry("600x400")
txt = Label(root, text= "Which pages in your document would you like to remove?")
e = Entry(root)

def parseEntry(user_entry):
  retVal = set()
  user_entry_nospace = user_entry.replace(" ", "")
  strlist = user_entry_nospace.split(";")
  
  for w in strlist:
    if w.isdigit():
      retVal.add(int(w)-1)
    else:
      two_nums_str = w.split("-")
      two_nums = []
      for m in two_nums_str:
        two_nums.append(int(m))
      mini = min(two_nums)
      maxi = max(two_nums)
      for i in range(mini,maxi+1):
        retVal.add(i-1)

  return retVal


def delete():
  user_entry = e.get()
  pagelist = parseEntry(user_entry)
  maximum = reader.getNumPages()
  for i in range(maximum):
   if i not in pagelist:
    writer.addPage(reader.getPage(i))

  with Path("editedFile.pdf").open(mode='wb') as editFile:
    writer.write(editFile) 
  root.destroy()
  sys.exit()

b = Button(root, text="Delete", command = delete)
txt.pack()
e.pack()
b.pack()





root.mainloop()
