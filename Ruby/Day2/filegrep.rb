search_string = ARGV.shift
ARGF.each_with_index{|line, idx|
 if (/#{search_string}/.match(line))
   puts "#{idx}:#{line}"
 end
}