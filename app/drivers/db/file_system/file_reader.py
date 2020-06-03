import os
import platform
from logger import log

class FileReader:

    def read_file(self, filename):
        try:
            f = open(filename, "r")
            contents = f.read()
            f.close
            log.debug(f"Contents of file {filename} successfully read from persistent disk")
            return contents
        except:
            log.error(f"Unable to read file {filename}")
            return None

    def creation_date(self, filename):
        """
        Try to get the date that a file was created, falling back to when it was
        last modified if that isn't possible.
        From https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
        See http://stackoverflow.com/a/39501288/1709587 for explanation.
        """
        if platform.system() == 'Windows':
            return os.path.getctime(filename)
        else:
            stat = os.stat(filename)
            try:
                return stat.st_birthtime
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                log.error(f"Unable to find the creation file for the file {filename}, falling back to last modified time")
                return stat.st_mtime

    def is_substring_in_file(self, filename, substring):
        try:
            f = open(filename, "r")
            contents = f.read()
            f.close
            found =  substring in contents
            log.debug(f"The substring {substring} was found in file {filename}")
        except:
            log.error(f"Unable to read file {filename}")
            return None
