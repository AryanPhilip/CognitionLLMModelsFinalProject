# Theory of Mind in Poker: LLM Analysis 🧠

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This repository contains the code and analysis for studying Theory of Mind (ToM) capabilities in Large Language Models through poker deception detection tasks. The project investigates how well LLMs can understand and reason about other agents' mental states in the context of poker games.

## 📋 Overview

- Novel experimental design combining poker scenarios with context swapping controls
- Analysis of ToM capabilities across different LLM architectures
- Comprehensive visualization and analysis tools
- ACL-style paper with detailed methodology and results

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/theory-of-mind-poker.git
cd theory-of-mind-poker
```

2. Set up the environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the setup script:
```bash
python src/setup_experiment.py --setup
```

## 📁 Project Structure

```
.
├── data/                      # Data files
│   ├── raw/                  # Raw experimental data
│   └── processed/            # Processed and analyzed data
├── notebooks/                # Jupyter notebooks for analysis
├── src/                      # Source code
│   ├── experiments/         # Experiment scripts
│   ├── analysis/           # Analysis scripts
│   └── visualization/      # Visualization scripts
├── results/                 # Generated results and figures
├── paper/                   # Paper-related files
└── requirements.txt         # Python dependencies
```

## 🔧 Key Components

### Experiments
- `poker_tom_experiment.py`: Main experiment script
- `context_swapping_control.py`: Context swapping control implementation

### Analysis
- `cognitive_analysis.py`: Analysis of cognitive patterns
- `tom_examples_analysis.py`: Analysis of ToM reasoning

### Visualization
- `presentation_visuals.py`: Generation of presentation figures
- `context_control_visualization.py`: Context control visualizations

## 📊 Results

Key findings and visualizations are available in the `results/` directory. The paper provides detailed analysis and discussion of the results.

## 📝 Paper

The paper is written in LaTeX and includes:
- Main paper assembly (`acl_paper_assembly.tex`)
- Individual sections (methods, results, discussion)
- Supporting tables and figures

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Citation

If you use this code or data, please cite our paper:
```
@article{your-paper-citation}
```

## 👥 Authors

- Your Name - Initial work - [Your GitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Thanks to all contributors and reviewers
- Special thanks to [Your Professor/Advisor] for guidance 