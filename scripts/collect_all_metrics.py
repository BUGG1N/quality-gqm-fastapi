#!/usr/bin/env python3
"""
Script de Coleta Automatizada - FastAPI GQM Analysis
Executa coleta completa de métricas de forma reproduzível

Autor: Análise GQM FastAPI - UFJF
Data: 2025-10-01
"""

import os
import sys
import subprocess
import json
import time
from pathlib import Path
from datetime import datetime

def print_banner():
    """Exibe banner do script"""
    print("🚀 FastAPI GQM Quality Analysis - Coleta Automatizada")
    print("=" * 60)
    print("📚 UFJF - Métricas de Software (1322004)")
    print("👨‍🏫 Prof. Leonardo Vieira dos Santos Reis")
    print("📅 Data:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 60)
    print()

def check_prerequisites():
    """Verifica pré-requisitos do sistema"""
    print("🔍 Verificando pré-requisitos...")
    
    errors = []
    
    # Verificar Python
    try:
        python_version = sys.version.split()[0]
        print(f"✅ Python: {python_version}")
    except Exception as e:
        errors.append(f"Python: {e}")
    
    # Verificar ferramentas necessárias
    tools = {
        'git': ['git', '--version'],
        'radon': ['radon', '--version'],
        'pygount': ['pygount', '--version']
    }
    
    for tool, cmd in tools.items():
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                version = result.stdout.strip().split('\n')[0]
                print(f"✅ {tool}: {version}")
            else:
                errors.append(f"{tool}: comando falhou")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            errors.append(f"{tool}: não encontrado")
        except Exception as e:
            errors.append(f"{tool}: {e}")
    
    if errors:
        print("\n❌ Erros encontrados:")
        for error in errors:
            print(f"  - {error}")
        print("\n💡 Instale as dependências:")
        print("  pip install radon pygount pandas matplotlib")
        return False
    
    print("✅ Todos os pré-requisitos atendidos!\n")
    return True

def setup_directories():
    """Cria estrutura de diretórios necessária"""
    print("📁 Configurando estrutura de diretórios...")
    
    dirs = ['data', 'docs', 'scripts', 'img']
    
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
        print(f"✅ {dir_name}/")
    
    print()

def check_fastapi_repo():
    """Verifica se repositório FastAPI está disponível"""
    print("🔍 Verificando repositório FastAPI...")
    
    fastapi_dir = Path("fastapi")
    
    if not fastapi_dir.exists():
        print("❌ Diretório 'fastapi' não encontrado")
        print("💡 Clone o repositório:")
        print("  git clone https://github.com/tiangolo/fastapi.git")
        print("  cd fastapi && git checkout 45bfb89ea25fcbe8c44ac5d5657b147cfa074649")
        return False
    
    # Verificar se é o commit correto
    try:
        os.chdir("fastapi")
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                              capture_output=True, text=True)
        current_commit = result.stdout.strip()
        
        expected_commit = "45bfb89ea25fcbe8c44ac5d5657b147cfa074649"
        
        if current_commit == expected_commit:
            print(f"✅ FastAPI commit correto: {current_commit[:12]}")
        else:
            print(f"⚠️  Commit diferente: {current_commit[:12]}")
            print(f"   Esperado: {expected_commit[:12]}")
            print("💡 Execute: git checkout 45bfb89ea25fcbe8c44ac5d5657b147cfa074649")
        
        os.chdir("..")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao verificar commit: {e}")
        os.chdir("..")
        return False

def collect_complexity_metrics():
    """Coleta métricas de complexidade ciclomática"""
    print("📊 Coletando complexidade ciclomática...")
    
    try:
        # Complexidade ciclomática
        with open("data/cc.txt", "w", encoding="utf-8") as f:
            result = subprocess.run(
                ['radon', 'cc', '-s', '-a', 'fastapi/'],
                stdout=f, stderr=subprocess.PIPE, text=True
            )
        
        if result.returncode == 0:
            print("✅ Complexidade ciclomática coletada")
        else:
            print(f"⚠️  Aviso radon cc: {result.stderr}")
            
        time.sleep(1)
        
        # Índice de manutenibilidade
        with open("data/mi.txt", "w", encoding="utf-8") as f:
            result = subprocess.run(
                ['radon', 'mi', '-s', 'fastapi/'],
                stdout=f, stderr=subprocess.PIPE, text=True
            )
        
        if result.returncode == 0:
            print("✅ Índice de manutenibilidade coletado")
        else:
            print(f"⚠️  Aviso radon mi: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Erro ao coletar métricas de complexidade: {e}")

def collect_sloc_metrics():
    """Coleta métricas de linhas de código"""
    print("📏 Coletando linhas de código...")
    
    try:
        # SLOC em formato texto
        with open("data/sloc.txt", "w", encoding="utf-8") as f:
            result = subprocess.run(
                ['pygount', '--format=summary', 'fastapi/'],
                stdout=f, stderr=subprocess.PIPE, text=True
            )
        
        if result.returncode == 0:
            print("✅ SLOC (texto) coletado")
        else:
            print(f"⚠️  Aviso pygount summary: {result.stderr}")
            
        time.sleep(1)
        
        # SLOC em formato JSON
        with open("data/sloc.json", "w", encoding="utf-8") as f:
            result = subprocess.run(
                ['pygount', '--format=json', 'fastapi/'],
                stdout=f, stderr=subprocess.PIPE, text=True
            )
        
        if result.returncode == 0:
            print("✅ SLOC (JSON) coletado")
        else:
            print(f"⚠️  Aviso pygount json: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Erro ao coletar SLOC: {e}")

def collect_git_metrics():
    """Coleta métricas de churn do Git"""
    print("📈 Coletando métricas de churn...")
    
    try:
        os.chdir("fastapi")
        
        with open("../data/git_numstat.log", "w", encoding="utf-8") as f:
            result = subprocess.run([
                'git', 'log', '--since=12 months ago', '--numstat', 
                '--date=iso', '--pretty=format:%H;%ad;%an;%s'
            ], stdout=f, stderr=subprocess.PIPE, text=True)
        
        os.chdir("..")
        
        if result.returncode == 0:
            print("✅ Churn do Git coletado")
        else:
            print(f"⚠️  Aviso git log: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Erro ao coletar churn: {e}")
        os.chdir("..")

def collect_version_info():
    """Coleta informações de versão"""
    print("📋 Coletando informações de versão...")
    
    try:
        os.chdir("fastapi")
        
        # Hash do commit
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                              capture_output=True, text=True)
        commit_hash = result.stdout.strip()
        
        # Descrição da versão
        result = subprocess.run(['git', 'describe', '--tags', '--always'], 
                              capture_output=True, text=True)
        version_desc = result.stdout.strip()
        
        os.chdir("..")
        
        version_info = {
            "commit_hash": commit_hash,
            "version": version_desc,
            "analysis_date": datetime.now().isoformat(),
            "repository": "https://github.com/tiangolo/fastapi",
            "branch": "master"
        }
        
        with open("data/version_info.txt", "w", encoding="utf-8") as f:
            f.write(f"FastAPI Version Analysis\n")
            f.write(f"========================\n\n")
            f.write(f"Repository: {version_info['repository']}\n")
            f.write(f"Commit Hash: {version_info['commit_hash']}\n")
            f.write(f"Version: {version_info['version']}\n")
            f.write(f"Branch: {version_info['branch']}\n")
            f.write(f"Analysis Date: {version_info['analysis_date']}\n")
        
        print("✅ Informações de versão coletadas")
        
    except Exception as e:
        print(f"❌ Erro ao coletar versão: {e}")
        if os.getcwd().endswith("fastapi"):
            os.chdir("..")

def run_analysis_scripts():
    """Executa scripts de análise"""
    print("🔬 Executando análises...")
    
    scripts = [
        ("scripts/analyze_metrics.py", "Análise de métricas"),
        ("scripts/analyze_hotspots.py", "Análise de hotspots")
    ]
    
    for script_path, description in scripts:
        if Path(script_path).exists():
            try:
                print(f"🔄 {description}...")
                result = subprocess.run([sys.executable, script_path], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"✅ {description} concluída")
                else:
                    print(f"⚠️  {description} com avisos: {result.stderr}")
                    
            except Exception as e:
                print(f"❌ Erro em {description}: {e}")
        else:
            print(f"⚠️  Script {script_path} não encontrado")

def generate_summary():
    """Gera resumo da coleta"""
    print("\n📊 Resumo da Coleta")
    print("=" * 40)
    
    data_dir = Path("data")
    files_info = []
    
    expected_files = [
        "cc.txt", "mi.txt", "sloc.txt", "sloc.json", 
        "git_numstat.log", "version_info.txt"
    ]
    
    for filename in expected_files:
        filepath = data_dir / filename
        if filepath.exists():
            size = filepath.stat().st_size
            files_info.append((filename, size, "✅"))
        else:
            files_info.append((filename, 0, "❌"))
    
    print(f"{'Arquivo':<20} {'Tamanho':<10} {'Status'}")
    print("-" * 40)
    
    for filename, size, status in files_info:
        size_str = f"{size:,} bytes" if size > 0 else "N/A"
        print(f"{filename:<20} {size_str:<10} {status}")
    
    # Contar arquivos de análise adicionais
    analysis_files = list(data_dir.glob("*analysis*.json"))
    if analysis_files:
        print(f"\n📈 Arquivos de análise: {len(analysis_files)}")
        for f in analysis_files:
            print(f"  - {f.name}")
    
    docs_files = list(Path("docs").glob("*.md"))
    if docs_files:
        print(f"\n📋 Documentos gerados: {len(docs_files)}")
        for f in docs_files:
            print(f"  - {f.name}")

def main():
    """Função principal"""
    print_banner()
    
    # Verificar pré-requisitos
    if not check_prerequisites():
        sys.exit(1)
    
    # Configurar estrutura
    setup_directories()
    
    # Verificar FastAPI
    if not check_fastapi_repo():
        sys.exit(1)
    
    print("🚀 Iniciando coleta de métricas...\n")
    
    # Coletar métricas
    collect_complexity_metrics()
    collect_sloc_metrics()
    collect_git_metrics()
    collect_version_info()
    
    print()
    
    # Executar análises
    run_analysis_scripts()
    
    # Gerar resumo
    generate_summary()
    
    print(f"\n🎉 Coleta completa! Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("📁 Verifique os resultados em:")
    print("  - data/ (métricas brutas)")
    print("  - docs/ (relatórios)")
    print("\n💡 Próximos passos:")
    print("  1. Revisar docs/Relatorio_GQM_Final.md")
    print("  2. Verificar docs/Analise_Hotspots.md")
    print("  3. Gerar PDF para entrega")

if __name__ == "__main__":
    main()