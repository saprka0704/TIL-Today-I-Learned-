#making a password for google

url = "https://google.com"

my_str = url.replace("https://","")
my_str = my_str[:my_str.index(".")]

password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + "!"

print("The password for {0} is {1}".format(url,password))
