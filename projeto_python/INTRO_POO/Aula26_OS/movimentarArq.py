import os
import shutil

caminho_antigo = ''
caminho_novo = ''

try:
    os.mkdir(caminho_novo)  #cria o caminho novo
except FileExistsError as e:
    pass

for root, dirs, files in os.walk(caminho_antigo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        #move arquivos
        shutil.move(old_file_path, new_file_path)
        print('movido com sucesso')



for root, dirs, files in os.walk(caminho_antigo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        #copia arquivo com extensão .str
        if '.str' in file:
            shutil.copy(old_file_path, new_file_path)
            print('copiado com sucesso')




for root, dirs, files in os.walk(caminho_antigo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        # apaga arquivo com extensão .str
        if '.str' in file:
            os.remove(caminho_antigo)
            print('removido com sucesso')