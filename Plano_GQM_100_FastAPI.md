
# Plano de Escopo e Entrega — **GQM** no projeto **FastAPI** (tiangolo/fastapi)

> **Repositório-alvo:** https://github.com/tiangolo/fastapi  
> **Linguagem:** Python (3.8+)  
> **Contexto:** Framework web assíncrono de alta performance. Projeto **muito popular**, com amplo histórico de *issues/PRs* e suíte de testes robusta ― ideal para aplicar **Goal–Question–Metric (GQM)** visando **nota máxima (100)**.

---

## 0) TL;DR — clonar, preparar ambiente e rodar testes/coverage

```bash
# 1) Clonar o repositório oficial
git clone https://github.com/tiangolo/fastapi
cd fastapi

# 2) Criar e ativar ambiente virtual (venv)
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows (PowerShell):
# .\.venv\Scripts\Activate.ps1

# 3) Instalar dependências de desenvolvimento (usa requirements.txt do repo)
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4) Rodar testes com cobertura (script oficial)
bash scripts/test-cov-html.sh

# 5) (Opcional) Abrir relatório de cobertura HTML
# arquivo gerado em: ./htmlcov/index.html

# 6) (Opcional) Padronizar código/formatação (script oficial)
bash scripts/format.sh
```

> Observação: o `requirements.txt` do próprio repositório instala a versão local do FastAPI em **modo editável (-e)**, permitindo alterar o código e reexecutar testes sem reinstalar.

---

## 1) Escopo do trabalho

**Incluído**  
- Aplicação integral do **GQM** com **2 objetivos** principais, ≥ **2 questões** por objetivo e **métricas quantitativas** por questão.  
- Foco em módulos **centrais** do FastAPI (ex.: `fastapi/routing.py`, `fastapi/applications.py`, `fastapi/dependencies/`, `fastapi/params.py`, `fastapi/responses.py`).  
- Coleta **automatizada** de métricas (Radon, `cloc`, GitHub CLI, SonarQube/SonarCloud opcional).  
- **Análise crítica** que conecta números a riscos/decisões e recomendações priorizadas.  
- Relatório final **PDF (≤ 5 páginas)** com as 7 seções do enunciado.

**Excluído**  
- Alterar comportamento público do framework (apenas recomendações).  
- Benchmarking de *performance* (fora do escopo ― foco em métricas de qualidade/manutenibilidade/confiabilidade).

---

## 2) Objetivos, Questões e Métricas (GQM) — **adaptado ao FastAPI**

### **G1 — Melhorar a _manutenibilidade_** em módulos críticos (roteamento, params, DI)

| Q | Métrica | Descrição | Unidade | Fonte | Ferramenta | Alvo/limite |
|---|---|---|---|---|---|---|
| **Q1.1** Quais funções/módulos têm **complexidade** elevada? | **Complexidade ciclomática (CC)** média/máx por função | Nº de caminhos independentes | valor | Código (`fastapi/`) | **Radon** | CC média ≤ 10; máx ≤ 20 |
|  | **Índice de Manutenibilidade (MI)** por arquivo | Composto (Halstead, CC, SLOC) | 0–100 | Código | **Radon** | MI ≥ 70 |
| **Q1.2** Há **duplicação** entre utilitários/roteamento? | **% Linhas duplicadas** | Linhas duplicadas/total | % | Código | **SonarQube/CodeClimate** | ≤ 5–10% |
| **Q1.3** Onde estão os **hotspots** (churn × complexidade)? | **Churn** por arquivo + CC | Linhas alteradas × CC | linhas/semana | Git + Código | `git log` + Radon | Top 5 arquivos priorizados |
| **Q1.4** Há **smells/lints** relevantes? | **Smells/Lints por KLOC** | Alertas estáticos | smells/KLOC | Código | Linters/Sonar | Tendência de queda |

### **G2 — Aumentar a _confiabilidade_** (bugs, testes, pipeline)

| Q | Métrica | Descrição | Unidade | Fonte | Ferramenta | Alvo/limite |
|---|---|---|---|---|---|---|
| **Q2.1** Qual a **densidade de defeitos**? | **Defect Density** | Issues com *bug* / KLOC | bugs/KLOC | Issues + SLOC | GitHub API + `cloc` | Tendência de queda |
| **Q2.2** Tempo para corrigir **bugs**? | **MTTR de bugs** | Abertura→fechamento | dias | Issues | GitHub API | ≤ 14 dias (ex.) |
| **Q2.3** Qual a **cobertura de testes**? | **Cobertura** | Linhas cobertas/total | % | CI/Relatórios | `scripts/test-cov-html.sh` (pytest) / Sonar | ≥ 60–80% |
| **Q2.4** O **pipeline** é estável? | **Falhas de pipeline** | Builds com falha / total | % | CI | Histórico CI | ≤ 10% |

> Ajuste limiares ao contexto e **justifique** no relatório.

---

## 3) Entregáveis (escopo de entrega)

1. **Relatório PDF (≤ 5 págs)** com as 7 seções do enunciado.  
2. **Apêndice (opcional)**: prints/tabelas de métricas e gráficos (se permitido).  
3. **Pacote de reprodutibilidade (recomendado)**:  
   - `scripts/collect_metrics.sh` / `Makefile` com os comandos abaixo;  
   - CSVs/imagens (`data/`, `img/`);  
   - `README.md` com passos para reproduzir.

---

## 4) Planejamento e cronograma (D0 = entrega)

| Janela | Atividades e Saídas | Excelência (nota 100) |
|---|---|---|
| **D-14 a D-12** | Clonar repo, criar **venv**, instalar via `requirements.txt`, registrar **hash** analisado; justificativa (½ pág). | Destacar popularidade/uso amplo do FastAPI e impacto. |
| **D-11 a D-9** | Rascunhar **G** e **Q** (Seção 2) focando módulos críticos. | Mapear riscos (ex.: DI/roteamento/validação). |
| **D-8 a D-6** | Definir **M** com **unidade, fonte e ferramenta**; preparar ambiente (Radon, cloc, gh). | Preferir coleta **automatizada** e comparável (por módulo). |
| **D-5 a D-4** | **Coleta**: Radon (CC/MI), `cloc` (SLOC), churn (`git log`), *issues/PRs* (GitHub API), cobertura (`scripts/test-cov-html.sh`). | Salvar versões e **hash**. |
| **D-3** | **Análise** com tabelas/gráficos; responder Q por G; priorizar hotspots. | Cruzar churn × CC; interpretar smells no contexto. |
| **D-2** | **Redação** do PDF (≤ 5 págs). | Figuras legíveis, unidades claras. |
| **D-1** | **Revisão** + checklist final. | Garantir rastreabilidade **G→Q→M**. |
| **D0** | Submissão do PDF + pacote de reprodutibilidade. | Checklist (Seção 8). |

---

## 5) Coleta prática — comandos (ajuste caminhos se necessário)

> A raiz de código é `fastapi/`. Gere uma pasta `data/` e `img/` para organizar saídas.

**5.1 Complexidade e Manutenibilidade (Radon)**
```bash
pip install radon
mkdir -p data img
# complexidade por função e média (-a)
radon cc -s -a fastapi/ > data/cc.txt
# índice de manutenibilidade por arquivo
radon mi -s fastapi/ > data/mi.txt
```

**5.2 Tamanho (SLOC) por arquivo e total**
```bash
# Linux (ex. Ubuntu/Debian) — ou use 'pipx install scc'
sudo apt-get install -y cloc
cloc fastapi/ --by-file --csv --out=data/sloc.csv
```

**5.3 Churn do repositório (últimos 12 meses)**
```bash
git log --since="12 months ago" --numstat --date=iso \
  --pretty=format:"%H;%ad;%an;%s" > data/git_numstat.log
# processe em Python para somar adições/remoções por arquivo/semana
```

**5.4 Duplicação e Smells (SonarQube opcional)**
```bash
# subir SonarQube (LTS) localmente
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts-community
# configurar sonar-scanner para Python e analisar o diretório do projeto
# salve prints/relatório em img/ e docs/
```

**5.5 Issues/PRs (GitHub CLI) — Defect Density, MTTR e produtividade**
```bash
# instalar gh: https://cli.github.com/
# bugs para densidade e MTTR
gh issue list --label bug --limit 300 \
  --json number,title,createdAt,closedAt \
  --repo tiangolo/fastapi > data/issues_bug.json

# PRs (lead time e tamanho, se quiser G3 produtividade)
gh pr list --state merged --limit 300 \
  --json number,createdAt,mergedAt,additions,deletions \
  --repo tiangolo/fastapi > data/prs.json
```

**5.6 Testes e cobertura (oficial do repo)**
```bash
# executa toda a suíte e gera cobertura HTML em ./htmlcov
bash scripts/test-cov-html.sh

# (Alternativo) rodar pytest direto
pytest -q
```

**5.7 Registrar versão/recorte analisado**
```bash
git rev-parse HEAD
git describe --tags --always
```

---

## 6) Estrutura de pastas sugerida (reprodutibilidade)
```
fastapi/
  data/       # CSVs dos resultados (sloc, churn, issues, etc.)
  img/        # prints de Sonar e gráficos
  scripts/    # scripts de coleta e análise (opcional)
  docs/       # rascunhos auxiliares (não confundir com docs do projeto)
```

Exemplo de script (`scripts/collect_metrics.sh`):
```bash
#!/usr/bin/env bash
set -e
mkdir -p data img
radon cc -s -a fastapi/ > data/cc.txt
radon mi -s fastapi/ > data/mi.txt
cloc fastapi/ --by-file --csv --out=data/sloc.csv
git log --since="12 months ago" --numstat --date=iso \
  --pretty=format:"%H;%ad;%an;%s" > data/git_numstat.log
gh issue list --label bug --limit 300 \
  --json number,title,createdAt,closedAt --repo tiangolo/fastapi \
  > data/issues_bug.json || true
```

---

## 7) Estrutura do relatório (≤ 5 páginas)
1. **Introdução** — contexto do FastAPI e objetivo GQM.  
2. **Escolha do software** — relevância, atividade e **hash** analisado.  
3. **Objetivos (G)** — G1 manutenibilidade; G2 confiabilidade.  
4. **Questões (Q)** — ≥ 2 por objetivo (ver Tabelas G1/G2).  
5. **Métricas (M)** — nome, descrição, unidade, fonte, ferramenta.  
6. **Extração e resultados** — evidências (tabelas/prints).  
7. **Análise e discussão** — interpretação por objetivo; hotspots; recomendações.  
8. **Conclusão** — síntese e próximos passos.  

---

## 8) Checklist de excelência (antes de enviar)

- [ ] PDF ≤ 5 págs com **todas as 7 seções**.  
- [ ] **Hash** registrado.  
- [ ] **G → Q → M** coerentes e rastreáveis.  
- [ ] Métricas com **unidade, fonte e ferramenta** explícitas.  
- [ ] Tabelas/figuras com **títulos e unidades**.  
- [ ] Análise que **responde às questões** e gera **recomendações** práticas.  
- [ ] Versões de ferramentas registradas; scripts e dados em `scripts/`, `data/`, `img/`.  
- [ ] Referências normalizadas (NBR/APA/ACM, conforme exigência).

---

## 9) Bibliografia focal (uso recomendado)

- **Fenton & Bieman.** *Software Metrics: A Rigorous and Practical Approach (3ª ed.)*.  
- **Lanza; Marinescu; Ducasse.** *Object-Oriented Metrics in Practice*.  
- **Nicolette.** *Software Development Metrics*.  
- **IEEE 1061:1998** — metodologia de métricas de qualidade.  
- **ISO/IEC 25010:2011** — modelo de qualidade de produto.

---

### Observações finais
- O script `scripts/test-cov-html.sh` executa a suíte de testes e gera o HTML de cobertura em `./htmlcov/`.  
- O script `scripts/format.sh` formata e organiza *imports* do código.  
- Se decidir incluir **G3 Produtividade**, meça *lead time* e tamanho médio de PRs a partir de `data/prs.json`.
