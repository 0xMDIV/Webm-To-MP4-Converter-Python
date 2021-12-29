import glob
import os
import sys
import time

from ffmpeg_converter import *

ffmpeg = FFMPEG_Converter()


def menu():
    try:
        choice = int(input("1. Convert one file\n2. Convert all Files in dir\n> "))
        if choice == 1:
            convert_file()
        elif choice == 2:
            convert_dir()
        else:
            print("Choose 1 or 2")
    except KeyboardInterrupt:
        print("Aborted, Program Closing")
        time.sleep(2)
        sys.exit()


def convert_file():
    try:
        input_file = input("Bitte geben den Pfad zur Datei an: ")
        output_file = input_file.replace(".webm", ".mp4")
        if len(input_file) > 5 and len(output_file) > 5:
            print("transformating, please wait...")
            ffmpeg.convert_webm_mp4_subprocess(input_file, output_file)
            os.remove(input_file)
    except KeyboardInterrupt:
        print("Aborted, Program Closing")
        time.sleep(2)
        sys.exit()


def convert_dir():
    dirname = input("Bitte gib den Ordner Pfad ein:\n> ") + "\\*.webm"
    if len(dirname) > 5:
        for filename in glob.glob(dirname, recursive=True):
            try:
                print("transformating, please wait...")
                output_file = filename.replace(".webm", ".mp4")
                ffmpeg.convert_webm_mp4_subprocess(filename, output_file)
                os.remove(filename)
            except KeyboardInterrupt:
                print("Aborted, Program Closing")
                time.sleep(2)
                sys.exit()


while True:
    menu()