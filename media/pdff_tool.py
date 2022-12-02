
#==== working pdf extracter on a list ===
import os
import PyPDF2
path = os.getcwd()
pth = os.path.join(path,"media/")
pdflist =[]
pdffilesname = [] 
for files in os.listdir(pth):
    if files.endswith('.pdf'):
        str2 = files[:-4]
        pdffilesname.append(str2)
        pdflist.append(pth+files)
for pdfs in pdflist:
    pdfObj = PyPDF2.PdfFileReader(pdfs)
    pg = pdfObj.numPages
    str = ""
    for i in range(1,pg):
        str += (pdfObj.getPage(i).extractText())
    for name in pdffilesname:
        text_file = open(os.path.join(path,"PDF_Extracted_Data/{}.txt".format(name)), "w")
        text_file.write(str)
        text_file.close()
print("Extraction DONE ! ")     





























#older version -----------------
# import os
# import PyPDF2
# path = os.getcwd()
# pth = os.path.join(path,"media/")
# pdflist =[]

# for files in os.listdir(pth):
#     if files.endswith('.pdf'):
#         str = pth+files
#         pdflist.append(str)
# count = 1        
# for pdfs in pdflist:
#     a = PyPDF2.PdfFileReader(pdfs)
#     pg = a.numPages
#     str = ""
#     for i in range(1,pg):
#         str += (a.getPage(i).extractText())

#     text_file = open(os.path.join(path,"Extracted_Data/{}pdf.txt".format(count)), "w")
#     text_file.write(str)
#     text_file.close()
#     count+=1



# #Another method on file save 
# import os
# import PyPDF2
# path = os.getcwd()
# pth = os.path.join(path,"media/")
# pdflist =[]
# pdffilesname = [] 
# for files in os.listdir(pth):
#     if files.endswith('.pdf'):
#         str2 = files[:-4]
#         pdffilesname.append(str2)
#         pdflist.append(pth+files)
# for pdfs in pdflist:
#     a = PyPDF2.PdfFileReader(pdfs)
#     pg = a.numPages
#     str = ""
#     for i in range(1,pg):
#         str += (a.getPage(i).extractText())
#     for name in pdffilesname:
#         text_file = open(os.path.join(path,"Extracted_Data/{}.txt".format(name)), "w")
#         text_file.write(str)
#         text_file.close()
   









# previous version ----
# 
# 
#     
# import os
# import PyPDF2
# path = os.getcwd()
# pth = os.path.join(path,"media/")
# pdflist =[]

# for files in os.listdir(pth):
#     if files.endswith('.pdf'):
#         str =pth+files
#         pdflist.append(str)
# count = 1        
# for pdfs in pdflist:
#     a = PyPDF2.PdfFileReader(pdfs)
#     pg = a.numPages
#     str = ""
#     for i in range(1,pg):
#         str += (a.getPage(i).extractText())

#     text_file = open("/home/akashk/Desktop/Workspace/project1/Extracted_Data/{}pdf.txt".format(count), "w")
#     text_file.write(str)
#     text_file.close()
#     count+=1



# trying some other methods or trying to optmizing code 

# import os
# import PyPDF2
# path = os.getcwd()
# pth = os.path.join(path,"media/")
# pdflist =[]

# for files in os.listdir(pth):
#     if files.endswith('.pdf'):
#         str =pth+files
#         pdflist.append(str)
# count = 1             
# # for pdfs in pdflist:    
# a = PyPDF2.PdfFileReader(pdflist[0])
# pg = a.numPages
# str = ""
# for i in range(1,):
#     str += (a.getPage(i).extractText())
# text_file = open(pth+"data.txt", "w")
# text_file.write(str)
# text_file.close()
# count+=1

#         str += (a.getPage(i).extractText())

#     text_file = open("/home/akashk/Desktop/Workspace/project1/Extracted_Data/{}pdf.txt".format(count), "w")
#     text_file.write(str)
#     text_file.close()
#     count+=1


# import os 
# print(os.getcwd())



# path = "/home/akashk/Desktop/Workspace/project1/media"
# print(os.path.join(path,"xyz","A.pdf"))


# import os
# import PyPDF2
# path = os.getcwd()
# pth = os.path.join(path,"media")
# pdflist =[]

# for files in os.listdir(pth):
#     print(files)
#     if files.endswith('.pdf'):
#         str =os.path.join+files
#         pdflist.append(str)