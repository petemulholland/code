srand()
x = rand(10) + 1
picked = false
guess = 0
while not picked
	if guess == 0
		puts 'Guess the number between 1 and 10'
	elsif guess == x
		puts "Well done! you guessed #{x}"
		picked = true
	elsif guess < x
		puts 'Guess higher: '
	else
		puts 'Guess lower: '
	end
	guess = gets.chomp.to_i
end
