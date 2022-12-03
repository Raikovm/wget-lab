import sys
import os
import requests
import typer

def main(url: str):
   file_name = os.path.basename(url)
   download_bar_length = 50
   with open(file_name, "wb") as file:
      print("Downloading %s" % url)
      response = requests.get(url, stream=True)
      total_length = response.headers.get('content-length')

      downloaded = 0
      total_length = int(total_length)
      for data in response.iter_content(chunk_size=1024):
          downloaded += len(data)
          file.write(data)
          done = int(download_bar_length * downloaded / total_length)
          sys.stdout.write("\r[%s%s] %s/%s bytes" % ('■' * done, '□' * (download_bar_length - done), downloaded, total_length) )    
          sys.stdout.flush()
      print("\nDone!")

if __name__ == "__main__":
   typer.run(main)
   