file = open("forest.txt", "r")
data= file.read()
file.close()
file = open("fores.txt", "w")
data= file.write(data)
data_len = data
file.close()
print(data_len)