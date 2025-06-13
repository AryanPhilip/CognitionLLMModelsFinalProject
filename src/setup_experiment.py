#!/usr/bin/env python3
"""
Setup script for Theory of Mind in Poker project.
This script helps users set up and run the experiment.
"""

import os
import sys
from pathlib import Path
import argparse
from dotenv import load_dotenv

def setup_environment():
    """Set up the environment variables and paths."""
    # Load environment variables
    load_dotenv()
    
    # Create necessary directories if they don't exist
    dirs = ['data/raw', 'data/processed', 'results', 'notebooks']
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description='Setup Theory of Mind in Poker experiment')
    parser.add_argument('--setup', action='store_true', help='Set up the environment')
    parser.add_argument('--run', action='store_true', help='Run the experiment')
    args = parser.parse_args()

    if args.setup:
        setup_environment()
        print("Environment setup complete!")
        print("\nNext steps:")
        print("1. Configure your API keys in .env file")
        print("2. Run 'python src/setup_experiment.py --run' to start the experiment")
    
    if args.run:
        from experiments.poker_tom_experiment import PokerToMExperiment
        experiment = PokerToMExperiment()
        experiment.run()

if __name__ == '__main__':
    main() 