file "#{ENV['HOME']}/example.txt" do
  action :create
  content "Greetings #{ENV['USER']}!"
end
