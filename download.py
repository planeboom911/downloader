#@title Superfast downloader ;)
from google.colab import drive
from google.colab import files
import os
drive.mount('/content/drive')
url = "" #@param {type: "string"}
download_filename = "file.bin" #@param {type: "string"}
download_loc = f"/content/drive/MyDrive/${download_filename}"

!curl -L -o "$download_loc" "$url"
files.download(download_loc)
