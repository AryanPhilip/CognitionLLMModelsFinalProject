"""Configuration settings for the experiment."""

import os
from pathlib import Path

# Experimental Parameters
TEMPERATURE = 0.5
MAX_NEW_TOKENS = 350
NUM_RUNS_PER_STIM = 3

# File Paths
PROJECT_ROOT = Path(__file__).parent
STIMULI_CSV = PROJECT_ROOT / "poker_stimuli_20250527_212428.csv"
RESULTS_DIR = PROJECT_ROOT / "results"
CODING_TEMPLATE = PROJECT_ROOT / "poker_llm_coding_sheet.csv"

# Model Configuration (adapt for your setup)
MODEL_CONFIGS = {
    "qwen3-1.7B-unsloth": {
        "model_name": "unsloth/qwen2.5-1.5b-instruct-bnb-4bit",
        "load_in_4bit": True,
        "max_seq_length": 2048,
    },
    # Add more model configurations as needed
}

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FILE = PROJECT_ROOT / "experiment.log" 