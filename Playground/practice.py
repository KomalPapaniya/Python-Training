import gdown
import zipfile

url = "https://drive.google.com/file/d/1Aeh4GIjLwyiuWGd6AGxM8Q3WgiffLfIu/view?usp=sharing"
output = "Exam.zip"
obj = gdown.download(url, output, quiet=False,fuzzy=True)


pathOfUnzipFolder = 'C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training'

with zipfile.ZipFile('C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\Exam.zip', 'r') as zip_ref:
    zip_ref.extractall(pathOfUnzipFolder)