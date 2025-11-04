# 🛳️ Análise Exploratória de Dados - Titanic

Este projeto realiza uma **Análise Exploratória de Dados (EDA)** do famoso dataset Titanic, utilizando **Python** e bibliotecas de ciência de dados. O objetivo é **coletar, limpar e analisar dados**, extraindo insights iniciais sobre os passageiros e sua sobrevivência.

---

## 🎯 Objetivo do Projeto
- Aprender a manipular dados com **Pandas**.  
- Tratar valores nulos e inconsistências.  
- Gerar estatísticas descritivas.  
- Criar visualizações para entender padrões e tendências.  
- Produzir insights iniciais sobre o dataset Titanic.

---

## 🧰 Bibliotecas Utilizadas

| Biblioteca | Uso no Projeto |
|------------|----------------|
| **Pandas** | Manipulação e análise de dados: leitura do dataset, tratamento de valores nulos, cálculo de estatísticas descritivas. |
| **Seaborn** | Visualização gráfica de dados: criação de gráficos como `countplot` e `histplot` para identificar padrões de sobrevivência e distribuição de idades. |
| **Matplotlib** | Complementa o Seaborn para renderizar gráficos e personalizar visualizações. |
| **Jupyter Notebook** | Ferramenta interativa para explorar dados passo a passo, combinar código, gráficos e texto explicativo. |

---

## 📊 Análises Realizadas
1. **Leitura do dataset Titanic**  
2. **Identificação de valores nulos**  
3. **Tratamento de dados ausentes**:
   - `age` preenchido com a média  
   - `embarked` preenchido com a moda  
   - `deck` removido quando ausente  
4. **Estatísticas descritivas**:
   - Total de passageiros  
   - Taxa de sobrevivência  
   - Média de idade  
   - Distribuição por gênero e classe  
5. **Visualizações**:
   - Sobreviventes por gênero  
   - Distribuição de idades  

---

## 💡 Insights Iniciais
- A taxa de sobrevivência geral foi de aproximadamente **67%**.  
- A **média de idade** dos passageiros é de **35 anos**.  
- A maior parte dos passageiros embarcou em **Southampton (S)**.  
- Mulheres tiveram maior taxa de sobrevivência que homens.  

---

## 🚀 Como Executar o Projeto

1. Clone este repositório:
```bash
git clone https://github.com/josephgabriel/projeto-titanic.git
```
2. Entre na pasta do projeto:
```bash
cd projeto-titanic
```
4. Ative o ambiente virtual:
```bash
source .venv/bin/activate
```
5. Instale as dependências:
```bash
pip install -r requirements.txt
```
6. Execute o notebook:
```bash
jupyter notebook notebooks/eda_titanic.ipynb
```
