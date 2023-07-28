print('SETUP FILE CONFIG.PY')
print('======================================')

token = input('Bot Token: ')
userid = int(input('User ID Owner: '))
owner = input('Username Owner: ')
group = input('Username Grup 1: ')
group2 = input('Username Grup 2: ')
channel = input('Username Channel: ')
project = input('Nama Project: ')

teks = 'TOKEN = "{}"\nADMIN = int("{}")\nOWNER = "{}"\nGROUP = "{}"\nGROUP2 = "{}"\nCHANNEL = "{}"\nPROJECT_NAME = "{}"'.format(token,userid,owner,group,group2,channel,project)
file = open('config.py','w')

file.write(teks)
file.close()

print('SETUP BERHASIL! Silahkan Dirun.')
