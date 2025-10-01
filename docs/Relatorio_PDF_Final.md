# Relatório GQM - FastAPI Quality Analysis

**Universidade Federal de Juiz de Fora (UFJF)**  
**Especialização em Gerência de Projetos de Software na Era de Dados de Sensores e IA**  
**Disciplina: Métricas de Software (1322004)**  
**Professor: Leonardo Vieira dos Santos Reis**  
**Data: 2025-10-01**

---

## 1. Escolha do Software

**Software**: FastAPI | **Repositório**: https://github.com/tiangolo/fastapi  
**Versão**: 0.118.0-26-g45bfb89ea | **Commit**: 45bfb89ea25fc...

**Justificativa**: Framework Python moderno, 75k+ estrelas, ~15k SLOC, desenvolvimento ativo, adequado para análise GQM.

---

## 2. Objetivos

**G1 - Manutenibilidade**: Aprimorar código em módulos críticos (routing, dependencies, params)  
**G2 - Confiabilidade**: Melhorar estabilidade através de análise de testes e bugs

---

## 3. Questões e Métricas

### G1 - Manutenibilidade

| Questão | Métrica | Unidade | Ferramenta | Meta | Resultado |
|---------|---------|---------|------------|------|-----------|
| Q1.1: Complexidade? | CC Média/Máxima | Número | Radon | ≤10/≤15 | **4.8/10** ✅ |
| Q1.2: Manutenibilidade? | Índice MI | 0-100 | Radon | ≥70 | **81.56** ✅ |
| Q1.3: Tamanho arquivos? | SLOC | Linhas | Pygount | <500 | **14,695** total |
| Q1.4: Frequência mudanças? | Git Churn | Commits | Git | Monitor | **52** max |

### G2 - Confiabilidade  

| Questão | Métrica | Unidade | Ferramenta | Meta | Resultado |
|---------|---------|---------|------------|------|-----------|
| Q2.1: Densidade bugs? | Bugs/KLOC | Bugs/1000 | GitHub CLI | ≤1.0 | **0.7** ✅ |
| Q2.2: Tempo resolução? | MTTR | Dias | GitHub CLI | ≤30 | **~15** ✅ |
| Q2.3: Cobertura testes? | Coverage | % | pytest-cov | ≥80% | **99%** ✅ |
| Q2.4: Estabilidade CI? | Pipeline Success | % | GitHub API | ≥95% | **~97%** ✅ |

---

## 4. Extração das Métricas

**Comandos Executados**:
```bash
radon cc -s -a fastapi/ > data/cc.txt          # Complexidade (376 linhas)
radon mi -s fastapi/ > data/mi.txt             # Manutenibilidade (46 arquivos)  
pygount --format=json fastapi/ > data/sloc.json # SLOC (14,695 linhas)
git log --since="12 months ago" --numstat > data/git_numstat.log
bash scripts/test-cov-html.sh                 # Cobertura 99%
```

**Evidências**: ✅ data/cc.txt, mi.txt, sloc.json, analysis_summary.json, hotspots_analysis.json

---

## 5. Análise dos Resultados

### 🔥 Top 5 Hotspots Críticos

| Arquivo | Commits | CC | MI | Score | Prioridade |
|---------|---------|----|----|-------|------------|
| `dependencies/utils.py` | 52 | 5.2 | **5.29** | 114,237 | 🔴 **CRÍTICA** |
| `routing.py` | 38 | 4.8 | 73.45 | 9,895 | 🔴 **ALTA** |
| `applications.py` | 45 | 3.2 | **41.07** | 3,957 | 🟡 **MÉDIA** |
| `encoders.py` | 22 | 2.1 | **49.23** | 2,364 | 🟡 **MÉDIA** |
| `params.py` | 28 | 1.8 | **42.37** | 1,708 | 🟡 **MÉDIA** |

### Interpretação por Objetivo

**G1 - Manutenibilidade**: ✅ **BOM** (MI=81.56) com 1 hotspot crítico  
- 89% arquivos atendem padrões (≥70)
- **CRÍTICO**: dependencies/utils.py (MI=5.29) precisa refatoração urgente
- Arquivos grandes: applications.py (4,043 linhas), routing.py (3,846 linhas)

**G2 - Confiabilidade**: ✅ **EXCELENTE**  
- Cobertura 99% (meta ≥80%)
- Densidade bugs 0.7/KLOC (meta ≤1.0)  
- MTTR 15 dias (meta ≤30)
- Pipeline 97% sucesso (meta ≥95%)

---

## 6. Recomendações

### 🚨 URGENTE (2 semanas)
1. **Refatorar dependencies/utils.py** - MI crítico (5.29), extrair funções menores

### 🔴 ALTA (1 mês)  
2. **Modularizar applications.py** - 4,043 linhas, dividir em módulos especializados
3. **Refatorar routing.py** - 3,846 linhas + alto churn, simplificar lógica

### 🟡 MÉDIA (3 meses)
4. **Melhorar arquivos MI 40-70** - params.py, encoders.py  
5. **Monitoramento contínuo** - métricas no CI/CD, alertas qualidade

---

## 7. Conclusão

FastAPI demonstra **qualidade geral excelente** (MI: 81.56) e **confiabilidade excepcional** (99% cobertura, 0.7 bugs/KLOC). A metodologia GQM foi eficaz para identificar hotspots específicos.

**Principais Aprendizados**:
- Cruzamento métricas (churn × complexidade × MI) revela prioridades claras
- Framework mantém alta qualidade apesar do crescimento rápido  
- Hotspot crítico concentrado em 1 arquivo específico

**Impacto**: Refatoração do hotspot crítico reduzirá riscos de manutenção significativamente.

---

**Rastreabilidade**: Commit 45bfb89ea | Python 3.13.7 | Radon 6.0.1+ | 2025-10-01  
**Repositório do Estudo**: https://github.com/BUGG1N/quality-gqm-fastapi