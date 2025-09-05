from math import pow, sqrt
from time import sleep
import re

valores = {}
rds = 0

def leiaInt(msg: str):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m[ERRO] Digite um número inteiro válido.\033[m ')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário optou em não digitar nada.\033[m')
        else:
            return n


def leiaFloat(msg: str):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31m [ERRO] Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário optou em não digitar o número real\033[m.')
            return 0
        else:
            return n
        

def leiaResistor(msg: str):

    r = str(input(msg)).strip().replace(",", ".")

    if r.isalpha():
        print("So letra")

    if isnumber(r):
        print("Só numero")
        return float(r)
    
    if r.isalnum:
        if "k" in r or "K" in r or "M" in r:
    
            for multi in r:
                if "k" == r or "K" == r or "M" == r:
                    r.replace(f"{multi}", "")
                    return leiaMultiplicador(multi)

        

def leiaMultiplicador(indice: str):
    
    while indice != "k" or indice != "K" or indice != "M": return 1

    if indice == "k" or indice == "K": return 1000

    elif indice == "M": return 1000000


def isnumber(s: str):
    
    s.strip()

    try:
        float(s)
        return True
    except ValueError:
        return False


polarizacao = str(input('Qual a sua polarização (AP ou DTG): ')).lower().strip() 

while polarizacao != 'ap' and polarizacao != 'dtg':
    polarizacao = str(input('Digite novamente a sua polarização: '))

if polarizacao == 'dtg':
    vgsoff = leiaFloat('Vgsoff: ')
    idss = leiaFloat('Idss em mA: ') * 0.001

    vf = leiaInt('valor da fonte: ')
    rs = leiaResistor('Rs: ')
    rd = leiaResistor('Rd: ')
    rg1 = leiaResistor('Rg1: ')
    rg2 = leiaResistor('Rg2: ')
    if vgsoff < 0:
        rds = (-1 * vgsoff)/idss
    else:
        rds = vgsoff/idss

    print('PROCESSANDO INFORMAÇÕES...')
    sleep(1)

    vgg = rg2 * (vf/(rg1 + rg2))
    termo1 = -1 * (vgg/vgsoff) + 1
    termo2 = -1 * (-rs/vgsoff) 

    print(f'\n\nId = {idss/0.001}x10⁻³({termo1} + {termo2}Id)²')

    a = (pow(termo2, 2)) * idss
    b = (((termo2 * termo1) * 2) * idss) - 1
    c = (pow(termo1, 2)) * idss

    print(f'Id = {a}Id² {b}Id + {c}')

    delta = b**2 - (4 * a * c)
    print(f'\n∆ = {delta}')

    print(f'0 = ({b * -1} ± {sqrt(delta)})/{2 * a}')

    print(f'\nx´ = {(b * -1 + sqrt(delta))/(2 * a)} A')
    print(f'x´´ = {(b * -1 - sqrt(delta))/(2 * a)} A \n')

    id = (b * -1 - sqrt(delta))/(2 * a)
    vds = vf - id * (rd + rs)
    vrds = id * rds
    
    if vds < vrds:
        
        idohm = vf / (rds + rd + rs)

        valores['Id'] = idohm
        valores['VRd'] = idohm * rd
        valores['VRs'] = idohm * rs
        valores['VDS'] = idohm * rds
        valores['VGS'] = vgg - idohm * rs
        valores['Pd'] = idohm * idohm * rds
        
        print('=' * 25)
        print('Região de Operação: Ôhmica')
        for i, v in valores.items():
            if i == 'Id':
                print(f'{i} = {v/0.001:.4f} mA')
            elif i == 'Pd':
                print(f'{i} = {v/0.001:.4f} mW')
            else:
                print(f'{i} = {v:.4f} V')
        print('=' * 25)

        print('Obrigado por usar o nosso programa. \nFINALIZANDO...\n\n')
        sleep(1)
    
    else:
        valores['Id'] = id
        valores['VRd'] = id * rd
        valores['VRs'] = id * rs
        valores['VDS'] = vds
        valores['VGS'] = vgg - id * rs
        valores['Pd'] = id * vds

        print('=' * 25)
        print('Região de Operação: Saturação')
        for i, v in valores.items():
            if i == 'Id':
                print(f'{i} = {v/0.001:.4f} mA')
            elif i == 'Pd':
                print(f'{i} = {v/0.001:.4f} mW')
            else:
                print(f'{i} = {v:.4f} V')
        print('=' * 25)

        print('Obrigado por usar o nosso programa. \nFINALIZANDO...\n\n')
        sleep(1)

elif polarizacao == 'ap':
    vgsoff = leiaFloat('Vgsoff: ')
    idss = leiaFloat('Idss: ') * 0.001
    vf = leiaFloat('Valor da fonte: ')
    rd = leiaInt('Rd: ')
    rs = leiaInt('Rs: ')
    if vgsoff < 0:
        rds = (-1 * vgsoff)/idss
    else:
        rds = vgsoff/idss

    print('PROCESSANDO INFORMAÇÕES...')
    sleep(1)

    termo1 = 1
    termo2 = ((-1 * rs) / vgsoff) * - 1

    print(f'\nId = {idss/0.001}x10⁻³({termo1} {termo2}Id)²')

    a = (termo2**2) * idss
    b = (termo2 * 2) * idss - 1
    c = 1 * idss

    print(f'\nAssim fica a sua fórmula de Bháskara: \n0 = {a}Id² {b}Id + {c}\n')

    delta = b**2 - (4 * a * c)
    print(f'0 = ({-1 * b} ± {sqrt(delta)})/{2 * a}\n')
    print(f'x´ = {((-1*b) + (sqrt(delta)))/ (2 * a) }')
    print(f'x´´ = {((-1*b) - (sqrt(delta)))/ (2 * a)}\n\n')

    id = ((-1*b) - (sqrt(delta)))/ (2 * a)
    vds = vf - id * (rd + rs)
    vrds = id * rds

    if vds < vrds:

        idohm = vf/(rds + rd + rs)
        
        valores['Id'] = idohm
        valores['VRd'] = idohm * rd
        valores['VRs' ] = idohm * rs
        valores['VDS'] = idohm * rds
        valores['VGS'] = -idohm * rs
        valores['Pd'] = idohm * idohm * rds

        print('=' * 25)
        print('Região de Operação: Ôhmica')
        for i, v in valores.items():
            if i == 'Id':
                print(f'{i} = {v/0.001:.4f} mA')
            elif i == 'Pd':
                print(f'{i} = {v/0.001:.4f} mW')
            else:
                print(f'{i} = {v:.4f} V')
        print('=' * 25)

        print('Obrigado por usar o nosso programa. \nFINALIZANDO...\n\n')
        sleep(1)

    else:
        valores['Id'] = id
        valores['VRd'] = id * rd
        valores['VRs'] = id * rs
        valores['VDS'] = vds
        valores['VGS'] = -id * rs
        valores['Pd'] = id * vds

        print('=' * 25)
        print('Região de Operação: Saturação')
        for i, v in valores.items():
            if i == 'Id':
                print(f'{i} = {v/0.001:.4f} mA')
            elif i == 'Pd':
                print(f'{i} = {v/0.001:.4f} mW')
            else:
                print(f'{i} = {v:.4f} V')
        print('=' * 25)

        
    