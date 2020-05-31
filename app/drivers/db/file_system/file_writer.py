import sys, os
from app.drivers.db.file_system.abstract_file_writer import abstractFileWriter


class FileWriter(abstractFileWriter):
    def __init__(self, filename):
        self._filename = filename
    
    def create_file(self, overwrite_if_exists):
        try:
            if overwrite_if_exists:
                f = open(self._filename , "w")
                f.close
            else:
                 f = open(self._filename , "x")
                 f.close
        except:
            print("Unable to write to file {}".format(self._filename))
            raise

    def delete_file(self):
        try:
            if os.path.exists(self._filename):
                os.remove(self._filename)
            else:
                print("The file does not exist")
        except:
            print("An error occurs trying to remove the file {}".format(self._filename))

    def write_to_file(self, contents, append,  delimiter = None):
        try:
            if append:
                f = open(self._filename , "a")
                f.write(contents)
                f.close 
            else:
                f = open(self._filename , "w")
                f.write(contents)
                f.close 
        except:
            print("Unable to write to file {}".format(self._filename))
            raise
