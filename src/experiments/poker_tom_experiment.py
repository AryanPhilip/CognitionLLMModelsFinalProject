#!/usr/bin/env python3
"""
Theory of Mind Poker Experiment Script
=====================================

Executes LLM classification experiments on poker scenarios to test Theory of Mind capabilities.
Supports Unsloth-optimized models with configurable parameters.

Usage:
    python poker_tom_experiment.py --model_name "qwen3-1.7B-unsloth" --output_dir "./results"
"""

import os
import re
import csv
import json
import argparse
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('experiment.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Experimental Parameters
TEMPERATURE = 0.5
MAX_NEW_TOKENS = 350
NUM_RUNS_PER_STIM = 3

# Prompt Template
PROMPT_TEMPLATE = """You are an expert poker player analyzing a hand of No-Limit Texas Hold'em.

Hero Hand: {HERO_HAND}
Community Cards (River complete): {BOARD}
Pot Size: {POT}
Opponent's Bet: {OPPONENT_BET}

Opponent Information:
{CONTEXT}

Please answer the following:

1. Classification: (Answer **only** "Bluff" or "Value")
2. Explanation: Explain **why** you classified the bet that way, referring to board texture, bet size, and the opponent tendencies described above."""

class PokerTOMExperiment:
    """Main experiment runner for Theory of Mind poker analysis."""
    
    def __init__(self, model_name: str, output_dir: str = "./results"):
        self.model_name = model_name
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Initialize model (placeholder - implement based on your LLM setup)
        self.model = None
        self.tokenizer = None
        
        # Results storage
        self.results = []
        
    def load_model(self):
        """Load the specified LLM model. Adapt this for your setup."""
        logger.info(f"Loading model: {self.model_name}")
        
        # TODO: Implement your model loading logic here
        # Examples for different setups:
        
        # For Unsloth:
        # from unsloth import FastLanguageModel
        # self.model, self.tokenizer = FastLanguageModel.from_pretrained(
        #     model_name=self.model_name,
        #     max_seq_length=2048,
        #     dtype=None,
        #     load_in_4bit=True,
        # )
        
        # For standard transformers:
        # from transformers import AutoTokenizer, AutoModelForCausalLM
        # self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        # self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        
        # For API-based models:
        # self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        logger.info("Model loaded successfully")
    
    def load_stimuli(self, csv_path: str = "poker_stimuli_20250527_212428.csv") -> pd.DataFrame:
        """Load poker stimuli from CSV file."""
        logger.info(f"Loading stimuli from: {csv_path}")
        
        try:
            df = pd.read_csv(csv_path)
            logger.info(f"Loaded {len(df)} stimuli scenarios")
            return df
        except Exception as e:
            logger.error(f"Error loading stimuli: {e}")
            raise
    
    def format_prompt(self, stimulus: Dict) -> str:
        """Format the prompt template with stimulus data."""
        return PROMPT_TEMPLATE.format(
            HERO_HAND=stimulus['Hero Hand'],
            BOARD=stimulus['Board'],
            POT=stimulus['Pot'],
            OPPONENT_BET=stimulus['Opponent Bet'],
            CONTEXT=stimulus['Context']
        )
    
    def generate_response(self, prompt: str) -> str:
        """Generate LLM response for given prompt. Adapt based on your model setup."""
        
        # TODO: Implement your inference logic here
        # Examples for different setups:
        
        # For local transformers model:
        # inputs = self.tokenizer(prompt, return_tensors="pt")
        # with torch.no_grad():
        #     outputs = self.model.generate(
        #         **inputs,
        #         max_new_tokens=MAX_NEW_TOKENS,
        #         temperature=TEMPERATURE,
        #         do_sample=True,
        #         pad_token_id=self.tokenizer.eos_token_id
        #     )
        # response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # return response[len(prompt):].strip()
        
        # For API-based models:
        # response = self.client.chat.completions.create(
        #     model=self.model_name,
        #     messages=[{"role": "user", "content": prompt}],
        #     temperature=TEMPERATURE,
        #     max_tokens=MAX_NEW_TOKENS
        # )
        # return response.choices[0].message.content
        
        # Placeholder for testing
        return "1. Classification: Bluff\n2. Explanation: This appears to be a bluff based on the opponent's aggressive tendencies and the scary river card."
    
    def parse_response(self, raw_response: str) -> Tuple[str, str]:
        """Parse LLM response into classification and explanation."""
        
        # Extract classification
        classification = "Unsure"  # Default
        class_match = re.search(r'1\.\s*Classification:\s*(?:\*\*)?([^*\n]+?)(?:\*\*)?\s*(?:\n|$)', raw_response, re.IGNORECASE)
        if class_match:
            class_text = class_match.group(1).strip().lower()
            if 'bluff' in class_text:
                classification = "Bluff"
            elif 'value' in class_text:
                classification = "Value"
        
        # Extract explanation
        explanation = ""
        exp_match = re.search(r'2\.\s*Explanation:\s*(.*)', raw_response, re.IGNORECASE | re.DOTALL)
        if exp_match:
            explanation = exp_match.group(1).strip()
        
        return classification, explanation
    
    def extract_ground_truth(self, stimulus_id: str) -> str:
        """Extract ground truth from stimulus ID."""
        if 'Bluff' in stimulus_id:
            return "Bluff"
        elif 'Value' in stimulus_id:
            return "Value"
        else:
            return "Unknown"
    
    def extract_core_scenario(self, stimulus_id: str) -> str:
        """Extract core scenario ID (e.g., S1 from S1_Bluff)."""
        match = re.match(r'(S\d+)_', stimulus_id)
        return match.group(1) if match else stimulus_id
    
    def run_single_stimulus(self, stimulus: Dict, run_number: int) -> Dict:
        """Run experiment for single stimulus."""
        
        stimulus_id = stimulus['ID']
        logger.info(f"Processing {stimulus_id}, Run {run_number}")
        
        # Format prompt
        prompt = self.format_prompt(stimulus)
        
        # Generate response
        try:
            raw_response = self.generate_response(prompt)
        except Exception as e:
            logger.error(f"Error generating response for {stimulus_id}: {e}")
            raw_response = f"ERROR: {str(e)}"
        
        # Parse response
        classification, explanation = self.parse_response(raw_response)
        
        # Extract metadata
        ground_truth = self.extract_ground_truth(stimulus_id)
        core_scenario = self.extract_core_scenario(stimulus_id)
        is_correct = 1 if classification == ground_truth else 0
        
        # Create result record
        result = {
            'Stimulus_ID': stimulus_id,
            'Core_Scenario_ID': core_scenario,
            'Context_Type': ground_truth,
            'LLM_Model': self.model_name,
            'Run_Number': run_number,
            'Temperature': TEMPERATURE,
            'Max_New_Tokens': MAX_NEW_TOKENS,
            'LLM_Raw_Response': raw_response,
            'Parsed_Classification': classification,
            'Is_Classification_Correct': is_correct,
            'Explanation_Text': explanation,
            'Timestamp': datetime.now().isoformat()
        }
        
        return result
    
    def run_experiment(self, csv_path: str = "poker_stimuli_20250527_212428.csv"):
        """Run the complete experiment."""
        
        logger.info("Starting Theory of Mind Poker Experiment")
        logger.info(f"Model: {self.model_name}")
        logger.info(f"Parameters: T={TEMPERATURE}, Max_tokens={MAX_NEW_TOKENS}, Runs={NUM_RUNS_PER_STIM}")
        
        # Load model and stimuli
        self.load_model()
        stimuli_df = self.load_stimuli(csv_path)
        
        # Run experiments
        total_runs = len(stimuli_df) * NUM_RUNS_PER_STIM
        progress_bar = tqdm(total=total_runs, desc="Running experiments")
        
        for _, stimulus in stimuli_df.iterrows():
            stimulus_dict = stimulus.to_dict()
            
            for run_num in range(1, NUM_RUNS_PER_STIM + 1):
                result = self.run_single_stimulus(stimulus_dict, run_num)
                self.results.append(result)
                progress_bar.update(1)
        
        progress_bar.close()
        
        # Save results
        self.save_results()
        
        logger.info(f"Experiment completed. {len(self.results)} responses generated.")
    
    def save_results(self):
        """Save experimental results to CSV."""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"poker_tom_results_{self.model_name}_{timestamp}.csv"
        filepath = self.output_dir / filename
        
        # Convert to DataFrame and save
        results_df = pd.DataFrame(self.results)
        results_df.to_csv(filepath, index=False)
        
        logger.info(f"Results saved to: {filepath}")
        
        # Generate summary
        self.generate_summary(results_df, filepath.with_suffix('.summary.txt'))
    
    def generate_summary(self, results_df: pd.DataFrame, summary_path: Path):
        """Generate experiment summary statistics."""
        
        total_responses = len(results_df)
        correct_responses = results_df['Is_Classification_Correct'].sum()
        accuracy = correct_responses / total_responses if total_responses > 0 else 0
        
        # Accuracy by context type
        bluff_accuracy = results_df[results_df['Context_Type'] == 'Bluff']['Is_Classification_Correct'].mean()
        value_accuracy = results_df[results_df['Context_Type'] == 'Value']['Is_Classification_Correct'].mean()
        
        # Consistency across runs
        consistency_data = []
        for scenario in results_df['Core_Scenario_ID'].unique():
            scenario_data = results_df[results_df['Core_Scenario_ID'] == scenario]
            for context_type in ['Bluff', 'Value']:
                context_data = scenario_data[scenario_data['Context_Type'] == context_type]
                if len(context_data) == NUM_RUNS_PER_STIM:
                    classifications = context_data['Parsed_Classification'].tolist()
                    is_consistent = len(set(classifications)) == 1
                    consistency_data.append(is_consistent)
        
        consistency_rate = np.mean(consistency_data) if consistency_data else 0
        
        summary = f"""
Theory of Mind Poker Experiment Summary
======================================

Model: {self.model_name}
Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Experimental Parameters:
- Temperature: {TEMPERATURE}
- Max New Tokens: {MAX_NEW_TOKENS}
- Runs per Stimulus: {NUM_RUNS_PER_STIM}

Results:
- Total Responses: {total_responses}
- Correct Classifications: {correct_responses}
- Overall Accuracy: {accuracy:.3f} ({accuracy*100:.1f}%)

Accuracy by Context Type:
- Bluff Detection: {bluff_accuracy:.3f} ({bluff_accuracy*100:.1f}%)
- Value Detection: {value_accuracy:.3f} ({value_accuracy*100:.1f}%)

Response Consistency:
- Consistent across runs: {consistency_rate:.3f} ({consistency_rate*100:.1f}%)

Classification Distribution:
{results_df['Parsed_Classification'].value_counts().to_string()}

Next Steps:
1. Manual coding using poker_llm_coding_sheet.csv template
2. Apply coding rubric for ToM analysis
3. Statistical testing of hypotheses
"""
        
        with open(summary_path, 'w') as f:
            f.write(summary)
        
        logger.info(f"Summary saved to: {summary_path}")
        print(summary)

def main():
    """Main execution function."""
    
    parser = argparse.ArgumentParser(description="Theory of Mind Poker Experiment")
    parser.add_argument("--model_name", required=True, help="Name/path of the LLM model")
    parser.add_argument("--output_dir", default="./results", help="Output directory for results")
    parser.add_argument("--stimuli_csv", default="poker_stimuli_20250527_212428.csv", 
                       help="Path to stimuli CSV file")
    
    args = parser.parse_args()
    
    # Create and run experiment
    experiment = PokerTOMExperiment(
        model_name=args.model_name,
        output_dir=args.output_dir
    )
    
    experiment.run_experiment(args.stimuli_csv)

if __name__ == "__main__":
    main() 