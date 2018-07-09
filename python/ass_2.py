import datetime

class WriteFile(object):
    """
    Master object class for all files
    """
    def __init__(self,file_name, file_formater):
        self.file=open(file_name, "a+")
        self.file_formatter = file_formater()
    def write(self, text):
        line = self.file_formatter.create_line(text)
        self.file.write(line)
        self.file.write( "\n")
    def close(self):
        self.file.close()

class LogFormatter(object):
    """
    class for log files
    """
    def create_line(self, input_string):
        log_time = datetime.datetime.now().strftime("%Y-%m-%d :")
        return log_time + input_string

class CsvFormatter(object):
    """
    class for delimited files
    """
    def create_line(self, input_string_array):
        entries = [ entry if "," not in entry else "'"+entry+"'" for entry in input_string_array ]
        return ",".join(entries)


