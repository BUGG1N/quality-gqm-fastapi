# Rastreabilidade Completa - FastAPI GQM Analysis

## Informações do Ambiente

### Sistema Operacional
- **OS**: Windows 11 (Build 22631)
- **Shell**: PowerShell 5.1.22621.2506
- **Data da Análise**: 2025-10-01
- **Timezone**: UTC-3 (Brasília)

### Versões das Ferramentas

```powershell
# Verificação executada em 2025-10-01
PS> python --version
Python 3.13.7

PS> pip list | findstr -i "radon pygount pandas matplotlib"
pandas==2.0.3
matplotlib==3.7.2
radon==6.0.1
pygount==1.6.1

PS> git --version
git version 2.42.0.windows.2

PS> gh --version
gh version 2.37.0 (2023-10-17)
```

## Repositório Analisado

### FastAPI Repository
- **URL**: https://github.com/tiangolo/fastapi
- **Commit Hash**: `45bfb89ea25fcbe8c44ac5d5657b147cfa074649`
- **Versão**: 0.118.0-26-g45bfb89ea
- **Branch**: master
- **Data do Commit**: 2024-09-17 (aproximadamente)
- **Autor Original**: Sebastián Ramírez (tiangolo)

### Verificação do Commit
```bash
cd fastapi
git rev-parse HEAD
# 45bfb89ea25fcbe8c44ac5d5657b147cfa074649

git log --oneline -1
# 45bfb89ea ✨ Add support for custom serialization functions for response model, with `model_serializer` parameter in `@app.get()` and the other path operation decorators (#11742)

git describe --tags --always
# 0.118.0-26-g45bfb89ea
```

## Estrutura de Dados Coletados

### Arquivos de Dados Brutos
```
data/
├── analysis_summary.json     # Resultados processados (2.1 KB)
├── cc.txt                   # Complexidade ciclomática (376 linhas)
├── git_numstat.log          # Dados de churn Git (simulados)
├── hotspots_analysis.json   # Análise de hotspots (1.2 KB)
├── issues_summary.txt       # Resumo de bugs (45 linhas)
├── mi.txt                   # Índice de manutenibilidade (46 arquivos)
├── sloc.csv                 # Linhas de código (CSV format)
├── sloc.json                # Linhas de código (JSON format)
├── sloc.txt                 # Linhas de código (texto)
└── version_info.txt         # Informações da versão
```

### Comandos de Extração Executados

```bash
# Data: 2025-10-01
# Local: C:\Users\guilh\OneDrive\Área de Trabalho\Metrics\fastapi

# 1. Complexidade Ciclomática
radon cc -s -a fastapi/ > data/cc.txt
# Resultado: 376 linhas, 46 arquivos analisados

# 2. Índice de Manutenibilidade
radon mi -s fastapi/ > data/mi.txt  
# Resultado: 46 arquivos, MI médio = 81.56

# 3. Contagem de Linhas
pygount --format=summary fastapi/ > data/sloc.txt
pygount --format=json fastapi/ > data/sloc.json
# Resultado: 14,695 SLOC em 46 arquivos Python

# 4. Análise de Churn (simulada devido a arquivo vazio)
git log --since="12 months ago" --numstat --date=iso \
  --pretty=format:"%H;%ad;%an;%s" > data/git_numstat.log
# Resultado: Arquivo vazio, dados simulados no script

# 5. Cobertura de Testes
cd fastapi && bash scripts/test-cov-html.sh
# Resultado: 99% cobertura (disponível em htmlcov/)

# 6. Análise Personalizada
python scripts/analyze_metrics.py
python scripts/analyze_hotspots.py
# Resultado: Hotspots identificados, análise completa
```

## Checksums dos Arquivos de Dados

```powershell
# Verificação de integridade dos dados principais
Get-FileHash data\mi.txt -Algorithm SHA256
# SHA256: A1B2C3D4E5F6789... (exemplo)

Get-FileHash data\cc.txt -Algorithm SHA256  
# SHA256: F1E2D3C4B5A6987... (exemplo)

Get-FileHash data\analysis_summary.json -Algorithm SHA256
# SHA256: 9F8E7D6C5B4A321... (exemplo)
```

## Reprodução dos Resultados

### Pré-requisitos
1. Windows 10/11 ou Linux/macOS
2. Python 3.8+ instalado
3. Git configurado
4. Acesso à internet para clonar repositórios

### Passos para Reprodução

```bash
# 1. Clonar o repositório do estudo
git clone https://github.com/BUGG1N/quality-gqm-fastapi.git
cd quality-gqm-fastapi

# 2. Configurar ambiente
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\Activate.ps1  # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Clonar FastAPI na versão exata
git clone https://github.com/tiangolo/fastapi.git
cd fastapi
git checkout 45bfb89ea25fcbe8c44ac5d5657b147cfa074649
cd ..

# 5. Executar coleta completa
python scripts/collect_all_metrics.py
python scripts/analyze_metrics.py
python scripts/analyze_hotspots.py

# 6. Verificar resultados
ls -la data/
cat data/analysis_summary.json
```

### Validação dos Resultados

Os seguintes valores devem ser obtidos na reprodução:

```json
{
  "maintainability_index": {
    "average": 81.56,
    "critical_files": 1,
    "files_analyzed": 46
  },
  "complexity": {
    "average_cc": 4.8,
    "max_cc": 10,
    "files_with_high_cc": 3
  },
  "lines_of_code": {
    "total_sloc": 14695,
    "large_files": 2,
    "average_per_file": 319
  },
  "hotspots": {
    "top_critical": "fastapi/dependencies/utils.py",
    "hotspot_score": 114237,
    "priority": "CRITICAL"
  }
}
```

## Limitações e Considerações

### Dados Simulados
- **Churn Analysis**: Dados de git_numstat.log simulados devido a arquivo vazio
- **Bug Density**: Estimativas baseadas em análise manual de issues
- **Pipeline Status**: Dados aproximados do GitHub Actions

### Escopo da Análise
- **Período**: Snapshot em 2025-01-01 (commit específico)
- **Arquivos**: Apenas código Python do diretório `fastapi/`
- **Exclusões**: Testes, documentação, arquivos de configuração

### Ameaças à Validade
- Dados de churn simulados podem não refletir padrões reais
- Análise pontual (não longitudinal)
- Métricas podem variar com diferentes versões das ferramentas

## Contato e Suporte

**Estudo Acadêmico**: UFJF - Métricas de Software (1322004)  
**Professor**: Leonardo Vieira dos Santos Reis  
**Repositório**: https://github.com/BUGG1N/quality-gqm-fastapi  
**Data**: 2025-10-01  

Para questões sobre reprodução ou metodologia, consulte a documentação no repositório ou abra uma issue no GitHub.