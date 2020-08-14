import pandas as pd
import operator
import json
class Compra:
    def __init__(self,numero_compra,usuario,nome,dados,filial,data,valor,imposto,info_imposto):
        self.numero = str(numero_compra)
        self.usuario = str(usuario)
        self.nome   = str(nome)
        self.dados  = str(dados)
        self.filial = str(filial)
        self.data   = str(data)
        self.valor  =round(float(valor),2)
        self.imposto=  round(float(imposto),2)
        self.info_imposto = str(info_imposto)
    def toString(self):
        return  self.numero+"\t"+self.usario +"\t"+self.nome +"\t"+self.dados+"\t"+self.filial+"\t"+"\t"+self.data +"\t"+str(self.valor) +"\t"+str(self.info_imposto)
class ControllerVededor:
    def __init__(self):
        self.excel = pd.ExcelFile('planilhas/relatorio.xlsx')
        self.sheet_vendas = pd.read_excel(self.excel,1)
        self.vendedores={}
        self.loja = {}

        self.list_compras = []
        self.gerarDicionariosVendas()
    def addVendedor(self, compra):
        infoVenda = {
            'filial': compra.filial,
            'data_compra': compra.data,
            'valor_compra': compra.valor
        }
        if (self.vendedores.get(compra.usuario, False)):
            self.vendedores[compra.usuario]['totalVenda'] += compra.valor
            self.vendedores[compra.usuario]['infoVenda'].append(infoVenda)
            if(self.vendedores[compra.usuario]['lojas'].get(compra.filial,False)):
                self.vendedores[compra.usuario]['lojas'][compra.filial]+=compra.valor
            else:
                self.vendedores[compra.usuario]['lojas'][compra.filial] = compra.valor
        else:
            self.vendedores[compra.usuario] = {
                'totalVenda': compra.valor,
                'nome': compra.nome,
                'infoVenda': [infoVenda],
                'lojas':{
                    compra.filial:compra.valor
                }
            }


    def addLoja(self,compra):
        if(self.loja.get(compra.filial,False)):
            self.loja[compra.filial]['total']+=compra.valor
            if(compra.usuario not in self.loja[compra.filial]['vendedores']):
                self.loja[compra.filial]['vendedores'].append(compra.usuario)
                melhorAtual =  self.loja[compra.filial]['melhor_vendedor']
                self.loja[compra.filial]['melhor_vendedor'] =compra.usuario if self.melhorVendedor(compra.usuario, melhorAtual,compra.filial) else melhorAtual
        else:
            self.loja[compra.filial]={
                'total':compra.valor,
                'vendedores':[compra.usuario],
                'melhor_vendedor':compra.usuario
            }

    def melhorVendedor(self,v1,v2,loja):

        if self.vendedores[v1]['lojas'][loja]>self.vendedores[v2]['lojas'][loja]:
            return True
        return False
    def gerarDicionariosVendas(self):
        v = pd.read_excel(self.excel,1)
        for i in range(len(v['num_compra'].values)):
            self.list_compras.append(Compra(v['num_compra'].values[i],v['usuario'].values[i],v['nome'].values[i],v['dados'].values[i],v['Filial'].values[i],v['data_compra'].values[i],v['valor_compra'].values[i],v['Imposto'].values[i],v['Informado sobre importo?'].values[i]))
        for compra in self.list_compras:
            self.addVendedor(compra)
        for compra in self.list_compras:
            self.addLoja(compra)
        open('estrutura_dicionarios/estruturaQ1_loja.json','w').write(json.dumps(self.loja))
        open('estrutura_dicionarios/estruturaQ1_vendedores.json','w').write(json.dumps(self.vendedores))