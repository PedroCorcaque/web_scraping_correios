from lib.webScraping import sendCEPToFindAddress

def checkCEPNumber(cep: str):
    if '-' in cep:
        cep = cep.replace('-', '')
    if '.' in cep:
        cep = cep.replace('.', '')
    
    if len(cep) != 8:
        raise Exception("CEP inválido.")
    else:
        return cep

def getInputData():
    try:
        cep = input('Digite seu CEP: ')
        return checkCEPNumber(cep)
    except Exception as e:
        print(f'[ERRO] - {str(e)}\nTente novamente...')

if __name__ == '__main__':
    print('Informe o CEP a ser buscado')
    cep_checked = getInputData()
    try:
        address = sendCEPToFindAddress(cep=cep_checked)
        print(f'O endereço do CEP: {cep_checked[:5]}-{cep_checked[5:]} é: {address[0]}, {address[1]} - {address[2]}')
    except Exception as e:
        print('Não foi possível encontrar o endereço do CEP passado.')


    
