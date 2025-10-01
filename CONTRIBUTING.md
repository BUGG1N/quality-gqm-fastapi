# Contributing to FastAPI GQM Quality Analysis

Thank you for your interest in contributing to this software quality analysis study!

## 📋 Overview

This repository contains an academic study applying the Goal-Question-Metric (GQM) methodology to analyze the FastAPI framework. This work is part of the **Software Metrics course (Code: 1322004)** at the **Federal University of Juiz de Fora (UFJF)**, under the **Software Project Management Specialization in the Era of Sensor Data and AI** program, supervised by **Prof. Leonardo Vieira dos Santos Reis**.

While the primary purpose is educational and research-oriented, we welcome contributions that enhance the analysis or methodology.

## 🤝 How to Contribute

### Types of Contributions Welcome

1. **Analysis Improvements**
   - Better data visualization
   - Additional metrics collection
   - Enhanced statistical analysis
   - Bug fixes in analysis scripts

2. **Documentation Enhancements**
   - Clearer explanations of methodology
   - Better formatting of results
   - Translation improvements
   - Additional examples

3. **Tool Enhancements**
   - Better error handling in scripts
   - Support for additional metrics tools
   - Cross-platform compatibility improvements
   - Performance optimizations

4. **Methodology Extensions**
   - Additional GQM objectives
   - New quality dimensions
   - Comparative analysis with other frameworks
   - Longitudinal study approaches

### Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/fastapi-gqm-quality-analysis.git
   cd fastapi-gqm-quality-analysis
   ```

2. **Set up development environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # .venv\Scripts\Activate.ps1  # Windows
   
   pip install -r requirements-dev.txt
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-improvement-name
   ```

4. **Make your changes**
   - Follow existing code style
   - Add appropriate documentation
   - Test your changes
   - Update relevant documentation

5. **Submit a pull request**
   - Describe your changes clearly
   - Reference any related issues
   - Include screenshots for UI changes
   - Ensure all tests pass

## 📋 Development Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and small

### Documentation
- Update README.md if adding new features
- Document any new metrics or analysis approaches
- Provide examples for complex functionality
- Use clear, concise language

### Testing
- Test scripts with different data sets
- Verify reproducibility of results
- Check cross-platform compatibility
- Validate statistical calculations

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, etc.)
- Keep the first line under 50 characters
- Add detailed description if necessary

Example:
```
Add support for GitHub API data collection

- Implement GitHub API client for issues data
- Add rate limiting and error handling
- Update documentation with API setup instructions
- Add tests for API functionality
```

## 🔍 Review Process

1. **Automated Checks**
   - Code style validation
   - Basic functionality tests
   - Documentation build verification

2. **Manual Review**
   - Code quality assessment
   - Methodology correctness
   - Documentation clarity
   - Impact on study validity

3. **Acceptance Criteria**
   - Maintains study integrity
   - Improves analysis quality
   - Follows contribution guidelines
   - Includes appropriate documentation

## 🐛 Reporting Issues

When reporting issues, please include:

- **Environment details** (OS, Python version, tool versions)
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Relevant log output** or error messages
- **Sample data** if applicable (anonymized)

## 📚 Resources

### GQM Methodology
- [Original GQM Paper](https://link.to.basili.paper)
- [Software Metrics: A Rigorous and Practical Approach](https://link.to.fenton.book)
- [IEEE 1061:1998 - Software Quality Metrics Methodology](https://link.to.ieee.standard)

### FastAPI Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI GitHub Repository](https://github.com/tiangolo/fastapi)
- [FastAPI Community](https://github.com/tiangolo/fastapi/discussions)

### Analysis Tools
- [Radon Documentation](https://radon.readthedocs.io/)
- [Pygount Documentation](https://github.com/roskakori/pygount)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## 🏷️ Labels and Tags

We use the following labels for issues and PRs:

- `enhancement` - New features or improvements
- `bug` - Something isn't working correctly
- `documentation` - Documentation improvements
- `methodology` - GQM methodology related
- `analysis` - Data analysis improvements
- `tools` - Analysis tools and scripts
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed

## 💡 Ideas for Contributions

If you're looking for ways to contribute, consider:

1. **Extend the analysis** to other Python frameworks (Django, Flask)
2. **Add time-series analysis** to track quality evolution
3. **Implement interactive visualizations** using Plotly or D3.js
4. **Create comparison reports** between different framework versions
5. **Add support for more metrics tools** (SonarQube, CodeClimate)
6. **Improve cross-platform support** for Windows/Mac/Linux
7. **Translate documentation** to other languages
8. **Add unit tests** for analysis scripts
9. **Create GitHub Actions** for automated analysis
10. **Develop quality trend monitoring** dashboards

## 📄 Code of Conduct

This project follows academic and open-source community standards:

- Be respectful and inclusive
- Focus on constructive feedback
- Maintain professional communication
- Respect intellectual property
- Follow scientific methodology principles

## 🎓 Academic Use

If you use this study or methodology in academic work:

1. **Citation**: Please cite this repository and the GQM methodology appropriately
2. **Acknowledgment**: Acknowledge the FastAPI project and its maintainers
3. **Sharing**: Consider sharing your findings with the community
4. **Collaboration**: We're open to academic collaborations and extensions

## ❓ Questions?

If you have questions about:
- **Methodology**: Create an issue with the `methodology` label
- **Implementation**: Create an issue with the `tools` label  
- **Results**: Create an issue with the `analysis` label
- **Documentation**: Create an issue with the `documentation` label

Thank you for contributing to software quality research! 🎉