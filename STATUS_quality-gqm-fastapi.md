
# Status de Entrega — `quality-gqm-fastapi` × Enunciado (GQM)

> Repositório: https://github.com/BUGG1N/quality-gqm-fastapi  
> Contexto: avaliar **o que foi alcançado**, **o que falta** e **melhorias** para atender **100%** ao enunciado do trabalho (PDF anexo). fileciteturn1file0

> ⚠️ **Nota de acesso**: não consegui abrir o repositório pelo navegador embutido aqui (limitação técnica de acesso/caching). Vou entregar abaixo um **checklist objetivo + plano de correção** alinhado ao enunciado e ao plano que preparamos para o **FastAPI**, de modo que você possa marcar rapidamente **feito / faltando**. Se puder tornar o repo público ou enviar um `.zip`, eu atualizo este status com evidências concretas (hash, caminhos e arquivos).

---

## 1) Matriz de conformidade com o enunciado

| Item do enunciado | Evidência esperada no repo | Status | Observações / Ação de correção |
|---|---|---|---|
| **1. Escolha do software** | README ou seção inicial do relatório citando **FastAPI (tiangolo/fastapi)**, link do repositório e dados gerais | A confirmar | Incluir **justificativa** (popularidade, linguagem, tamanho, ecossistema) |
| **2. Objetivos (≥2)** | Seção **Objetivos (G)** com foco em **Manutenibilidade** e **Confiabilidade** | A confirmar | Objetivos claros, mensuráveis, com contexto (p.ex.: reduzir hotspots) |
| **3. Questões por objetivo (≥2/Q)** | Tabelas **G→Q** (por ex.: CC/MI, duplicação, churn; bugs/KLOC, MTTR, cobertura) | A confirmar | Cada Q deve apontar para **métricas** específicas |
| **4. Métricas por questão** | Para **cada** métrica: **nome, descrição, unidade, fonte, ferramenta** | A confirmar | Colocar unidade (%, dias, linhas, bugs/KLOC), **fonte** (código/CI/issues), **ferramenta** (Radon/cloc/gh/Sonar) |
| **5. Extração das métricas** | Resultados gerados em `data/` (`cc.txt`, `mi.txt`, `sloc.csv`, `issues_bug.json`, `prs.json`, prints Sonar) | A confirmar | Salvar comandos em `scripts/collect_metrics.sh` ou `Makefile` |
| **6. Análise dos resultados** | Seção **Análise** conectando números às **Questões** e **Objetivos**; “Top5 hotspots” | A confirmar | **Interpretar**: ex.: “`routing.py` alta CC + alto churn ⇒ priorizar refatoração e testes” |
| **7. Conclusão** | Síntese do que foi aprendido + **recomendações** priorizadas | A confirmar | 3–5 recomendações acionáveis (refatorar módulos X/Y; aumentar cobertura) |
| **PDF ≤ 5 páginas** | `docs/relatorio.pdf` (≤5 págs) com as 7 seções | A confirmar | Objetivo é conciso e direto (gráficos legíveis) |
| **Rastreabilidade e reprodução** | Hash do commit, versões de ferramentas, passos de execução | A confirmar | Registrar `git rev-parse HEAD`, `python --version`, etc. |

> Critérios retirados do **enunciado oficial** (itens 1–7 e formato do PDF). fileciteturn1file0

---

## 2) O que provavelmente **já foi alcançado** (com base no plano FastAPI anterior)
- Seleção do software (**FastAPI**) e justificativa técnica.  
- Definição de **G1 Manutenibilidade** e **G2 Confiabilidade**, com **Q** correspondentes.  
- Lista de **métricas** (CC/MI, duplicação, churn; bugs/KLOC, MTTR, cobertura; falhas de pipeline).  
- **Comandos de coleta** prontos (Radon, `cloc`, `gh`, `pytest`/coverage, Sonar opcional).  
- **Estrutura de pastas** proposta (`data/`, `img/`, `scripts/`).

> Se essas partes já estiverem no repo, marque “Conforme” na Matriz e siga para as correções abaixo.

---

## 3) O que **falta** (ou costuma faltar) para **100%** e **como fechar**

1) **Unidades e fontes em TODAS as métricas**  
- ✅ Especificar *unidade*, *fonte* (código/CI/issues/PRs) e *ferramenta* (Radon/cloc/gh/Sonar).  
- ✅ Ex.: “Cobertura — **%** — Fonte: relatório de testes — Ferramenta: `scripts/test-cov-html.sh`/`pytest-cov`”.

2) **Evidência de extração** (arquivos em `data/` e prints)  
- ✅ `data/cc.txt`, `data/mi.txt`, `data/sloc.csv`, `data/issues_bug.json`, `data/prs.json`.  
- ✅ Prints/relatórios do Sonar (se usar), armazenados em `img/`.  

3) **Análise conectando número → decisão**  
- ✅ Cruzar **churn × complexidade** para criar “Top 5 hotspots”.  
- ✅ Interpretar duplicação/smells no contexto dos módulos de **roteamento/DI/params** do FastAPI.  
- ✅ Concluir com **ações** (refatorar módulo X; extrair função Y; criar teste Z).

4) **Rastreabilidade**  
- ✅ Registrar **hash** do commit analisado e **versões** das ferramentas (Python, Radon, cloc, gh).

5) **PDF enxuto (≤5 págs)** cobrindo **todas** as seções  
- ✅ Tabelas compactas (G→Q→M), 1–2 gráficos; fonte legível; sem apêndices extensos no PDF (use pasta `data/`).

---

## 4) Plano de correção (passo a passo rápido)

```bash
# 0) Preparar ambiente (Linux/macOS; ajuste no Windows)
python -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip radon pytest pytest-cov
# cloc: sudo apt-get install -y cloc  (ou 'pipx install scc')
# gh CLI: https://cli.github.com/

# 1) Coleta de métricas de código (ajuste o caminho se necessário)
mkdir -p data img
radon cc -s -a fastapi/ > data/cc.txt
radon mi -s fastapi/ > data/mi.txt
cloc fastapi/ --by-file --csv --out=data/sloc.csv

# 2) Churn (12 meses) para hotspots
git log --since="12 months ago" --numstat --date=iso \
  --pretty=format:"%H;%ad;%an;%s" > data/git_numstat.log

# 3) Bugs/KLOC e MTTR
gh issue list --label bug --limit 300 \
  --json number,title,createdAt,closedAt \
  --repo tiangolo/fastapi > data/issues_bug.json

# 4) Testes e cobertura (suíte do projeto)
bash scripts/test-cov-html.sh  # gera ./htmlcov/index.html

# 5) (Opcional) Duplicação e smells
# docker run -d --name sonarqube -p 9000:9000 sonarqube:lts-community
# sonar-scanner ... (salvar prints em img/)
```

**Preencher no relatório:** unidade/fonte/ferramenta de cada métrica, interpretar resultados e listar **recomendações priorizadas**.

---

## 5) Modelo de “Resultados & Análise” (preencher com os seus números)

> **Hotspots (churn × CC)** — priorizar refatoração/testes

| Arquivo | CC média/máx | Churn (12m) | Observação |
|---|---:|---:|---|
| fastapi/routing.py |  |  |  |
| fastapi/dependencies/utils.py |  |  |  |
| fastapi/applications.py |  |  |  |

> **Confiabilidade**

| Métrica | Valor | Interpretação |
|---|---:|---|
| Bugs/KLOC |  | (tendência/risco) |
| MTTR (dias) |  | (processo/fluxo) |
| Cobertura (%) |  | (alvos críticos/testes ausentes) |

---

## 6) Melhorias sugeridas (além do mínimo do enunciado)

- **Automatizar** a coleta em `scripts/collect_metrics.sh` ou `Makefile`.  
- **Gráfico** simples (barras) para CC média por módulo e churn (últimos 12m).  
- **Checklist de excelência** no README: hash, versões, como reproduzir, links para `data/`/`img/`/`htmlcov`.  
- **Hipóteses e ameaças à validade** (escopo do recorte, falta de cobertura/CI).  
- **Roadmap curto** (ex.: sprint de refatoração dos 3 maiores hotspots).

---

## 7) Checklist final (entrega)

- [ ] PDF **≤ 5 páginas** com as 7 seções do enunciado. fileciteturn1file0  
- [ ] **Hash** do commit analisado e **versões** das ferramentas.  
- [ ] Tabelas **G→Q→M** com **unidade, fonte, ferramenta**.  
- [ ] **Resultados** (arquivos em `data/`) + prints (em `img/`).  
- [ ] **Análise** respondendo às questões e gerando recomendações.  
- [ ] **Conclusão** clara e objetiva.  

---

> **Como prossigo se você quiser que eu preencha tudo com evidências reais?**  
> Basta tornar o repo público ou enviar um `.zip`. Aí eu **substituo os “A confirmar” por provas** (caminhos, trechos e números) e já **anexo** um `relatorio.pdf` ≤ 5 págs com os gráficos e as referências.
