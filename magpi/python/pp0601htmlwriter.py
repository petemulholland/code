# HTML Writer
# By Jaseman - 16th September 2012

import os

# Creates a file and opens it for writing (w)
f = open('/home/pi/test.html', 'w')

# Write lines of code into the file
# Note: avoid using " quotations, use instead '
f.write("<html>"+"\n")
f.write("<head>"+"\n")
f.write("<title>A Webpage Created by Python</title>"+"\n")
f.write("</head>"+"\n")
f.write("<body bgcolor='#ffffdd'>"+"\n")
f.write("<font face='verdana' color='#000000'>"+"\n")
f.write("<center>"+"\n")
f.write("<h1>THE HEADING</h1><p>"+"\n")
f.write("<hr>"+"\n")
f.write("</center>"+"\n")
f.write("<h3>A Subheading</h3><p>"+"\n")
f.write("This is the text of the first paragraph.<p>"+"\n")
f.write("<hr>"+"\n")
f.write("<center>"+"\n")
f.write("<font size='2'>"+"\n")
f.write("<b><a href='mailto:editor@themagpi.com'>EMAIL</a></b><p>"+"\n")
f.write("<b><a href='http:www.themagpi.com'>WEBSITE</a></b><p>"+"\n")
f.write("</body>"+"\n")
f.write("</html>")

# Close the file
f.close()

# Open the html file with Midori browser
os.system("midori /home/pi/test.html")