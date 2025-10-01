# FastAPI GQM Quality Analysis | Análise de Qualidade GQM do FastAPI

> **Goal-Question-Metric (GQM) methodology applied to FastAPI framework for software quality assessment**  
> **Metodologia Goal-Question-Metric (GQM) aplicada ao framework FastAPI para avaliação de qualidade de software**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.118.0-009688.svg)](https://fastapi.tiangolo.com)
[![GQM](https://img.shields.io/badge/Methodology-GQM-orange.svg)](https://en.wikipedia.org/wiki/GQM)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🌐 Language / Idioma

**[🇺🇸 English](#english-version)** | **[🇧🇷 Português](#versão-em-português)**

---

# 🇧🇷 Versão em Português

## 📋 Visão Geral

Este repositório contém uma análise abrangente de qualidade de software do **framework FastAPI** utilizando a metodologia **Goal-Question-Metric (GQM)**. O estudo avalia aspectos de manutenibilidade e confiabilidade de um dos frameworks web Python mais populares.

### 🎓 Contexto Acadêmico

**Curso**: Especialização em Gerência de Projetos de Software na Era de Dados de Sensores e IA  
**Instituição**: Universidade Federal de Juiz de Fora (UFJF)  
**Departamento**: Ciência da Computação  
**Disciplina**: Métricas de Software (Código: 1322004)  
**Professor**: Leonardo Vieira dos Santos Reis  
**Período**: 2025/1º Semestre

### 🎯 Objetivos do Estudo

- **G1 - Melhorar Manutenibilidade**: Aprimorar a manutenibilidade do código em módulos críticos (roteamento, parâmetros, injeção de dependência)
- **G2 - Aumentar Confiabilidade**: Melhorar a estabilidade e reduzir a ocorrência de defeitos através de testes e análise de bugs

### 📊 Principais Descobertas

- **Qualidade Geral**: Excelente índice de manutenibilidade de **81,56** (meta: ≥70)
- **Hotspot Crítico**: `fastapi/dependencies/utils.py` requer refatoração imediata (IM: 5,29)
- **Arquivos Grandes**: Dois arquivos excedem os limites recomendados (4.043 e 3.846 linhas)
- **Confiabilidade**: Testes aprovados, densidade de bugs controlada (~0,5-1,0 bugs/KLOC)

## 🚀 Início Rápido

### Configuração Automatizada (Recomendado)
```bash
# Linux/macOS
chmod +x setup.sh
./setup.sh

# Windows
setup.bat
```

### Configuração Manual

1. **Clone o repositório**
   ```bash
   git clone https://github.com/BUGG1N/quality-gqm-fastapi.git
   cd quality-gqm-fastapi
   ```

2. **Configure o ambiente**
   ```bash
   # Criar ambiente virtual
   python -m venv .venv
   source .venv/bin/activate      # Linux/macOS
   # .venv\Scripts\Activate.ps1   # Windows PowerShell
   
   # Instalar dependências
   pip install -r requirements.txt
   ```

3. **Clone o FastAPI para análise**
   ```bash
   git clone https://github.com/tiangolo/fastapi.git
   cd fastapi
   git checkout 45bfb89ea25fcbe8c44ac5d5657b147cfa074649
   cd ..
   ```

4. **Execute a análise**
   ```bash
   python scripts/collect_all_metrics.py
   python scripts/analyze_metrics.py
   ```

## 📈 Metodologia

Este estudo segue a abordagem **Goal-Question-Metric (GQM)** proposta por Basili e Weiss:

1. **Objetivos** - Definir metas conceituais para medição
2. **Questões** - Refinar objetivos em questões operacionais  
3. **Métricas** - Associar métricas quantitativas para responder questões

### Estrutura GQM Aplicada

#### 🎯 Objetivos
- **G1**: Melhorar manutenibilidade em módulos críticos
- **G2**: Aumentar confiabilidade (bugs, testes, pipeline)

#### ❓ Questões (8 no total)
- 4 questões para avaliação de manutenibilidade
- 4 questões para avaliação de confiabilidade

#### 📊 Métricas
- Complexidade Ciclomática (Radon)
- Índice de Manutenibilidade (Radon)  
- Linhas de Código Fonte (Pygount)
- Análise de Churn do Git
- Densidade de Bugs & MTTR
- Cobertura e Status de Testes

## 📋 Resumo dos Resultados

### ✅ Pontos Fortes
- **Alta qualidade geral** com IM de 81,56
- **89% dos arquivos** atendem aos padrões de manutenibilidade
- **Suíte de testes funcional** com todos os testes aprovados
- **Densidade de bugs controlada** dentro dos padrões da indústria

### ⚠️ Áreas para Melhoria
- **Arquivo crítico**: `dependencies/utils.py` (IM: 5,29) precisa de refatoração imediata
- **Arquivos grandes**: `applications.py` (4.043 linhas) e `routing.py` (3.846 linhas)
- **Dívida técnica** concentrada em módulos centrais

### 🎯 Recomendações Prioritárias
1. **ALTA**: Refatorar `fastapi/dependencies/utils.py`
2. **ALTA**: Dividir `fastapi/applications.py` em módulos menores
3. **ALTA**: Refatorar arquitetura do `fastapi/routing.py`
4. **MÉDIA**: Implementar monitoramento contínuo de qualidade

## 📚 Documentação

- **[Relatório Completo](docs/Relatorio_GQM_FastAPI.md)** - Análise GQM completa com 7 seções
- **[Resumo Executivo](docs/Sumario_Executivo.md)** - Principais descobertas e recomendações
- **[Lista de Verificação](docs/Checklist_Entrega.md)** - Validação e verificação de completude

## 🤝 Contribuições

Este é um repositório de estudo acadêmico. No entanto, se você encontrar problemas ou quiser aprimorar a análise:

1. Faça um fork do repositório
2. Crie uma branch de feature
3. Envie um pull request

## 📞 Contato

Para questões sobre esta análise ou a metodologia GQM aplicada:

- **Foco do Estudo**: Avaliação de Qualidade de Software usando GQM
- **Framework Analisado**: FastAPI (framework web Python)
- **Metodologia**: Abordagem Goal-Question-Metric
- **Contexto Acadêmico**: Curso de Métricas de Software UFJF (1322004)
- **Instituição**: Universidade Federal de Juiz de Fora - Depto. Ciência da Computação

---

# 🇺🇸 English Version

## 📋 Overview

This repository contains a comprehensive software quality analysis of the **FastAPI framework** using the **Goal-Question-Metric (GQM)** methodology. The study evaluates maintainability and reliability aspects of one of the most popular Python web frameworks.

### 🎓 Academic Context

**Course**: Software Project Management Specialization in the Era of Sensor Data and AI  
**Institution**: Federal University of Juiz de Fora (UFJF)  
**Department**: Computer Science  
**Subject**: Software Metrics (Code: 1322004)  
**Professor**: Leonardo Vieira dos Santos Reis  
**Period**: 2025/1st Semester

### 🎯 Study Objectives

- **G1 - Improve Maintainability**: Enhance code maintainability in critical modules (routing, parameters, dependency injection)
- **G2 - Increase Reliability**: Improve stability and reduce defect occurrence through testing and bug analysis

### 📊 Key Findings

- **Overall Quality**: Excellent maintainability index of **81.56** (target: ≥70)
- **Critical Hotspot**: `fastapi/dependencies/utils.py` requires immediate refactoring (MI: 5.29)
- **Large Files**: Two files exceed recommended limits (4,043 and 3,846 lines)
- **Reliability**: Tests passing, controlled bug density (~0.5-1.0 bugs/KLOC)

## 🏗️ Repository Structure

```
📁 fastapi-gqm-quality-analysis/
├── 📄 README.md                    # This file
├── 📄 LICENSE                      # MIT License
├── 📁 docs/                        # 📚 Reports and documentation
│   ├── Relatorio_GQM_FastAPI.md    # Complete GQM report (Portuguese)
│   ├── Sumario_Executivo.md        # Executive summary
│   └── Checklist_Entrega.md        # Delivery checklist
├── 📁 data/                        # 📊 Collected metrics data
│   ├── version_info.txt            # Analyzed version details
│   ├── analysis_summary.json       # Processed results
│   ├── mi.txt                      # Maintainability index (Radon)
│   ├── sloc.txt                    # Source lines of code (Pygount)
│   ├── cc.txt                      # Cyclomatic complexity
│   ├── git_numstat.log             # Git churn data
│   └── issues_summary.txt          # Bug density data
├── 📁 scripts/                     # 🔧 Analysis and collection scripts
│   ├── collect_all_metrics.py      # Automated metrics collection
│   └── analyze_metrics.py          # Complete data analysis
└── 📁 assets/                      # 🖼️ Images and visualizations
    └── methodology_diagram.png     # GQM methodology diagram
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Git
- Virtual environment support

### Quick Setup (Automated)

**Option 1: Automated Setup (Recommended)**
```bash
# Linux/macOS
chmod +x setup.sh
./setup.sh

# Windows
setup.bat
```

**Option 2: Manual Setup**

1. **Clone the repository**
   ```bash
   git clone https://github.com/BUGG1N/quality-gqm-fastapi.git
   cd quality-gqm-fastapi
   ```

2. **Set up environment**
   ```bash
   # Create virtual environment
   python -m venv .venv
   source .venv/bin/activate      # Linux/macOS
   # .venv\Scripts\Activate.ps1   # Windows PowerShell
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Clone FastAPI for analysis**
   ```bash
   git clone https://github.com/tiangolo/fastapi.git
   cd fastapi
   git checkout 45bfb89ea25fcbe8c44ac5d5657b147cfa074649
   cd ..
   ```

4. **Run analysis**
   ```bash
   python scripts/collect_all_metrics.py
   python scripts/analyze_metrics.py
   ```

## 📈 Methodology

This study follows the **Goal-Question-Metric (GQM)** approach proposed by Basili and Weiss:

1. **Goals** - Define conceptual objectives for measurement
2. **Questions** - Refine goals into operational questions  
3. **Metrics** - Associate quantitative metrics to answer questions

### Applied GQM Structure

#### 🎯 Goals
- **G1**: Improve maintainability in critical modules
- **G2**: Increase reliability (bugs, tests, pipeline)

#### ❓ Questions (8 total)
- 4 questions for maintainability assessment
- 4 questions for reliability evaluation

#### 📊 Metrics
- Cyclomatic Complexity (Radon)
- Maintainability Index (Radon)  
- Source Lines of Code (Pygount)
- Git Churn Analysis
- Bug Density & MTTR
- Test Coverage & Status

## 📋 Results Summary

### ✅ Strengths
- **High overall quality** with MI of 81.56
- **89% of files** meet maintainability standards
- **Functional test suite** with all tests passing
- **Controlled bug density** within industry standards

### ⚠️ Areas for Improvement
- **Critical file**: `dependencies/utils.py` (MI: 5.29) needs immediate refactoring
- **Large files**: `applications.py` (4,043 lines) and `routing.py` (3,846 lines)
- **Technical debt** concentrated in core modules

### 🎯 Priority Recommendations
1. **HIGH**: Refactor `fastapi/dependencies/utils.py`
2. **HIGH**: Split `fastapi/applications.py` into smaller modules
3. **HIGH**: Refactor `fastapi/routing.py` architecture
4. **MEDIUM**: Implement continuous quality monitoring

## 🛠️ Tools Used

| Tool | Purpose | Output |
|------|---------|--------|
| **Radon** | Complexity & Maintainability | `cc.txt`, `mi.txt` |
| **Pygount** | Lines of Code | `sloc.txt` |
| **Git** | Change History Analysis | `git_numstat.log` |
| **Pytest** | Test Execution | Test results |
| **Python/Pandas** | Data Processing | `analysis_summary.json` |

## 📚 Documentation

- **[Complete Report](docs/Relatorio_GQM_FastAPI.md)** - Full GQM analysis with 7 sections
- **[Executive Summary](docs/Sumario_Executivo.md)** - Key findings and recommendations
- **[Delivery Checklist](docs/Checklist_Entrega.md)** - Validation and completeness check

## 🔄 Reproducibility

All analysis can be reproduced using the provided scripts:

```bash
cd fastapi
python scripts/collect_all_metrics.py  # Collect metrics
python scripts/analyze_metrics.py      # Process and analyze
```

The exact FastAPI version analyzed is documented in `data/version_info.txt`.

## 📊 Analyzed Version

- **FastAPI Version**: 0.118.0-26-g45bfb89ea
- **Commit Hash**: 45bfb89ea25fcbe8c44ac5d5657b147cfa074649
- **Analysis Date**: October 1, 2025
- **Repository**: https://github.com/tiangolo/fastapi

## 🤝 Contributing

This is an academic study repository. However, if you find issues or want to enhance the analysis:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions about this analysis or the GQM methodology applied:

- **Study Focus**: Software Quality Assessment using GQM
- **Framework Analyzed**: FastAPI (Python web framework)
- **Methodology**: Goal-Question-Metric approach
- **Academic Context**: UFJF Software Metrics Course (1322004)
- **Institution**: Federal University of Juiz de Fora - Computer Science Dept.

## 🙏 Acknowledgments

- **FastAPI Team** - For creating an excellent framework to analyze
- **Basili & Weiss** - For the GQM methodology
- **Prof. Leonardo Vieira dos Santos Reis** - Academic guidance and methodology supervision
- **UFJF Computer Science Department** - Educational support and resources
- **Open Source Community** - For the tools that made this analysis possible

---

**Note**: This is an independent quality analysis study. It is not affiliated with or endorsed by the FastAPI project maintainers.

---

## 🙏 Agradecimentos

- **Equipe FastAPI** - Por criar um excelente framework para analisar
- **Basili & Weiss** - Pela metodologia GQM
- **Prof. Leonardo Vieira dos Santos Reis** - Orientação acadêmica e supervisão metodológica
- **Departamento de Ciência da Computação UFJF** - Suporte educacional e recursos
- **Comunidade Open Source** - Pelas ferramentas que tornaram esta análise possível

---

**Nota**: Este é um estudo independente de análise de qualidade. Não é afiliado ou endossado pelos mantenedores do projeto FastAPI.