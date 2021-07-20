input_data = str(input()).split()
print('[', end=' ')
MAGICIAN = [print('"', (input_data[i]), '"', end=' ') for i in range(len(input_data))]
print(']')
