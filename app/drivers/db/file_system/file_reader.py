import os
import platform
from app.drivers.db.file_system.abstract_file_reader import abstractFileReader


class FileReader(abstractFileReader):

    def __init__(self, filename):
        self._filename = filename

    def read_file(self):
        try:
            f = open(self._filename, "r")
            contents = f.read()
            f.close
            return contents, self.creation_date()
        except:
            print("Unable to read file {}".format(self._filename))
            return None

    def creation_date(self):
        """
        Try to get the date that a file was created, falling back to when it was
        last modified if that isn't possible.
        From https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
        See http://stackoverflow.com/a/39501288/1709587 for explanation.
        """
        if platform.system() == 'Windows':
            return os.path.getctime(self._filename)
        else:
            stat = os.stat(self._filename)
            try:
                return stat.st_birthtime
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                return stat.st_mtime

    def is_substring_in_file(self, substring):
        try:
            f = open(self._filename, "r")
            contents = f.read()
            f.close
            return substring in contents
        except:
            print("Unable to read file {}".format(self._filename))
            return None
