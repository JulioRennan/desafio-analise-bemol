#  Analise Bemol

## Descrição
  Foi fornecido uma planilha xlsx, com dados **fictícios**  com a seguinte estrutura:
  
  *A instrução completa do desafio esta em __planilhas/relatorio.xlsx__*
  
### Folha 1
num_compra|	usuario|	nome	|dados|	Filial	|data_compra|	valor_compra	|Imposto	|Informado sobre importo?
------------|-------|-------|------|--------|-----------|---------------|---------|------------------------|
24937847	|295|	Daniel	|12	|Loja Armando Mendes|	2019-01-06 11:53:01	|R$129,12|	R$2,60	|Sim
23600787	|295	|Daniel	|12|	Loja Manoa	|2019-06-01 17:27:11	|R$95,96|	R$1,94	|Sim
23802765	|331|	Alex|	12	|Loja Manoa|	2019-06-11 20:10:43|	R$586,20|	R$11,82	|Sim


### Folha 2

Loja|	data_compra|	inicio	|termino	|Loja_nome	|codloja	|produto	|EAN|	quantidade	|valor_total|	Imposto|
----|------------|----------|----------|----------|---------|---------|---|-------------|------------|---------|
430	|2019-07-05 |10:30:41	|2019-07-05	|2019-07-20	|Mercadinho Daskina|	4,96186E+13	|Açaí 1L|	3,29849E+12|1|	R$ 9,23	|R$ 1,58|
430 |	2019-07-07|13:50:44	2019-07-05	|2019-07-20|	Mercadinho Daskina|4,96186E+13	|Açaí| 1L Zero|7,8949E+12|1|	R$ 5,59|	R$ 0,96|


  
  E a partir dessa informações deveria ser feito um código capaz de capturar pelo menos os seguintes dados:
1. **Questão**
    1. Melhor vendedor por unidade
    1. Venda por vendedor
    
1. **Questão**
    1. Produto mais vendido
    
  
## Libs Necessárias para executar o código:
  1. **Matplotlib:** `pip install matplotlib`
  1. **Unidecode:** `pip install Unidecode`
  1. **Pandas:** `pip install pandas` 
  
  
 ## Descriçao das Classes
 * **ControllerVededor**:
    * **atributos**:
        - **`self.vendedores`**: Dicionário, para armazenas os dados do vendedor como se fosse um JSON.
        
        - **`self.loja`**: Dicionario, para armazenas os dados da Loja como se fosse um JSON.
        
        - **`self.compras`**: Lista com todas as compras registradas na planilha.
        
      
    * **métodos**:
       - **`addVendedor(self,compra)`**: cria um novo nó de vendedor em `self.vendedores`
       
       - **`addLoja(self,compra)`**: cria um novo nó de loja em `self.loja`
       
       - **`melhorVendedor(self,id_v1,id_v2,loja)`**: retorna True se o vendedor do id_v1 vender mais que o do id_v2, retorna False caso contrário
       
       - **`gerarDicionariosVendas(self)`**: contrói os atributos fundamentais do código `self.vendedores`,`self.loja` e `self.compras`, e salva os dados de `self.vendedores` e `self.loja` em um arquivo *.json* na pasta *estrutura_dicionarios*.
       
 * **ControllerProduto**:
 
     * **atributos**:
     
        - **`self.produtos`**: Dicionário, para armazenas os dados do vendedor como se fosse um JSON.

        - **`self.lojas`**: Dicionario, para armazenas os dados da Loja como se fosse um JSON.


        
      
      * **métodos**:
           - **`produtoMaisVendido(self,lojaAndId)`**: retorna o produto mais vendido de uma loja, recebendo como paramentro uma `String` que conrresponde a algum nó cadastrado em `self.loja`
           - **`addProduto(self,compra)`**: cria um novo nó de produto em `self.vendedores`
          
           - **`addLoja(self,linhaProduto)`**: cria um novo nó de loja em `self.loja`

           - **`maisVendido(self,id_p1,id_p2,loja)`**: retorna True se o produto do id_p2 foi mais vendido que o produto do id_v2, retorna False caso contrário

           - **`gerarDicionarioLoja(self)`**: contrói os atributos fundamentais do código `self.produtos`,`self.loja` e `self.lojas`, e salva os dados deles em um arquivo *.json* na pasta *estrutura_dicionarios/*.
  
 
 

 
