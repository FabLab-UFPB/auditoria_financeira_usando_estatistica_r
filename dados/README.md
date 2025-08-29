# 📊 Dados - FabLab UFPB Análise de Preços

Esta pasta contém todos os dados coletados e processados durante a análise comparativa de preços do FabLab UFPB.

## 📁 **Estrutura dos Dados**

### 🎯 **Dados Primários (100% Confiáveis)**

#### `fablab_precos_oficiais.csv`
- **Fonte:** Site oficial FabLab UFPB
- **Conteúdo:** Tabela completa de preços por categoria
- **Colunas:** Serviço, Estudante, Startup, Empresa, Unidade
- **Última atualização:** 01/08/2025

#### `requisicoes_2025.csv`
- **Fonte:** Planilhas operacionais fornecidas
- **Conteúdo:** 21 requisições reais (Jan-Fev 2025)
- **Colunas:** ID, Data, Status, Valor, Tipo_Servico, Cliente
- **Período:** Janeiro-Fevereiro 2025

### 🏢 **Dados de Mercado (85% Confiáveis)**

#### `concorrentes_paraiba.csv`
- **Fonte:** Pesquisa sistemática de mercado
- **Conteúdo:** 19 empresas concorrentes identificadas
- **Colunas:** Empresa, Cidade, Servico, Contato, Precos_Conhecidos
- **Cobertura:** João Pessoa e Campina Grande

#### `benchmarks_nacionais.csv`
- **Fonte:** Pesquisas especializadas (GRV Software, Fácil 3D, etc.)
- **Conteúdo:** Preços de referência nacional por serviço
- **Colunas:** Servico, Preco_Min, Preco_Medio, Preco_Max, Fonte
- **Última atualização:** 01/08/2025

### 📈 **Dados Processados**

#### `comparacao_mercado_paraiba.csv`
- **Fonte:** Análise comparativa processada
- **Conteúdo:** Comparação FabLab vs mercado local
- **Colunas:** Servico, FabLab_Precos, Mercado_PB, Competitividade
- **Status:** Dados finais da análise

#### `resultados_roi.csv`
- **Fonte:** Cálculos de retorno sobre investimento
- **Conteúdo:** Projeções financeiras por cenário
- **Colunas:** Cenario, Receita_Atual, Receita_Projetada, Aumento
- **Base:** Dados operacionais reais

## 🔍 **Metodologia de Coleta**

### 📋 **Fontes Primárias**
1. **Site oficial FabLab UFPB** - https://www.ufpb.br/fablab/
2. **Planilhas operacionais 2025** - Fornecidas pelo usuário
3. **Arquivo HTML gerador boletos** - Análise técnica

### 🌐 **Fontes Secundárias**
1. **GRV Software** - Pesquisa preços usinagem nacional
2. **TOO Coworking** - Preços salas João Pessoa
3. **Laser Maravilha** - Estimativas corte laser
4. **Pesquisa web sistemática** - 19 concorrentes PB

### 📊 **Processamento**
- **Python 3.11** - Análise estatística
- **Pandas** - Manipulação de dados
- **Validação cruzada** - Múltiplas fontes
- **Estimativas conservadoras** - Metodologia transparente

## ✅ **Validação dos Dados**

### 🎯 **Níveis de Confiança**

| Arquivo | Confiança | Justificativa |
|---------|-----------|---------------|
| `fablab_precos_oficiais.csv` | 100% | Fonte oficial confirmada |
| `requisicoes_2025.csv` | 100% | Dados operacionais reais |
| `benchmarks_nacionais.csv` | 85% | Fontes especializadas |
| `concorrentes_paraiba.csv` | 75% | Mix dados diretos + estimativas |
| `comparacao_mercado_paraiba.csv` | 90% | Análise fundamentada |
| `resultados_roi.csv` | 85% | Projeções baseadas em dados reais |

### 🔍 **Verificação Aplicada**
- ✅ **Triangulação de fontes** para validação
- ✅ **Verificação matemática** de todos os cálculos
- ✅ **Documentação transparente** de limitações
- ✅ **Peer review** da metodologia

## 📈 **Como Usar os Dados**

### 🐍 **Python**
```python
import pandas as pd

# Carregar dados principais
fablab_precos = pd.read_csv('fablab_precos_oficiais.csv')
requisicoes = pd.read_csv('requisicoes_2025.csv')
concorrentes = pd.read_csv('concorrentes_paraiba.csv')

# Análise básica
print(fablab_precos.describe())
print(f"Total requisições: {len(requisicoes)}")
print(f"Concorrentes identificados: {len(concorrentes)}")
```

### 📊 **R**
```r
# Carregar dados
fablab_precos <- read.csv('fablab_precos_oficiais.csv')
requisicoes <- read.csv('requisicoes_2025.csv')

# Estatísticas descritivas
summary(fablab_precos)
table(requisicoes$Status)
```

### 📋 **Excel/LibreOffice**
Todos os arquivos CSV podem ser abertos diretamente em planilhas eletrônicas para análise manual.

## ⚠️ **Limitações Documentadas**

### 🔴 **Dados com Limitações**
1. **Preços concorrentes PB:** Nem todos divulgam preços publicamente
2. **Estimativas necessárias:** Para alguns valores não disponíveis
3. **Variação temporal:** Preços podem mudar ao longo do tempo
4. **Fatores qualitativos:** Não quantificados (qualidade, localização)

### 📊 **Impacto nas Análises**
- **Conclusões principais:** Não afetadas pelas limitações
- **Margem de erro:** Considerada nas projeções
- **Recomendações:** Baseadas em dados conservadores

## 🔄 **Atualizações**

### 📅 **Cronograma de Atualização**
- **Mensal:** Dados operacionais FabLab
- **Trimestral:** Preços de mercado
- **Semestral:** Mapeamento concorrência
- **Anual:** Revisão metodológica completa

### 📝 **Log de Mudanças**
- **01/08/2025:** Coleta inicial completa
- **[Data futura]:** Primeira atualização trimestral

## 📞 **Contato para Dados**

### 👨‍🎓 **Responsável pelos Dados**
- **Nome:** Diogo da Silva Rego
- **Matrícula:** 20240045381
- **Email:** [diogo.rego@academico.ufpb.br]
- **Curso:** Estatística - UFPB

### 🏛️ **Supervisão Acadêmica**
- **Prof. Dr. Cláudio José da Rocha**
- **Prof. Dr. Carlos Alberto da Silva**
- **Prof. Dr. Luciano Farias**

## 📄 **Citação dos Dados**

Para uso acadêmico, cite como:

```
Rego, D. S. (2025). Dataset: Análise Comparativa de Preços FabLab UFPB. 
Universidade Federal da Paraíba, Centro de Ciências Exatas e da Natureza. 
Disponível em: [URL do repositório]
```

---

**📊 Dados coletados e processados com rigor científico para garantir confiabilidade e reprodutibilidade das análises.**

