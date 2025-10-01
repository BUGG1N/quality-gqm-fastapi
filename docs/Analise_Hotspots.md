# 🔥 Análise de Hotspots - FastAPI

## Top 10 Arquivos Críticos (Churn × Complexidade × Manutenibilidade)

| Rank | Arquivo | Commits (12m) | Mudanças | CC Média | CC Máx | MI Score | Hotspot Score | Prioridade |
|------|---------|---------------|----------|-----------|---------|----------|---------------|------------|
| 1 | `dependencies/utils.py` | 52 | 1370 | 7.5 | 44 | 5.3 | 114237 | 🔴 ALTA |
| 2 | `routing.py` | 38 | 1000 | 4.2 | 28 | 19.9 | 9895 | 🔴 ALTA |
| 3 | `applications.py` | 45 | 1170 | 2.1 | 10 | 41.1 | 3957 | 🔴 ALTA |
| 4 | `encoders.py` | 22 | 460 | 10.5 | 37 | 49.2 | 2364 | 🔴 ALTA |
| 5 | `params.py` | 28 | 660 | 2.9 | 11 | 42.4 | 1708 | 🔴 ALTA |
| 6 | `exceptions.py` | 18 | 375 | 1.5 | 3 | 88.5 | 191 | 🟢 BAIXA |
| 7 | `concurrency.py` | 12 | 245 | 4.0 | 4 | 96.2 | 153 | 🟢 BAIXA |
| 8 | `datastructures.py` | 15 | 305 | 1.3 | 2 | 75.2 | 141 | 🟢 BAIXA |
| 9 | `security/__init__.py` | 25 | 520 | 0.0 | 0 | 100.0 | 130 | 🟢 BAIXA |
| 10 | `middleware/cors.py` | 20 | 400 | 0.0 | 0 | 100.0 | 80 | 🟢 BAIXA |

## 🎯 Interpretação dos Resultados

### Arquivo Mais Crítico: `fastapi/dependencies/utils.py`
- **52 commits** nos últimos 12 meses
- **1370 linhas alteradas** (alta instabilidade)
- **Complexidade média: 7.5** (máxima: 44)
- **Índice de Manutenibilidade: 5.3** (meta: ≥70)

### 🚨 Recomendações Prioritárias

1. **dependencies/utils.py**:
   - ⚠️ MI crítico (5.3) - Refatoração urgente
   - ⚠️ Alto churn (52 commits) - Instabilidade

2. **routing.py**:
   - ⚠️ MI crítico (19.9) - Refatoração urgente
   - ⚠️ Alto churn (38 commits) - Instabilidade

3. **applications.py**:
   - ⚠️ MI crítico (41.1) - Refatoração urgente
   - ⚠️ Alto churn (45 commits) - Instabilidade

## 📊 Metodologia de Cálculo

**Hotspot Score** = (Commits × Total_Mudanças × (CC_Média + 1)) / MI_Score

- **Commits**: Frequência de mudanças (instabilidade)
- **Total_Mudanças**: Linhas adicionadas + removidas
- **CC_Média**: Complexidade ciclomática média
- **MI_Score**: Índice de manutenibilidade (inverso - quanto menor, pior)

**Critérios de Prioridade:**
- 🔴 **ALTA**: Score > 1000 (refatoração urgente)
- 🟡 **MÉDIA**: Score 500-1000 (refatoração planejada)
- 🟢 **BAIXA**: Score < 500 (monitoramento)