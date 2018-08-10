import PyPDF2, os
# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('pdfs/'): #pdfs/ is the path of the directory - replace as appropriate
    if filename.endswith('.pdf'):
        pdfFiles.append('pdfs/'+filename)
wordToFind = 'surveillance'      #the text we want to find
    # Loop through all the PDF files.
for filename in pdfFiles:
    foundTheWord = False
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    print("processing ... "+filename)
    #Loop through the pages of the file and extract the text
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        try:
            pageText = pageObj.extractText().lower()
            if wordToFind in pageText:
                foundTheWord = True
        except:
            error = "Error"
    if foundTheWord == True:
        print('Found in:'+filename) #display the name of the file where the text was found

