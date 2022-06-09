import xmltodict
import pandas as pd

with open('nfe.xml') as fd:
    doc = xmltodict.parse(fd.read())
    itens = []
    for info in doc['nfeProc']['NFe']['infNFe']['det']:
        item = {}
        item['nfe'] = doc['nfeProc']['NFe']['infNFe']['ide']['nNF']
        item['dhEmi'] = doc['nfeProc']['NFe']['infNFe']['ide']['dhEmi']
        item['cEAN'] = info['prod']['cEAN']
        item['cProd'] = info['prod']['cProd']
        item['xProd'] = info['prod']['xProd']
        item['uCom'] = info['prod']['uCom']
        item['qCom'] = info['prod']['qCom']
        item['vUnCom'] = info['prod']['vUnCom']
        itens.append(item)
    print(itens)
    df = pd.DataFrame(itens)
    df.to_csv('nfe.csv', index=False, sep=';')