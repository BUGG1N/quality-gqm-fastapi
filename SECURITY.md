# Security Policy

## Supported Versions

This repository contains an academic research study and analysis tools. Security updates are provided for the current version:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Security Considerations

### Data Security
- This study analyzes publicly available open-source code (FastAPI)
- No sensitive data or credentials are collected or stored
- All analysis is performed on public repository data
- Raw metrics are stored locally without transmission

### Script Security
- Analysis scripts use only standard Python libraries
- External dependencies are minimal and well-established
- No network operations beyond repository cloning
- No elevated privileges required for execution

### Reporting a Vulnerability

While this is primarily an academic study, if you discover any security concerns:

1. **For immediate security issues**: Create a private issue or contact directly
2. **For analysis methodology concerns**: Open a public issue with the `security` label
3. **For dependency vulnerabilities**: Run `pip audit` and report findings

### Security Best Practices

When using this analysis framework:

1. **Virtual Environment**: Always use isolated Python environments
2. **Dependency Management**: Regularly update dependencies with `pip install --upgrade`
3. **Data Handling**: Ensure analyzed repositories are from trusted sources
4. **Script Execution**: Review scripts before execution in your environment
5. **Access Control**: Limit access to analysis results as appropriate

### Responsible Disclosure

This project follows responsible disclosure principles:
- Security issues will be addressed promptly
- Public disclosure will occur after fixes are available
- Credit will be given to security researchers who report issues responsibly

### Dependencies Security

Current dependencies and their security status:
- `pandas`: Data analysis library (regularly updated)
- `matplotlib`: Visualization library (stable)
- `radon`: Code metrics tool (active maintenance)
- `pygount`: Line counting tool (stable)

Regular security audits are performed using:
```bash
pip audit
```

For academic and research use, this framework follows standard software engineering security practices while maintaining transparency and reproducibility.