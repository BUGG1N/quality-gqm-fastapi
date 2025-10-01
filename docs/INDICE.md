# 📋 Índice de Documentação - FastAPI GQM Quality Analysis

> **Guia de navegação para todos os documentos e entregáveis do projeto**

## 🎯 **Documentos Principais (Para Entrega)**

### 📄 **1. Relatório Principal**
**Arquivo**: [`docs/Relatorio_Principal.md`](Relatorio_Principal.md)  
**Descrição**: Relatório GQM completo e detalhado com as 7 seções exigidas  
**Uso**: Versão completa para leitura e avaliação acadêmica  
**Tamanho**: ~8 páginas (versão detalhada)

### 📄 **2. Relatório para PDF**
**Arquivo**: [`docs/Relatorio_GQM_Completo.md`](Relatorio_GQM_Completo.md)  
**Descrição**: Versão concisa e otimizada para conversão em PDF  
**Uso**: **ENTREGA OFICIAL** - formato ≤5 páginas conforme enunciado  
**Conversão**: `pandoc Relatorio_GQM_Completo.md -o relatorio.pdf`

## 🔥 **Análises Específicas**

### 📊 **3. Análise de Hotspots**
**Arquivo**: [`docs/Analise_Hotspots.md`](Analise_Hotspots.md)  
**Descrição**: Top 10 arquivos críticos identificados (Churn × Complexidade × Manutenibilidade)  
**Uso**: Priorização de refatoração e melhorias  
**Destaques**: dependencies/utils.py como hotspot crítico

### 📋 **4. Tabela de Métricas Completa**
**Arquivo**: [`docs/Tabela_Metricas_Completa.md`](Tabela_Metricas_Completa.md)  
**Descrição**: Especificação detalhada de todas as 16 métricas utilizadas  
**Uso**: Referência técnica (unidade, fonte, ferramenta, comando)  

### 🔍 **5. Rastreabilidade Completa**
**Arquivo**: [`docs/Rastreabilidade_Completa.md`](Rastreabilidade_Completa.md)  
**Descrição**: Documentação completa de reprodutibilidade  
**Uso**: Validação e replicação do estudo  
**Inclui**: Versões, comandos, checksums, instruções passo-a-passo

## 📝 **Documentos de Apoio**

### 📊 **6. Resumo Executivo**
**Arquivo**: [`docs/Sumario_Executivo.md`](Sumario_Executivo.md)  
**Descrição**: Síntese das principais descobertas e recomendações  
**Uso**: Apresentações e resumos gerenciais  

### ✅ **7. Checklist de Entrega**
**Arquivo**: [`docs/Checklist_Entrega.md`](Checklist_Entrega.md)  
**Descrição**: Lista de verificação de completude do trabalho  
**Uso**: Validação antes da entrega  

## 🤖 **Scripts e Automação**

### 🔧 **Script Principal**
**Arquivo**: [`scripts/collect_all_metrics.py`](../scripts/collect_all_metrics.py)  
**Descrição**: Coleta automatizada completa de todas as métricas  
**Uso**: `python scripts/collect_all_metrics.py`  
**Saída**: Arquivos em `data/` + execução de análises

### 📊 **Análise de Hotspots**  
**Arquivo**: [`scripts/analyze_hotspots.py`](../scripts/analyze_hotspots.py)  
**Descrição**: Identifica e ranqueia arquivos críticos  
**Uso**: Executado automaticamente pelo script principal

### 🔬 **Análise de Métricas**
**Arquivo**: [`scripts/analyze_metrics.py`](../scripts/analyze_metrics.py)  
**Descrição**: Processa dados coletados e gera insights  
**Uso**: Executado automaticamente pelo script principal

## 📊 **Dados e Resultados**

### Arquivos em `data/`:
- `analysis_summary.json` - Resultados processados finais
- `hotspots_analysis.json` - Ranking de hotspots 
- `mi.txt` - Índice de manutenibilidade (Radon)
- `cc.txt` - Complexidade ciclomática (Radon)  
- `sloc.json` - Linhas de código (Pygount)
- `version_info.txt` - Informações da versão analisada

## 🎯 **Fluxo de Uso Recomendado**

### **Para Avaliação Acadêmica:**
1. 📄 Ler [`Relatorio_Principal.md`](Relatorio_Principal.md) (versão completa)
2. 📄 Converter [`Relatorio_GQM_Completo.md`](Relatorio_GQM_Completo.md) para PDF (entrega)
3. 🔍 Consultar [`Rastreabilidade_Completa.md`](Rastreabilidade_Completa.md) para validação

### **Para Reprodução do Estudo:**
1. 🔧 Executar `python scripts/collect_all_metrics.py`
2. 📊 Consultar [`Tabela_Metricas_Completa.md`](Tabela_Metricas_Completa.md) para detalhes técnicos
3. 🔍 Seguir [`Rastreabilidade_Completa.md`](Rastreabilidade_Completa.md) para setup

### **Para Análise Técnica:**
1. 🔥 Revisar [`Analise_Hotspots.md`](Analise_Hotspots.md) para prioridades
2. 📊 Examinar arquivos em `data/` para dados brutos
3. 📝 Consultar [`Sumario_Executivo.md`](Sumario_Executivo.md) para insights

## ✅ **Status da Documentação**

| Documento | Status | Atualizado | Completo |
|-----------|---------|------------|----------|
| Relatório Principal | ✅ | 2025-10-01 | 100% |
| Relatório GQM Completo | ✅ | 2025-10-01 | 100% |
| Análise de Hotspots | ✅ | 2025-10-01 | 100% |
| Tabela de Métricas | ✅ | 2025-10-01 | 100% |
| Rastreabilidade | ✅ | 2025-10-01 | 100% |
| Resumo Executivo | ✅ | 2025-10-01 | 100% |
| Checklist Entrega | ✅ | 2025-10-01 | 100% |

---

**Última atualização**: 2025-10-01  
**Repositório**: https://github.com/BUGG1N/quality-gqm-fastapi