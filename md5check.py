from asyncio.windows_events import NULL
import hashlib
import argparse
from pickle import TRUE
from types import NoneType
parser = argparse.ArgumentParser()


parser.add_argument("-f", "--file", help = "Input file", default = "None")

args = parser.parse_args()

if args.file == "None":
    print("Please use -f flag to select file")
    quit()
    

print("Please paste the md5 checksum to compare:")
md5sum = input()

with open(args.file, "rb") as f:
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)

md5_checked = file_hash.hexdigest()
print(file_hash.hexdigest())

if md5sum == md5_checked:
    print("MD5 Checksum Matches!")

else:
    print("MD5 Checksum Error!")