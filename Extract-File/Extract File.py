from zipfile import ZipFile
file_path = "zipfile.zip"
with ZipFile(file_path, "r") as zip_:
    zip_.printdr()

    zip_.extractall()
