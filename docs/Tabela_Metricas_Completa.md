# Tabela de Métricas Completa - FastAPI GQM Quality Analysis

## Estrutura Goal-Question-Metric Detalhada

### G1 - Melhorar Manutenibilidade
**Objetivo**: Aprimorar a manutenibilidade do código em módulos críticos (routing, parameters, dependency injection)

#### Q1.1: Qual é a complexidade ciclomática dos módulos críticos?
| Métrica | Unidade | Fonte | Ferramenta | Meta |
|---------|---------|-------|------------|------|
| Complexidade Ciclomática Média | Número | Código fonte Python | Radon | ≤ 10 |
| Complexidade Ciclomática Máxima | Número | Código fonte Python | Radon | ≤ 15 |

#### Q1.2: Qual é o índice de manutenibilidade dos arquivos?
| Métrica | Unidade | Fonte | Ferramenta | Meta |
|---------|---------|-------|------------|------|
| Índice de Manutenibilidade (MI) | Escala 0-100 | Código fonte Python | Radon | ≥ 70 |
| Arquivos com MI Crítico | Quantidade | Código fonte Python | Radon | 0 |

#### Q1.3: Qual o tamanho dos arquivos fonte?
| Métrica | Unidade | Fonte | Ferramenta | Meta |
|---------|---------|-------|------------|------|
| Linhas de Código (SLOC) | Linhas | Código fonte Python | Pygount | < 500/arquivo |
| Arquivos Grandes (>1000 linhas) | Quantidade | Código fonte Python | Pygount | ≤ 5 |

#### Q1.4: Qual a frequência de mudanças (churn) nos módulos?
| Métrica | Unidade | Fonte | Ferramenta | Meta |
|---------|---------|-------|------------|------|
| Git Churn (12 meses) | Commits/arquivo | Histórico Git | Git log | Monitor |
| Arquivos com Alto Churn | Quantidade | Histórico Git | Git log | Monitor |

### G2 - Aumentar Confiabilidade
**Objetivo**: Melhorar a estabilidade e reduzir a ocorrência de defeitos através de testes e análise de bugs

#### Q2.1: Qual a densidade de bugs no sistema?
| Métrica | Unidade | Fonte | Ferramenta | Meta |
|---------|---------|-------|------------|------|
| Bugs por KLOC | Bugs/1000 linhas | GitHub Issues | GitHub CLI | ≤ 1.0 |
| Bugs Abertos | Quantidade | GitHub Issues | GitHub CLI | Monitor |

#### Q2.2: Qual o tempo de resolução de bugs (MTTR)?
| Métrica | Unidade | Fonte | Ferramenta | Meta |
|---------|---------|-------|------------|------|
| MTTR (Mean Time to Repair) | Dias | GitHub Issues | GitHub CLI | ≤ 30 |
| Bugs Críticos Pendentes | Quantidade | GitHub Issues | GitHub CLI | 0 |

#### Q2.3: Qual a cobertura de testes do sistema?
| Métrica | Unidade | Fonte | Ferramenta | Meta |
|---------|---------|-------|------------|------|
| Cobertura de Testes | Porcentagem (%) | Relatório de Testes | pytest-cov | ≥ 80% |
| Testes Passando | Porcentagem (%) | CI/CD Pipeline | pytest | 100% |

#### Q2.4: Qual a estabilidade do pipeline de CI/CD?
| Métrica | Unidade | Fonte | Ferramenta | Meta |
|---------|---------|-------|------------|------|
| Taxa de Sucesso do Pipeline | Porcentagem (%) | GitHub Actions | GitHub API | ≥ 95% |
| Falhas de Build | Quantidade/mês | GitHub Actions | GitHub API | ≤ 5 |

## Ferramentas Utilizadas - Versões

| Ferramenta | Versão | Comando de Verificação |
|------------|---------|----------------------|
| Python | 3.13.7 | `python --version` |
| Radon | 6.0.1+ | `radon --version` |
| Pygount | 1.6.1+ | `pygount --version` |
| pytest-cov | 4.1.0+ | `pytest --version` |
| Git | 2.40+ | `git --version` |
| GitHub CLI | 2.0+ | `gh --version` |

## Comandos de Coleta

```bash
# Complexidade Ciclomática
radon cc -s -a fastapi/ > data/cc.txt

# Índice de Manutenibilidade  
radon mi -s fastapi/ > data/mi.txt

# Linhas de Código
pygount --format=json fastapi/ > data/sloc.json
pygount --format=summary fastapi/ > data/sloc.txt

# Churn Analysis (12 meses)
git log --since="12 months ago" --numstat --date=iso \
  --pretty=format:"%H;%ad;%an;%s" > data/git_numstat.log

# Bugs e Issues
gh issue list --label bug --limit 300 \
  --json number,title,createdAt,closedAt \
  --repo tiangolo/fastapi > data/issues_bug.json

# Cobertura de Testes
bash scripts/test-cov-html.sh

# Pipeline Status (se disponível)
gh run list --limit 100 --json status,conclusion \
  --repo tiangolo/fastapi > data/pipeline_status.json
```

## Rastreabilidade

- **Repositório Analisado**: https://github.com/tiangolo/fastapi
- **Commit Hash**: 45bfb89ea25fcbe8c44ac5d5657b147cfa074649
- **Versão**: 0.118.0-26-g45bfb89ea
- **Data da Análise**: 2025-10-01
- **Ambiente**: Windows 11, PowerShell 5.1
- **Repositório do Estudo**: https://github.com/BUGG1N/quality-gqm-fastapi