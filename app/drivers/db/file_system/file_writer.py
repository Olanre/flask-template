import sys, os
from logger import log

class FileWriter:
    
    def create_file(self, filename,  overwrite_if_exists):
        try:
            if overwrite_if_exists:
                f = open(filename , "w")
                f.close
            else:
                 f = open(filename , "x")
                 f.close
            log.debug("Created the file " + filename + " with overwrite parameter {overwrite_if_exists}")
        except:
            log.error("Unable to write to file {}".format(filename))
            raise

    def delete_file(self, filename):
        try:
            if os.path.exists(filename):
                os.remove(filename)
                log.debug(f"Successfully deleted the filename {filename}")
            else:
                log.error(f"The file {filename} does not exist")
        except:
            log.error(f"An error occurs trying to remove the file {filename}")

    def write_to_file(self, contents, append,  filename, delimiter = None):
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
            print(f"Unable to write to file {filename}")
            raise
