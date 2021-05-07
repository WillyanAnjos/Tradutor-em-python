#python3 -m pip install translate

#Importar lib
from translate import Translator


#Configurar tradução para inglês
portugues_para_ingles = Translator(from_lang="portuguese", to_lang="en")

#Configurar tradução para portuguêS
ingles_para_portugues = Translator(from_lang="english", to_lang="pt-br")


#Entrada do texto
texto_original = input('Insira o texto para tradução: ')

#Entrada da opção de tradução
opcao = int(input('Traduzir para InglêS [1] ou para portuguêS [2]: '))


#Verifica qual foi a opção selecionada
if opcao == 1:
    texto = portugues_para_ingles.translate(texto_original)
elif opcao == 2:
    texto = ingles_para_portugues.translate(texto_original)
else:
    print('Informe 1 ou 2')


#Resultado
print(texto)


