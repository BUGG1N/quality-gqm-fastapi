#!/usr/bin/env python3
"""
Script para processar e analisar dados do estudo GQM no FastAPI
"""

import os
import json
import re
from collections import defaultdict, Counter
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def analyze_complexity_data():
    """Analisa dados de complexidade ciclomática do Radon"""
    print("=== ANÁLISE DE COMPLEXIDADE CICLOMÁTICA ===")
    
    cc_file = "data/cc.txt"
    if not os.path.exists(cc_file):
        print(f"Arquivo {cc_file} não encontrado")
        return
    
    complexity_data = []
    current_file = ""
    
    with open(cc_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith(' '):  # Nome do arquivo
                current_file = line
            elif line.startswith('    ') and ' - ' in line:  # Método/função
                parts = line.split(' - ')
                if len(parts) >= 2:
                    method_info = parts[0].strip()
                    complexity_info = parts[1]
                    complexity_grade = complexity_info.split()[0]  # A, B, C, D, E, F
                    if '(' in complexity_info:
                        try:
                            complexity_value = int(complexity_info.split('(')[1].split(')')[0])
                        except (ValueError, IndexError):
                            continue
                        # Extrair nome do método
                        method_parts = method_info.split(' ')
                        if len(method_parts) >= 3:
                            method_name = method_parts[2]  # Ex: "M 67:4 FastAPI.__init__"
                        else:
                            method_name = method_info
                        
                        complexity_data.append({
                            'file': current_file,
                            'method': method_name,
                            'grade': complexity_grade,
                            'value': complexity_value
                        })
    
    df_complexity = pd.DataFrame(complexity_data)
    
    print(f"Total de funções/métodos analisados: {len(df_complexity)}")
    
    if len(df_complexity) > 0:
        print(f"Complexidade média: {df_complexity['value'].mean():.2f}")
        print(f"Complexidade máxima: {df_complexity['value'].max()}")
        print(f"Complexidade mínima: {df_complexity['value'].min()}")
    else:
        print("Nenhum dado de complexidade encontrado")
    
    if len(df_complexity) > 0:
        # Top 10 métodos mais complexos
        print("\nTop 10 métodos mais complexos:")
        top_complex = df_complexity.nlargest(10, 'value')
        for _, row in top_complex.iterrows():
            print(f"  {row['method']}: {row['value']} ({row['grade']}) - {row['file']}")
        
        # Distribuição por grades
        print("\nDistribuição por grades de complexidade:")
        grade_counts = df_complexity['grade'].value_counts().sort_index()
        for grade, count in grade_counts.items():
            print(f"  {grade}: {count} métodos")
    
    return df_complexity

def analyze_maintainability_data():
    """Analisa dados do índice de manutenibilidade"""
    print("\n=== ANÁLISE DE ÍNDICE DE MANUTENIBILIDADE ===")
    
    mi_file = "data/mi.txt"
    if not os.path.exists(mi_file):
        print(f"Arquivo {mi_file} não encontrado")
        return
    
    mi_data = []
    
    with open(mi_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if ' - ' in line:
                parts = line.split(' - ')
                file_path = parts[0]
                if '(' in parts[1]:
                    grade = parts[1].split()[0]
                    value = float(parts[1].split('(')[1].split(')')[0])
                    mi_data.append({
                        'file': file_path,
                        'grade': grade,
                        'value': value
                    })
    
    df_mi = pd.DataFrame(mi_data)
    
    print(f"Total de arquivos analisados: {len(df_mi)}")
    print(f"Índice médio de manutenibilidade: {df_mi['value'].mean():.2f}")
    print(f"Valor máximo: {df_mi['value'].max():.2f}")
    print(f"Valor mínimo: {df_mi['value'].min():.2f}")
    
    # Arquivos com menor manutenibilidade (potenciais hotspots)
    print("\nArquivos com menor manutenibilidade:")
    worst_mi = df_mi.nsmallest(10, 'value')
    for _, row in worst_mi.iterrows():
        print(f"  {row['file']}: {row['value']:.2f} ({row['grade']})")
    
    return df_mi

def analyze_sloc_data():
    """Analisa dados de SLOC (Source Lines of Code)"""
    print("\n=== ANÁLISE DE SLOC (LINHAS DE CÓDIGO) ===")
    
    sloc_file = "data/sloc.txt"
    if not os.path.exists(sloc_file):
        print(f"Arquivo {sloc_file} não encontrado")
        return
    
    sloc_data = []
    
    with open(sloc_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('Total'):
                parts = line.split('\t')
                if len(parts) >= 4:
                    sloc = int(parts[0])
                    language = parts[1]
                    module = parts[2]
                    file_path = parts[3]
                    sloc_data.append({
                        'sloc': sloc,
                        'language': language,
                        'module': module,
                        'file': file_path
                    })
    
    df_sloc = pd.DataFrame(sloc_data)
    
    print(f"Total de arquivos: {len(df_sloc)}")
    print(f"Total de linhas de código: {df_sloc['sloc'].sum()}")
    print(f"Média de linhas por arquivo: {df_sloc['sloc'].mean():.2f}")
    
    # Maiores arquivos
    print("\nMaiores arquivos por SLOC:")
    largest_files = df_sloc.nlargest(10, 'sloc')
    for _, row in largest_files.iterrows():
        print(f"  {row['file']}: {row['sloc']} linhas")
    
    return df_sloc

def analyze_churn_data():
    """Analisa dados de churn do Git"""
    print("\n=== ANÁLISE DE CHURN (ALTERAÇÕES FREQUENTES) ===")
    
    churn_file = "data/git_numstat.log"
    if not os.path.exists(churn_file):
        print(f"Arquivo {churn_file} não encontrado")
        return
    
    file_changes = defaultdict(lambda: {'additions': 0, 'deletions': 0, 'commits': 0})
    
    with open(churn_file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if '\t' in line and line.split('\t')[0].isdigit():
            parts = line.split('\t')
            if len(parts) >= 3:
                try:
                    additions = int(parts[0]) if parts[0] != '-' else 0
                    deletions = int(parts[1]) if parts[1] != '-' else 0
                    file_path = parts[2]
                    
                    if file_path.startswith('fastapi/') and file_path.endswith('.py'):
                        file_changes[file_path]['additions'] += additions
                        file_changes[file_path]['deletions'] += deletions
                        file_changes[file_path]['commits'] += 1
                except ValueError:
                    continue
    
    churn_data = []
    for file_path, data in file_changes.items():
        total_changes = data['additions'] + data['deletions']
        churn_data.append({
            'file': file_path,
            'total_changes': total_changes,
            'additions': data['additions'],
            'deletions': data['deletions'],
            'commits': data['commits']
        })
    
    df_churn = pd.DataFrame(churn_data)
    
    if len(df_churn) > 0:
        df_churn = df_churn.sort_values('total_changes', ascending=False)
        
        print(f"Total de arquivos Python com alterações: {len(df_churn)}")
        print(f"Total de alterações: {df_churn['total_changes'].sum()}")
        
        # Arquivos com maior churn
        print("\nArquivos com maior churn (últimos 12 meses):")
        top_churn = df_churn.head(10)
        for _, row in top_churn.iterrows():
            print(f"  {row['file']}: {row['total_changes']} alterações ({row['commits']} commits)")
    else:
        print("Nenhum dado de churn encontrado")
    
    return df_churn

def identify_hotspots(df_complexity, df_mi, df_sloc, df_churn):
    """Identifica hotspots críticos cruzando métricas"""
    print("\n=== IDENTIFICAÇÃO DE HOTSPOTS CRÍTICOS ===")
    
    # Mapeamento de arquivos para análise cruzada
    hotspots = {}
    
    # Complexidade alta
    if df_complexity is not None and len(df_complexity) > 0:
        high_complexity_files = df_complexity[df_complexity['value'] >= 10]['file'].unique()
        for file in high_complexity_files:
            if file not in hotspots:
                hotspots[file] = {'issues': []}
            hotspots[file]['issues'].append('Alta Complexidade')
    
    # Baixa manutenibilidade
    if df_mi is not None and len(df_mi) > 0:
        low_maintainability_files = df_mi[df_mi['value'] < 50]['file'].unique()
        for file in low_maintainability_files:
            if file not in hotspots:
                hotspots[file] = {'issues': []}
            hotspots[file]['issues'].append('Baixa Manutenibilidade')
    
    # Alto churn
    if df_churn is not None and len(df_churn) > 0:
        # Considera top 20% dos arquivos com maior churn
        threshold = df_churn['total_changes'].quantile(0.8)
        high_churn_files = df_churn[df_churn['total_changes'] >= threshold]['file'].unique()
        for file in high_churn_files:
            if file not in hotspots:
                hotspots[file] = {'issues': []}
            hotspots[file]['issues'].append('Alto Churn')
    
    # Arquivos grandes
    if df_sloc is not None and len(df_sloc) > 0:
        large_files = df_sloc[df_sloc['sloc'] > 1000]['file'].unique()
        for file in large_files:
            file_path = f"fastapi/{file.split('/')[-1]}" if '/' in file else f"fastapi/{file}"
            if file_path not in hotspots:
                hotspots[file_path] = {'issues': []}
            hotspots[file_path]['issues'].append('Arquivo Grande')
    
    print("Hotspots identificados (arquivos com múltiplos problemas):")
    critical_hotspots = {k: v for k, v in hotspots.items() if len(v['issues']) >= 2}
    
    for file, data in sorted(critical_hotspots.items(), key=lambda x: len(x[1]['issues']), reverse=True):
        print(f"  {file}: {', '.join(data['issues'])}")
    
    if not critical_hotspots:
        print("  Nenhum hotspot crítico identificado (arquivos com múltiplos problemas)")
    
    print(f"\nTotal de arquivos com pelo menos um problema: {len(hotspots)}")
    print(f"Total de hotspots críticos: {len(critical_hotspots)}")
    
    return hotspots, critical_hotspots

def generate_summary_report():
    """Gera relatório resumo das métricas"""
    print("\n" + "="*60)
    print("RELATÓRIO RESUMO - ESTUDO GQM FASTAPI")
    print("="*60)
    
    # Executar todas as análises
    df_complexity = analyze_complexity_data()
    df_mi = analyze_maintainability_data()
    df_sloc = analyze_sloc_data()
    df_churn = analyze_churn_data()
    
    # Identificar hotspots
    hotspots, critical_hotspots = identify_hotspots(df_complexity, df_mi, df_sloc, df_churn)
    
    # Salvar dados processados
    summary_data = {
        'timestamp': datetime.now().isoformat(),
        'complexity_stats': {
            'total_methods': len(df_complexity) if df_complexity is not None and len(df_complexity) > 0 else 0,
            'avg_complexity': float(df_complexity['value'].mean()) if df_complexity is not None and len(df_complexity) > 0 else 0,
            'max_complexity': int(df_complexity['value'].max()) if df_complexity is not None and len(df_complexity) > 0 else 0
        },
        'maintainability_stats': {
            'total_files': len(df_mi) if df_mi is not None and len(df_mi) > 0 else 0,
            'avg_maintainability': float(df_mi['value'].mean()) if df_mi is not None and len(df_mi) > 0 else 0,
            'min_maintainability': float(df_mi['value'].min()) if df_mi is not None and len(df_mi) > 0 else 0
        },
        'sloc_stats': {
            'total_files': len(df_sloc) if df_sloc is not None and len(df_sloc) > 0 else 0,
            'total_sloc': int(df_sloc['sloc'].sum()) if df_sloc is not None and len(df_sloc) > 0 else 0,
            'avg_sloc_per_file': float(df_sloc['sloc'].mean()) if df_sloc is not None and len(df_sloc) > 0 else 0
        },
        'churn_stats': {
            'files_with_changes': len(df_churn) if df_churn is not None and len(df_churn) > 0 else 0,
            'total_changes': int(df_churn['total_changes'].sum()) if df_churn is not None and len(df_churn) > 0 else 0
        },
        'hotspots': {
            'total_files_with_issues': len(hotspots),
            'critical_hotspots': len(critical_hotspots),
            'critical_files': list(critical_hotspots.keys())[:10]  # Top 10
        }
    }
    
    # Salvar resumo em JSON
    with open('data/analysis_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nRelatório salvo em: data/analysis_summary.json")
    
    return summary_data

if __name__ == "__main__":
    # Verificar se estamos no diretório correto
    if not os.path.exists('fastapi'):
        print("ERRO: Execute este script no diretório raiz do projeto FastAPI")
        exit(1)
    
    # Criar diretório de dados se não existir
    os.makedirs('data', exist_ok=True)
    
    # Executar análise completa
    summary = generate_summary_report()
    
    print("\nAnálise concluída! Dados salvos em data/analysis_summary.json")