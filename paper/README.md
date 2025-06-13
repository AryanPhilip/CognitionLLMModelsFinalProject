# Theory of Mind in Poker: LLM Analysis

This repository contains code and analysis for studying Theory of Mind (ToM) capabilities in Large Language Models through poker deception detection tasks.

## Project Overview

This project investigates how well Large Language Models (LLMs) can understand and reason about other agents' mental states in the context of poker games. The study uses a novel experimental design that combines poker scenarios with context swapping controls to test true ToM capabilities.

## Repository Structure

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

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Key Components

### Experiments
- `poker_tom_experiment.py`: Main experiment script for running ToM tests
- `context_swapping_control.py`: Implementation of context swapping control condition

### Analysis
- `cognitive_analysis.py`: Analysis of cognitive patterns in model responses
- `tom_examples_analysis.py`: Analysis of ToM reasoning examples

### Visualization
- `presentation_visuals.py`: Generation of presentation figures
- `context_control_visualization.py`: Visualization of context control results

## Paper

The paper is written in LaTeX and includes:
- Main paper assembly (`acl_paper_assembly.tex`)
- Individual sections (methods, results, discussion)
- Supporting tables and figures

## Results

Key results are available in:
- `results/`: Generated figures and analysis outputs
- `paper/`: Tables and visualizations used in the paper

## Citation

If you use this code or data, please cite our paper:
```
@article{your-paper-citation}
```

## License

[Your chosen license] 