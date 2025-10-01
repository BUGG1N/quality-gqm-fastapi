# FastAPI GQM Quality Analysis

> **Goal-Question-Metric (GQM) methodology applied to FastAPI framework for software quality assessment**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.118.0-009688.svg)](https://fastapi.tiangolo.com)
[![GQM](https://img.shields.io/badge/Methodology-GQM-orange.svg)](https://en.wikipedia.org/wiki/GQM)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

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