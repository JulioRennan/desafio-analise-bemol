import pandas as pd

import json


class LinhaProduto:
    def getCel(self,key):
        return str(self.dfLinha[key].values[0])



    def __init__(self,dfLinha):
        self.dfLinha = dfLinha
        self.loja =  self.getCel('Loja_nome')+"#"+self.getCel('Loja')

        self.dataCompra = self.getCel('data_compra')
        self.inicio = self.getCel('inicio')
        self.fim = self.getCel('termino')
        self.codLoja = self.getCel('codloja')
        self.produto=self.getCel('produto')
        self.EAN = self.getCel('EAN')
        self.quantidade = float(self.getCel('quantidade'))
        self.valor_total = round(float(self.getCel('valor_total')),3)
        self.imposto = round(float(self.getCel('Imposto')))

    def toList(self):
        return list(self.__dict__.values())[1::]

class ControllerProduto:
    def __init__(self):
        self.excel = pd.ExcelFile('planilhas/relatorio.xlsx')
        self.sheet_produtos = pd.read_excel(self.excel,2)
        self.lojas = {}
        self.produtos ={}
        self.gerarDicionarioLoja()


    def gerarDicionarioLoja(self):
        qtdLinhas = self.sheet_produtos.shape[0]
        for i in range(qtdLinhas):
            linhaProduto = LinhaProduto(self.sheet_produtos.loc[[i]])
            self.addProduto(linhaProduto)
        for id_produto in self.produtos:
            self.addLoja(id_produto)

        open('estrutura_dicionarios/estrutura_JSON_produto.txt', 'w').write(json.dumps(self.produtos))
        open('estrutura_dicionarios/estrutura_JSON_loja_produto.txt', 'w').write(json.dumps(self.lojas))
    def addLoja(self,id_produto):
        for loja in self.produtos[id_produto]['lojas']:
            if(self.lojas.get(loja,False)):
                self.lojas[loja]['produtos'].append(id_produto)
                maisVendidoAtual = self.lojas[loja]['mais_vendido']
                if(self.maisVendido(maisVendidoAtual,id_produto,loja)):
                    self.lojas[loja]['mais_vendido'] = id_produto
            else:
                self.lojas[loja] = {
                    'produtos':[id_produto],
                    'mais_vendido':id_produto
                }
    def maisVendido(self,id_p1,id_p2,loja):
        valor_p1 = self.produtos[id_p1]['lojas'][loja]
        valor_p2 =  self.produtos[id_p2]['lojas'][loja]
        if(valor_p1<valor_p2):
            return True
        return False

    def addProduto(self,linhaProduto):
        if(self.produtos.get(linhaProduto.EAN,False)):
            self.produtos[linhaProduto.EAN]['quantidade']+=linhaProduto.quantidade
            self.produtos[linhaProduto.EAN]['valor_total']+=linhaProduto.valor_total

            if self.produtos[linhaProduto.EAN]['lojas'].get(linhaProduto.loja,False):
                self.produtos[linhaProduto.EAN]['lojas'][linhaProduto.loja]+=linhaProduto.valor_total
            else:
                self.produtos[linhaProduto.EAN]['lojas'][linhaProduto.loja] = linhaProduto.valor_total
        else:
            self.produtos[linhaProduto.EAN] ={
                'nome_produto':linhaProduto.produto,
                'cod_loja':linhaProduto.codLoja,
                'quantidade':linhaProduto.quantidade,
                'valor_total':linhaProduto.valor_total,
                'lojas':{linhaProduto.loja:linhaProduto.valor_total}
            }




controller = ControllerProduto()
