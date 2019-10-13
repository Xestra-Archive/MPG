from timeit import default_timer as timer
import generator

def genFile(amountOfPasswords, lengthOfPasswords, outputFile='output.txt'):
    with open(outputFile, 'w') as output:
        for password in range(amountOfPasswords):
            output.write(str(generator.gen(lengthOfPasswords) + '\n'))

print('------------------------')
print('MASS PASSWORD GENERATOR')
print('------------------------')
length = input('Length of password(s): ')
amount = input('Amount of password(s): ')
fileName = input('Name of file (must put .txt at end): ')

start = timer()

genFile(int(amount), int(length), str(fileName))

end = timer()
print('File Generated!')
print('Time taken to generate: ' + str(round(end - start, 4)))