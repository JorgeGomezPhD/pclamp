# This file sets the file path and file name
import pyabf

folder = input("Enter folder name where data is stored: ")
file_number = input("Enter last 2 digits of file: ")
file_name = f"{folder}/{folder}0{file_number}.abf"
abf = pyabf.ABF(file_name)
