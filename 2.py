import pyAesCrypt

password = input('Введите пароль для шифрования файла: ')

# шифруем файл

# encrypt
# pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

# дешифруем файл

# decrypt
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)

