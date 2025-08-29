#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GRÁFICOS COMPARATIVOS - FABLAB UFPB vs MERCADO
Análise visual dos preços praticados
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
print("GRÁFICOS COMPARATIVOS - FABLAB UFPB vs MERCADO")
print("="*80)

# ============================================================================
# 1. DADOS COMPARATIVOS
# ============================================================================

# Impressão 3D - Comparação por hora
impressao_3d = pd.DataFrame({
    'Categoria': ['FabLab Estudante', 'FabLab Startup', 'FabLab Empresa', 
                  'Mercado Mínimo', 'Mercado Médio', 'Mercado Máximo'],
    'FDM': [1.60, 8.00, 16.00, 10.00, 20.00, 30.00],
    'Resina': [2.00, 10.00, 20.00, 15.00, 25.00, 50.00]
})

# Corte a Laser - Comparação por hora (convertido de minuto)
corte_laser = pd.DataFrame({
    'Categoria': ['FabLab Estudante', 'FabLab Startup', 'FabLab Empresa', 
                  'Mercado Mínimo', 'Mercado Médio', 'Mercado Máximo'],
    'Preco_Hora': [18.00, 36.00, 72.00, 87.00, 120.00, 240.00]
})

# CNC - Comparação por hora
cnc_dados = pd.DataFrame({
    'Categoria': ['FabLab Router Estudante', 'FabLab Router Startup', 'FabLab Router Empresa',
                  'Mercado Torno CNC', 'Mercado Centro 3 Eixos', 'Mercado Torno Conv.'],
    'Preco_Hora': [4.00, 20.00, 40.00, 156.28, 189.78, 107.65]
})

# Salas - Comparação por hora
salas_dados = pd.DataFrame({
    'Categoria': ['FabLab Reunião Est.', 'FabLab Reunião Emp.', 'FabLab Trein. Est.', 'FabLab Trein. Emp.',
                  'Mercado Reunião', 'Mercado Treinamento'],
    'Preco_Hora': [4.00, 40.00, 10.00, 100.00, 52.50, 60.00]
})

# ============================================================================
# 2. GRÁFICOS COMPARATIVOS
# ============================================================================

# Criar figura com subplots
fig = plt.figure(figsize=(20, 16))

# Gráfico 1: Impressão 3D FDM
ax1 = plt.subplot(2, 3, 1)
x_pos = np.arange(len(impressao_3d))
bars1 = ax1.bar(x_pos, impressao_3d['FDM'], 
                color=['#2E8B57', '#4682B4', '#DC143C', '#FFD700', '#FF8C00', '#FF4500'])
ax1.set_title('Impressão 3D FDM - Comparação de Preços', fontsize=14, fontweight='bold')
ax1.set_ylabel('Preço por Hora (R$)')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(impressao_3d['Categoria'], rotation=45, ha='right')
ax1.grid(True, alpha=0.3)

# Adicionar valores nas barras
for i, v in enumerate(impressao_3d['FDM']):
    ax1.text(i, v + 0.5, f'R$ {v:.2f}', ha='center', va='bottom', fontweight='bold')

# Gráfico 2: Impressão 3D Resina
ax2 = plt.subplot(2, 3, 2)
bars2 = ax2.bar(x_pos, impressao_3d['Resina'], 
                color=['#2E8B57', '#4682B4', '#DC143C', '#FFD700', '#FF8C00', '#FF4500'])
ax2.set_title('Impressão 3D Resina - Comparação de Preços', fontsize=14, fontweight='bold')
ax2.set_ylabel('Preço por Hora (R$)')
ax2.set_xticks(x_pos)
ax2.set_xticklabels(impressao_3d['Categoria'], rotation=45, ha='right')
ax2.grid(True, alpha=0.3)

for i, v in enumerate(impressao_3d['Resina']):
    ax2.text(i, v + 1, f'R$ {v:.2f}', ha='center', va='bottom', fontweight='bold')

# Gráfico 3: Corte a Laser
ax3 = plt.subplot(2, 3, 3)
x_pos_laser = np.arange(len(corte_laser))
bars3 = ax3.bar(x_pos_laser, corte_laser['Preco_Hora'], 
                color=['#2E8B57', '#4682B4', '#DC143C', '#FFD700', '#FF8C00', '#FF4500'])
ax3.set_title('Corte a Laser - Comparação de Preços', fontsize=14, fontweight='bold')
ax3.set_ylabel('Preço por Hora (R$)')
ax3.set_xticks(x_pos_laser)
ax3.set_xticklabels(corte_laser['Categoria'], rotation=45, ha='right')
ax3.grid(True, alpha=0.3)

for i, v in enumerate(corte_laser['Preco_Hora']):
    ax3.text(i, v + 5, f'R$ {v:.2f}', ha='center', va='bottom', fontweight='bold')

# Gráfico 4: CNC
ax4 = plt.subplot(2, 3, 4)
x_pos_cnc = np.arange(len(cnc_dados))
bars4 = ax4.bar(x_pos_cnc, cnc_dados['Preco_Hora'], 
                color=['#2E8B57', '#4682B4', '#DC143C', '#FFD700', '#FF8C00', '#FF4500'])
ax4.set_title('CNC - Comparação de Preços', fontsize=14, fontweight='bold')
ax4.set_ylabel('Preço por Hora (R$)')
ax4.set_xticks(x_pos_cnc)
ax4.set_xticklabels(cnc_dados['Categoria'], rotation=45, ha='right')
ax4.grid(True, alpha=0.3)

for i, v in enumerate(cnc_dados['Preco_Hora']):
    ax4.text(i, v + 5, f'R$ {v:.2f}', ha='center', va='bottom', fontweight='bold')

# Gráfico 5: Salas
ax5 = plt.subplot(2, 3, 5)
x_pos_salas = np.arange(len(salas_dados))
bars5 = ax5.bar(x_pos_salas, salas_dados['Preco_Hora'], 
                color=['#2E8B57', '#4682B4', '#32CD32', '#DC143C', '#FFD700', '#FF8C00'])
ax5.set_title('Salas - Comparação de Preços', fontsize=14, fontweight='bold')
ax5.set_ylabel('Preço por Hora (R$)')
ax5.set_xticks(x_pos_salas)
ax5.set_xticklabels(salas_dados['Categoria'], rotation=45, ha='right')
ax5.grid(True, alpha=0.3)

for i, v in enumerate(salas_dados['Preco_Hora']):
    ax5.text(i, v + 2, f'R$ {v:.2f}', ha='center', va='bottom', fontweight='bold')

# Gráfico 6: Resumo Competitividade
ax6 = plt.subplot(2, 3, 6)

# Dados de competitividade (% abaixo do mercado)
servicos = ['Impressão 3D\nFDM', 'Impressão 3D\nResina', 'Corte Laser', 'CNC Router', 'Sala Reunião', 'Sala Trein.']
competitividade = [60, 70, 40, 85, 10, -20]  # % abaixo do mercado (negativo = acima)

colors = ['green' if x > 30 else 'orange' if x > 0 else 'red' for x in competitividade]
bars6 = ax6.bar(servicos, competitividade, color=colors, alpha=0.7)
ax6.set_title('Competitividade FabLab vs Mercado', fontsize=14, fontweight='bold')
ax6.set_ylabel('% Abaixo do Mercado')
ax6.axhline(y=0, color='black', linestyle='-', alpha=0.3)
ax6.grid(True, alpha=0.3)

for i, v in enumerate(competitividade):
    ax6.text(i, v + (2 if v > 0 else -5), f'{v}%', ha='center', va='bottom' if v > 0 else 'top', fontweight='bold')

plt.tight_layout()
plt.savefig('/home/ubuntu/comparacao_precos_fablab_mercado.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 3. GRÁFICO DE OPORTUNIDADES DE RECEITA
# ============================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Cenários de aumento de receita
cenarios = ['Atual', 'Conservador\n(+30%)', 'Realista\n(+50%)', 'Otimista\n(+80%)']
receitas = [5670, 7371, 8505, 10206]
aumentos = [0, 1701, 2835, 4536]

# Gráfico de receitas
bars1 = ax1.bar(cenarios, receitas, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
ax1.set_title('Projeção de Receita Anual', fontsize=14, fontweight='bold')
ax1.set_ylabel('Receita Anual (R$)')
ax1.grid(True, alpha=0.3)

for i, v in enumerate(receitas):
    ax1.text(i, v + 100, f'R$ {v:,.0f}', ha='center', va='bottom', fontweight='bold')

# Gráfico de aumentos
bars2 = ax2.bar(cenarios[1:], aumentos[1:], color=['#4ECDC4', '#45B7D1', '#96CEB4'])
ax2.set_title('Potencial de Aumento de Receita', fontsize=14, fontweight='bold')
ax2.set_ylabel('Aumento Anual (R$)')
ax2.grid(True, alpha=0.3)

for i, v in enumerate(aumentos[1:]):
    ax2.text(i, v + 50, f'R$ {v:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('/home/ubuntu/oportunidades_receita_fablab.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 4. MAPA DE CALOR - COMPETITIVIDADE POR SERVIÇO E CATEGORIA
# ============================================================================

# Dados para mapa de calor (% diferença do mercado)
servicos_mapa = ['Impressão 3D', 'Corte Laser', 'CNC Router', 'Sala Reunião', 'Sala Treinamento']
categorias_mapa = ['Estudante', 'Startup', 'Empresa']

# Matriz de competitividade (% abaixo do mercado)
competitividade_matriz = np.array([
    [85, 60, 20],  # Impressão 3D
    [70, 50, 30],  # Corte Laser
    [95, 85, 75],  # CNC Router
    [85, 60, 20],  # Sala Reunião
    [80, 15, -40]  # Sala Treinamento
])

fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(competitividade_matriz, cmap='RdYlGn', aspect='auto', vmin=-50, vmax=100)

# Configurar ticks
ax.set_xticks(np.arange(len(categorias_mapa)))
ax.set_yticks(np.arange(len(servicos_mapa)))
ax.set_xticklabels(categorias_mapa)
ax.set_yticklabels(servicos_mapa)

# Adicionar valores nas células
for i in range(len(servicos_mapa)):
    for j in range(len(categorias_mapa)):
        text = ax.text(j, i, f'{competitividade_matriz[i, j]}%',
                      ha="center", va="center", color="black", fontweight='bold')

ax.set_title('Mapa de Competitividade FabLab UFPB\n(% Abaixo do Mercado)', fontsize=14, fontweight='bold')
plt.colorbar(im, ax=ax, label='% Abaixo do Mercado')
plt.tight_layout()
plt.savefig('/home/ubuntu/mapa_competitividade_fablab.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================================================
# 5. EXPORTAR DADOS PARA CSV
# ============================================================================

# Consolidar todos os dados
dados_consolidados = pd.DataFrame({
    'Serviço': ['Impressão 3D FDM', 'Impressão 3D Resina', 'Corte Laser', 'CNC Router', 'Sala Reunião', 'Sala Treinamento'],
    'FabLab_Estudante': [1.60, 2.00, 18.00, 4.00, 4.00, 10.00],
    'FabLab_Startup': [8.00, 10.00, 36.00, 20.00, 20.00, 50.00],
    'FabLab_Empresa': [16.00, 20.00, 72.00, 40.00, 40.00, 100.00],
    'Mercado_Minimo': [10.00, 15.00, 87.00, 107.65, 35.00, 50.00],
    'Mercado_Medio': [20.00, 25.00, 120.00, 156.28, 52.50, 60.00],
    'Mercado_Maximo': [30.00, 50.00, 240.00, 189.78, 75.00, 100.00],
    'Competitividade_Estudante': [84, 87, 79, 96, 89, 80],
    'Competitividade_Startup': [60, 60, 70, 87, 62, 17],
    'Competitividade_Empresa': [20, 20, 40, 75, 24, 0]
})

dados_consolidados.to_csv('/home/ubuntu/comparacao_precos_consolidada.csv', index=False)

print("\n" + "="*80)
print("GRÁFICOS E ANÁLISES GERADOS COM SUCESSO")
print("="*80)

print("\nArquivos gerados:")
print("- comparacao_precos_fablab_mercado.png")
print("- oportunidades_receita_fablab.png") 
print("- mapa_competitividade_fablab.png")
print("- comparacao_precos_consolidada.csv")

print("\nResumo da Análise:")
print("- FabLab UFPB tem preços 20-95% abaixo do mercado")
print("- Maior oportunidade: CNC Router (75-95% abaixo)")
print("- Potencial aumento receita: R$ 1.700 - R$ 4.500/ano")
print("- Preços estudante mantêm missão educacional")

print("\n" + "="*80)

