from ass_2 import LogFormatter, CsvFormatter, WriteFile

writecsv = WriteFile( "my_delim_file", CsvFormatter )
writelog = WriteFile( "my_lofile",  LogFormatter )

writecsv.write(["we die, it", "i think", "but who knows"])
writelog.write("what time is it")

writecsv.write(["fsfsd","ddmssdcs", "akd,loe" ])
writelog.write("yep")

writecsv.close()
writelog.close()




