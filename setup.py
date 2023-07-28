print('SETUP FILE CONFIG.PY')
print('======================================')

token = raw_input('Bot Token: ')
userid = input('User ID Owner: ')
owner = raw_input('Username Owner: ')
group = raw_input('Username Grup 1: ')
group2 = raw_input('Username Grup 2: ')
channel = raw_input('Username Channel: ')
project = raw_input('Nama Project: ')

teks = 'TOKEN = "{}"\nADMIN = int("{}")\nOWNER = "{}"\nGROUP = "{}"\nGROUP2 = "{}"\nCHANNEL = "{}"\nPROJECT_NAME = "{}"'.format(token,userid,owner,group,group2,channel,project)
file = open('config.py','w')

file.write(teks)
file.close()

print('SETUP BERHASIL! Silahkan Dirun.')
