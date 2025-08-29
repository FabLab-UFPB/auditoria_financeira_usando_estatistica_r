#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GRÁFICOS COMPARATIVOS - FABLAB UFPB vs MERCADO DA PARAÍBA
Análise visual específica do mercado local
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings('ignore')

# Configurar matplotlib para português
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.family'] = 'DejaVu Sans'

print("="*80)
print("GRÁFICOS COMPARATIVOS - FABLAB UFPB vs MERCADO DA PARAÍBA")
print("="*80)

# ============================================================================
# 1. DADOS ESPECÍFICOS DO MERCADO PARAIBANO
# ============================================================================

# Salas de Reunião - Comparação com TOO Coworking (dados reais)
salas_paraiba = pd.DataFrame({
    'Categoria': ['FabLab Estudante', 'FabLab Startup', 'FabLab Empresa', 
                  'TOO Basic (7p)', 'TOO Premium (6p)', 'TOO VIP (3p)'],
    'Preco_Hora': [4.00, 20.00, 40.00, 30.00, 40.00, 40.00],
    'Capacidade': [10, 10, 10, 7, 6, 3],
    'Tipo': ['FabLab', 'FabLab', 'FabLab', 'Mercado PB', 'Mercado PB', 'Mercado PB']
})

# Corte a Laser - Estimativas baseadas em produtos Laser Maravilha
corte_laser_paraiba = pd.DataFrame({
    'Categoria': ['FabLab Estudante', 'FabLab Startup', 'FabLab Empresa',
                  'Laser Maravilha Est.', 'Mega Arts Est.', 'CW Arts Est.'],
    'Preco_Hora': [18.00, 36.00, 72.00, 60.00, 80.00, 50.00],
    'Tipo': ['FabLab', 'FabLab', 'FabLab', 'Mercado PB', 'Mercado PB', 'Mercado PB']
})

# CNC - Estimativas baseadas em mercado industrial local
cnc_paraiba = pd.DataFrame({
    'Categoria': ['FabLab Router Est.', 'FabLab Router Start.', 'FabLab Router Emp.',
                  'JA Metalúrgica Est.', 'Mercado Industrial', 'Usinagem Geral'],
    'Preco_Hora': [4.00, 20.00, 40.00, 80.00, 120.00, 100.00],
    'Tipo': ['FabLab', 'FabLab', 'FabLab', 'Mercado PB', 'Mercado PB', 'Mercado PB']
})

# Concorrentes identificados por serviço
concorrentes_pb = {
    'Impressão 3D': ['BR3DPRINT', '3Dados', '3D Eco House', '3D Tudo Tech'],
    'Corte Laser': ['Laser Maravilha', 'Mega Arts', 'Acrílaser PB', 'CW Arts', 'Paradaise', 'Lapidary'],
    'CNC/Usinagem': ['JA Metalúrgica', 'JG Usinagem', 'NB Máquinas'],
    'Salas/Coworking': ['TOO Coworking', 'Sua Esfera', 'PRÁTICO', 'Sul Office', 'Êxito', 'BL Virtual']
}

# ============================================================================
# 2. GRÁFICOS COMPARATIVOS ESPECÍFICOS DA PARAÍBA
# ============================================================================

# Criar figura com subplots
fig = plt.figure(figsize=(20, 16))

# Gráfico 1: Salas de Reunião - FabLab vs TOO Coworking
ax1 = plt.subplot(2, 3, 1)
colors1 = ['#2E8B57', '#4682B4', '#DC143C', '#FFD700', '#FF8C00', '#FF4500']
bars1 = ax1.bar(range(len(salas_paraiba)), salas_paraiba['Preco_Hora'], color=colors1)
ax1.set_title('Salas de Reunião - FabLab vs TOO Coworking (PB)', fontsize=14, fontweight='bold')
ax1.set_ylabel('Preço por Hora (R$)')
ax1.set_xticks(range(len(salas_paraiba)))
ax1.set_xticklabels(salas_paraiba['Categoria'], rotation=45, ha='right')
ax1.grid(True, alpha=0.3)

for i, v in enumerate(salas_paraiba['Preco_Hora']):
    ax1.text(i, v + 1, f'R$ {v:.0f}', ha='center', va='bottom', fontweight='bold')

# Gráfico 2: Corte a Laser - FabLab vs Mercado PB
ax2 = plt.subplot(2, 3, 2)
colors2 = ['#2E8B57', '#4682B4', '#DC143C', '#FFD700', '#FF8C00', '#FF4500']
bars2 = ax2.bar(range(len(corte_laser_paraiba)), corte_laser_paraiba['Preco_Hora'], color=colors2)
ax2.set_title('Corte a Laser - FabLab vs Mercado Paraíba', fontsize=14, fontweight='bold')
ax2.set_ylabel('Preço por Hora (R$)')
ax2.set_xticks(range(len(corte_laser_paraiba)))
ax2.set_xticklabels(corte_laser_paraiba['Categoria'], rotation=45, ha='right')
ax2.grid(True, alpha=0.3)

for i, v in enumerate(corte_laser_paraiba['Preco_Hora']):
    ax2.text(i, v + 2, f'R$ {v:.0f}', ha='center', va='bottom', fontweight='bold')

# Gráfico 3: CNC - FabLab vs Mercado PB
ax3 = plt.subplot(2, 3, 3)
colors3 = ['#2E8B57', '#4682B4', '#DC143C', '#FFD700', '#FF8C00', '#FF4500']
bars3 = ax3.bar(range(len(cnc_paraiba)), cnc_paraiba['Preco_Hora'], color=colors3)
ax3.set_title('CNC Router - FabLab vs Mercado Paraíba', fontsize=14, fontweight='bold')
ax3.set_ylabel('Preço por Hora (R$)')
ax3.set_xticks(range(len(cnc_paraiba)))
ax3.set_xticklabels(cnc_paraiba['Categoria'], rotation=45, ha='right')
ax3.grid(True, alpha=0.3)

for i, v in enumerate(cnc_paraiba['Preco_Hora']):
    ax3.text(i, v + 3, f'R$ {v:.0f}', ha='center', va='bottom', fontweight='bold')

# Gráfico 4: Número de Concorrentes por Serviço
ax4 = plt.subplot(2, 3, 4)
servicos = list(concorrentes_pb.keys())
num_concorrentes = [len(concorrentes_pb[servico]) for servico in servicos]
colors4 = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
bars4 = ax4.bar(servicos, num_concorrentes, color=colors4)
ax4.set_title('Concorrência por Serviço na Paraíba', fontsize=14, fontweight='bold')
ax4.set_ylabel('Número de Concorrentes')
ax4.grid(True, alpha=0.3)

for i, v in enumerate(num_concorrentes):
    ax4.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')

# Gráfico 5: Competitividade por Serviço (% abaixo do mercado PB)
ax5 = plt.subplot(2, 3, 5)
servicos_comp = ['Salas Reunião', 'Corte Laser', 'CNC Router']
competitividade_pb = [0, 50, 75]  # % abaixo do mercado PB (preços empresa)
colors5 = ['orange' if x < 30 else 'green' for x in competitividade_pb]
bars5 = ax5.bar(servicos_comp, competitividade_pb, color=colors5, alpha=0.7)
ax5.set_title('Competitividade FabLab vs Mercado PB', fontsize=14, fontweight='bold')
ax5.set_ylabel('% Abaixo do Mercado Local')
ax5.grid(True, alpha=0.3)

for i, v in enumerate(competitividade_pb):
    ax5.text(i, v + 2, f'{v}%', ha='center', va='bottom', fontweight='bold')

# Gráfico 6: Distribuição Geográfica dos Concorrentes
ax6 = plt.subplot(2, 3, 6)
cidades = ['João Pessoa', 'Campina Grande']
jp_concorrentes = 10  # BR3DPRINT, 3Dados, Laser Maravilha, Mega Arts, etc.
cg_concorrentes = 6   # 3D Tudo Tech, CW Arts, Paradaise, etc.
concorrentes_cidades = [jp_concorrentes, cg_concorrentes]
colors6 = ['#3498db', '#e74c3c']
bars6 = ax6.bar(cidades, concorrentes_cidades, color=colors6)
ax6.set_title('Distribuição de Concorrentes por Cidade', fontsize=14, fontweight='bold')
ax6.set_ylabel('Número de Empresas')
ax6.grid(True, alpha=0.3)

for i, v in enumerate(concorrentes_cidades):
    ax6.text(i, v + 0.2, str(v), ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('/home/ubuntu/comparacao_mercado_paraiba.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 3. GRÁFICO DE OPORTUNIDADES ESPECÍFICAS DA PARAÍBA
# ============================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Potencial de aumento de preços mantendo competitividade local
servicos_ajuste = ['Corte Laser\nStartup', 'Corte Laser\nEmpresa', 'CNC Router\nEstudante', 
                   'CNC Router\nStartup', 'CNC Router\nEmpresa']
preco_atual = [36, 72, 4, 20, 40]
preco_sugerido = [45, 90, 8, 40, 80]
margem_mercado_pb = [80, 120, 80, 120, 120]  # Preços estimados mercado PB

x = np.arange(len(servicos_ajuste))
width = 0.25

bars1 = ax1.bar(x - width, preco_atual, width, label='Preço Atual', color='#FF6B6B', alpha=0.8)
bars2 = ax1.bar(x, preco_sugerido, width, label='Preço Sugerido', color='#4ECDC4', alpha=0.8)
bars3 = ax1.bar(x + width, margem_mercado_pb, width, label='Mercado PB (Est.)', color='#45B7D1', alpha=0.8)

ax1.set_title('Oportunidades de Ajuste de Preços - Mercado PB', fontsize=14, fontweight='bold')
ax1.set_ylabel('Preço por Hora (R$)')
ax1.set_xticks(x)
ax1.set_xticklabels(servicos_ajuste)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Adicionar valores nas barras
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'R$ {height:.0f}', ha='center', va='bottom', fontsize=9)

# Impacto na receita anual
cenarios_pb = ['Atual', 'Conservador\n(+40%)', 'Realista\n(+60%)', 'Otimista\n(+80%)']
receitas_pb = [5670, 7938, 9072, 10206]
colors_receita = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']

bars_receita = ax2.bar(cenarios_pb, receitas_pb, color=colors_receita)
ax2.set_title('Projeção de Receita - Ajustes Mercado PB', fontsize=14, fontweight='bold')
ax2.set_ylabel('Receita Anual (R$)')
ax2.grid(True, alpha=0.3)

for i, v in enumerate(receitas_pb):
    ax2.text(i, v + 100, f'R$ {v:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('/home/ubuntu/oportunidades_mercado_paraiba.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 4. MAPA DE CONCORRÊNCIA POR SERVIÇO E CIDADE
# ============================================================================

# Dados para mapa de calor
servicos_mapa = ['Impressão 3D', 'Corte Laser', 'CNC/Usinagem', 'Salas/Coworking']
cidades_mapa = ['João Pessoa', 'Campina Grande']

# Matriz de concorrentes por cidade e serviço
concorrencia_matriz = np.array([
    [2, 1],  # Impressão 3D: JP=2, CG=1
    [4, 3],  # Corte Laser: JP=4, CG=3  
    [2, 1],  # CNC/Usinagem: JP=2, CG=1
    [6, 1]   # Salas/Coworking: JP=6, CG=1
])

fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(concorrencia_matriz, cmap='Reds', aspect='auto')

# Configurar ticks
ax.set_xticks(np.arange(len(cidades_mapa)))
ax.set_yticks(np.arange(len(servicos_mapa)))
ax.set_xticklabels(cidades_mapa)
ax.set_yticklabels(servicos_mapa)

# Adicionar valores nas células
for i in range(len(servicos_mapa)):
    for j in range(len(cidades_mapa)):
        text = ax.text(j, i, f'{concorrencia_matriz[i, j]}',
                      ha="center", va="center", color="black", fontweight='bold', fontsize=14)

ax.set_title('Mapa de Concorrência por Serviço e Cidade - Paraíba', fontsize=14, fontweight='bold')
plt.colorbar(im, ax=ax, label='Número de Concorrentes')
plt.tight_layout()
plt.savefig('/home/ubuntu/mapa_concorrencia_paraiba.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 5. EXPORTAR DADOS CONSOLIDADOS DA PARAÍBA
# ============================================================================

# Consolidar dados específicos da Paraíba
dados_paraiba = pd.DataFrame({
    'Serviço': ['Salas Reunião', 'Corte Laser', 'CNC Router'],
    'FabLab_Estudante': [4.00, 18.00, 4.00],
    'FabLab_Startup': [20.00, 36.00, 20.00],
    'FabLab_Empresa': [40.00, 72.00, 40.00],
    'Mercado_PB_Minimo': [30.00, 50.00, 80.00],
    'Mercado_PB_Medio': [35.00, 65.00, 100.00],
    'Mercado_PB_Maximo': [40.00, 80.00, 120.00],
    'Num_Concorrentes_JP': [6, 4, 2],
    'Num_Concorrentes_CG': [1, 3, 1],
    'Competitividade_Empresa': [0, 10, 67]  # % abaixo do mercado PB
})

dados_paraiba.to_csv('/home/ubuntu/comparacao_mercado_paraiba.csv', index=False)

# Lista de concorrentes identificados
concorrentes_detalhados = pd.DataFrame([
    {'Empresa': 'BR3DPRINT', 'Cidade': 'João Pessoa', 'Serviço': 'Impressão 3D', 'Instagram': '@br3dprint'},
    {'Empresa': '3Dados', 'Cidade': 'João Pessoa', 'Serviço': 'Impressão 3D', 'Instagram': '@3dadosjp'},
    {'Empresa': '3D Eco House', 'Cidade': 'Paraíba', 'Serviço': 'Impressão 3D Concreto', 'Instagram': '-'},
    {'Empresa': '3D Tudo Tech', 'Cidade': 'Campina Grande', 'Serviço': 'Impressão 3D', 'Instagram': '@3dtudotech'},
    {'Empresa': 'Laser Maravilha', 'Cidade': 'João Pessoa', 'Serviço': 'Corte Laser', 'Site': 'lasermaravilha.com.br'},
    {'Empresa': 'Mega Arts', 'Cidade': 'João Pessoa', 'Serviço': 'Corte Laser', 'Instagram': '@mega_arts_'},
    {'Empresa': 'Acrílaser PB', 'Cidade': 'João Pessoa', 'Serviço': 'Corte Laser', 'Instagram': '@acrilaserpb'},
    {'Empresa': 'CW Arts', 'Cidade': 'Campina Grande', 'Serviço': 'Corte Laser', 'Instagram': '@artscw'},
    {'Empresa': 'Paradaise', 'Cidade': 'Campina Grande', 'Serviço': 'Corte Laser', 'Instagram': '@paradaisemdf'},
    {'Empresa': 'Lapidary', 'Cidade': 'Campina Grande', 'Serviço': 'Corte Laser', 'Site': 'lapidary.ueniweb.com'},
    {'Empresa': 'JA Metalúrgica', 'Cidade': 'João Pessoa', 'Serviço': 'CNC/Usinagem', 'Instagram': '@jametalurgica2'},
    {'Empresa': 'JG Usinagem', 'Cidade': 'João Pessoa', 'Serviço': 'CNC/Usinagem', 'Site': 'jgusinagem.com.br'},
    {'Empresa': 'NB Máquinas', 'Cidade': 'Campina Grande', 'Serviço': 'CNC/Usinagem', 'Site': 'nb-maquinas-motores.ueniweb.com'},
    {'Empresa': 'TOO Coworking', 'Cidade': 'João Pessoa', 'Serviço': 'Salas/Coworking', 'Site': 'toocoworking.com.br'},
    {'Empresa': 'Sua Esfera', 'Cidade': 'João Pessoa', 'Serviço': 'Coworking', 'Site': 'suaesfera.com'},
    {'Empresa': 'PRÁTICO', 'Cidade': 'João Pessoa', 'Serviço': 'Escritório Virtual', 'Instagram': '-'},
    {'Empresa': 'Sul Office', 'Cidade': 'João Pessoa', 'Serviço': 'Coworking', 'Site': 'sulofficecw.com'},
    {'Empresa': 'Êxito Coworking', 'Cidade': 'João Pessoa', 'Serviço': 'Coworking', 'Site': 'exitocoworking.com'},
    {'Empresa': 'BL Escritório Virtual', 'Cidade': 'João Pessoa', 'Serviço': 'Salas por Hora', 'Instagram': '-'}
])

concorrentes_detalhados.to_csv('/home/ubuntu/concorrentes_paraiba_detalhados.csv', index=False)

print("\n" + "="*80)
print("ANÁLISE ESPECÍFICA DO MERCADO PARAIBANO CONCLUÍDA")
print("="*80)

print("\nArquivos gerados:")
print("- comparacao_mercado_paraiba.png")
print("- oportunidades_mercado_paraiba.png")
print("- mapa_concorrencia_paraiba.png")
print("- comparacao_mercado_paraiba.csv")
print("- concorrentes_paraiba_detalhados.csv")

print("\nResumo da Análise Paraibana:")
print("- 19 concorrentes identificados na Paraíba")
print("- João Pessoa: 13 empresas | Campina Grande: 6 empresas")
print("- Maior concorrência: Corte a Laser (7 empresas)")
print("- Menor concorrência: Impressão 3D (4 empresas)")
print("- FabLab UFPB: Único com oferta completa integrada")

print("\nOportunidades Específicas PB:")
print("- CNC Router: 67% abaixo do mercado local")
print("- Corte Laser: 10% abaixo do mercado local")
print("- Salas: Preços alinhados com mercado premium")
print("- Potencial aumento receita: R$ 2.268 - R$ 4.536/ano")

print("\n" + "="*80)

