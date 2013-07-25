aFile1 = File.new("testFile1.txt", "w")
if aFile1
	aFile1.syswrite("This is a test write")
	puts "have written to file."
	aFile1.close
else 
	puts "could not open file for write"
end

aFile2 = File.open("testFile1.txt", "r")
if aFile2
	puts "reading from file"
	content = aFile2.sysread(20)
	puts content
	aFile2.close
else 
	puts "could not open file for read"
end

# now with blocks?

File.open("aFile2.txt", "w+") do |theFile|
	puts "writing to file"
	theFile.puts("This is the first line of this file")
	theFile.puts("This is the second line of this file")

	puts "rewinding & reading the file"
	theFile.rewind
	puts theFile.readline
	puts theFile.readline
end


# try each on file
File.open("aFile2.txt", "r+") do |theFile|
	puts "writing contents of file using 'each' method"
	theFile.each {|line| print line}
end


