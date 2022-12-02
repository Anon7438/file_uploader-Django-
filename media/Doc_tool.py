from docx import Document
import os 

docname = []
docslist = []
path1 = os.getcwd()
path = os.path.join(path1,'media/')
for files in os.listdir(path):
    if files.endswith('.docx'):
        str2 = files[:-5]
        docname.append(str2)
        docslist.append(path+files)
        
for doc in docslist:   
        doc = Document(doc)
        str = ''
        for para in doc.paragraphs:
            str += (para.text)
       
        for name in docname:
            text_file = open(os.path.join(path1,"Doc_Extracted_Data/{}.txt".format(name)), "w")
            text_file.write(str)
            text_file.close()

            
print("Extraction DONE ! ")  


