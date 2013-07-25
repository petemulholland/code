test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
index = 0
test.each { |item|
if (index + 1) % 4 == 0
  puts item
else
  print item
  print ", "
end
index += 1
}

test.each_slice(4) { |s| p s }