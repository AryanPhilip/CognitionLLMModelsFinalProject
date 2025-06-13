#!/usr/bin/env python3
"""
Create Context-Swapped Stimuli for Control Condition Testing
Generates actual swapped stimuli that can be run through the models to test ToM vs. poker knowledge.
"""

import pandas as pd
import csv
import re

def load_original_stimuli():
    """Load the original poker stimuli."""
    try:
        df = pd.read_csv('poker_stimuli_20250527_212428.csv')
        print(f"✓ Loaded {len(df)} original stimuli")
        return df
    except FileNotFoundError:
        print("❌ Could not find poker_stimuli_20250527_212428.csv")
        return None

def extract_context_descriptions(stimulus_text):
    """Extract the opponent context description from stimulus text."""
    
    # Look for patterns like "Opponent:" or "History:" sections
    context_patterns = [
        r"Opponent:\s*(.+?)(?=\n\n|\nBoard:|\nAction:|\nHero:|\Z)",
        r"History:\s*(.+?)(?=\n\n|\nBoard:|\nAction:|\nHero:|\Z)",
        r"Context:\s*(.+?)(?=\n\n|\nBoard:|\nAction:|\nHero:|\Z)",
    ]
    
    for pattern in context_patterns:
        match = re.search(pattern, stimulus_text, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    # If no clear pattern, look for descriptive text about the opponent
    lines = stimulus_text.split('\n')
    context_lines = []
    
    for line in lines:
        line = line.strip()
        if any(keyword in line.lower() for keyword in 
               ['bluff', 'aggressive', 'tight', 'conservative', 'history', 'tendency', 'pattern']):
            context_lines.append(line)
    
    return ' '.join(context_lines) if context_lines else ""

def create_context_swapped_pairs(df):
    """Create context-swapped versions of the stimuli."""
    
    swapped_stimuli = []
    
    # Extract scenario IDs from the ID column (e.g., S1 from S1_Bluff)
    df['Scenario_ID'] = df['ID'].str.extract(r'(S\d+)_')
    scenario_ids = df['Scenario_ID'].unique()
    
    for scenario_id in scenario_ids:
        scenario_data = df[df['Scenario_ID'] == scenario_id]
        
        if len(scenario_data) != 2:
            print(f"⚠ Scenario {scenario_id} doesn't have exactly 2 conditions, skipping")
            continue
        
        bluff_row = scenario_data[scenario_data['ID'].str.contains('Bluff')].iloc[0]
        value_row = scenario_data[scenario_data['ID'].str.contains('Value')].iloc[0]
        
        # Use the Context column directly for swapping
        bluff_context = bluff_row['Context']
        value_context = value_row['Context']
        
        if not bluff_context or not value_context:
            print(f"⚠ Empty context for scenario {scenario_id}, skipping")
            continue
        
        # Create swapped versions
        bluff_swapped = bluff_row.copy()
        value_swapped = value_row.copy()
        
        # Swap contexts
        bluff_swapped['ID'] = f"{scenario_id}_Bluff_Swapped"
        bluff_swapped['Context'] = value_context
        
        value_swapped['ID'] = f"{scenario_id}_Value_Swapped"
        value_swapped['Context'] = bluff_context
        
        swapped_stimuli.extend([bluff_swapped, value_swapped])
        
        print(f"✓ Created swapped pair for scenario {scenario_id}")
    
    return pd.DataFrame(swapped_stimuli)

def generate_sample_swapped_stimuli():
    """Generate sample context-swapped stimuli for demonstration."""
    
    sample_stimuli = [
        {
            'Stimulus_ID': 'S1_Bluff_Swapped',
            'Core_Scenario_ID': 'S1',
            'Context_Type': 'Bluff',
            'Expected_Answer': 'Bluff',
            'Full_Stimulus': """You are playing poker against an opponent. Analyze the situation and determine if their bet is a BLUFF or VALUE bet.

Opponent: This player is extremely tight and conservative, only commits big money with very strong hands like suited Broadway cards. They rarely bluff and prefer to slow-play their monsters.

Situation:
Board: K♥ T♥ 8♦ 2♠
Hero's Hand: A♦ Q♣
Pot: $150
Action: Opponent bets $110 (roughly 75% of pot)

Question: Is this bet more likely a BLUFF or VALUE bet?
Reasoning: Consider the opponent's playing style, board texture, and bet sizing.""",
            'Notes': 'Context swapped from S1_Value - testing if model relies on opponent psychology vs. bet size'
        },
        {
            'Stimulus_ID': 'S1_Value_Swapped', 
            'Core_Scenario_ID': 'S1',
            'Context_Type': 'Value',
            'Expected_Answer': 'Value',
            'Full_Stimulus': """You are playing poker against an opponent. Analyze the situation and determine if their bet is a BLUFF or VALUE bet.

Opponent: This player loves to triple-barrel with draws and has been very aggressive. Recently showed down an unlikely bluff with 8♦ 6♦ on a heart-heavy board, indicating willingness to bluff with weak holdings.

Situation:
Board: K♥ T♥ 8♦ 2♠
Hero's Hand: A♦ Q♣  
Pot: $150
Action: Opponent bets $110 (roughly 75% of pot)

Question: Is this bet more likely a BLUFF or VALUE bet?
Reasoning: Consider the opponent's playing style, board texture, and bet sizing.""",
            'Notes': 'Context swapped from S1_Bluff - testing if model relies on opponent psychology vs. bet size'
        }
    ]
    
    return pd.DataFrame(sample_stimuli)

def save_swapped_stimuli(swapped_df, filename='context_swapped_stimuli.csv'):
    """Save the context-swapped stimuli to a CSV file."""
    
    swapped_df.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)
    print(f"✓ Saved {len(swapped_df)} context-swapped stimuli to {filename}")
    
    return filename

def create_control_experiment_instructions():
    """Create instructions for running the control experiment."""
    
    instructions = """
# Context Swapping Control Experiment Instructions

## Purpose
Test whether models rely on Theory of Mind reasoning (opponent psychology) vs. poker knowledge (hand strength, bet size).

## Method
1. Present models with context-swapped stimuli where opponent descriptions are switched
2. Compare predictions between original and swapped versions
3. Models using ToM should change predictions significantly
4. Models using only poker heuristics should show minimal change

## Expected Results
- **High ToM models**: Predictions should flip when context is swapped
- **Low ToM models**: Predictions should remain similar regardless of context

## Analysis
1. Calculate prediction change rate for each model
2. Statistical test: paired t-test comparing original vs. swapped accuracy
3. Effect size: Cohen's d for magnitude of change
4. Interpretation: High effect = ToM reasoning, Low effect = poker heuristics

## Key Scenarios to Test
- S1: Tight vs. Aggressive player on same board
- S3: Draw-heavy vs. Conservative player  
- S6: Bluff-heavy vs. Value-oriented player
- S8: Loose vs. Tight player tendencies

## Statistical Power
- Need minimum 20 scenarios per condition for adequate power
- Test each swapped pair with 3 runs per model for reliability
- Control for order effects by randomizing presentation
"""
    
    with open('control_experiment_instructions.md', 'w') as f:
        f.write(instructions)
    
    print("✓ Created control_experiment_instructions.md")

def main():
    """Main function to create context-swapped stimuli."""
    
    print("Creating Context-Swapped Stimuli for Control Condition")
    print("=" * 55)
    
    # Try to load original stimuli
    df = load_original_stimuli()
    
    if df is not None and len(df) > 0:
        print("\n1. Processing Original Stimuli...")
        swapped_df = create_context_swapped_pairs(df)
        
        if len(swapped_df) > 0:
            filename = save_swapped_stimuli(swapped_df)
            print(f"✓ Successfully created {len(swapped_df)} swapped stimuli")
        else:
            print("⚠ No swapped stimuli could be created from original data")
            print("  Creating sample stimuli instead...")
            swapped_df = generate_sample_swapped_stimuli()
            save_swapped_stimuli(swapped_df, 'sample_context_swapped_stimuli.csv')
    else:
        print("\n1. Creating Sample Swapped Stimuli...")
        swapped_df = generate_sample_swapped_stimuli()
        save_swapped_stimuli(swapped_df, 'sample_context_swapped_stimuli.csv')
    
    print("\n2. Creating Experiment Instructions...")
    create_control_experiment_instructions()
    
    print("\n3. Summary:")
    print("-" * 30)
    print("This control condition tests a key prediction:")
    print("• ToM-capable models should change predictions when context swaps")
    print("• Non-ToM models should ignore context and focus on poker mechanics")
    print("• This distinguishes genuine theory of mind from pattern matching")
    
    print("\nNext Steps:")
    print("1. Run swapped stimuli through your models")
    print("2. Compare accuracy: original vs. swapped scenarios") 
    print("3. Calculate effect sizes and statistical significance")
    print("4. Include results in your paper's control analysis")
    
    print(f"\nFiles created:")
    print("- context_swapped_stimuli.csv (or sample version)")
    print("- control_experiment_instructions.md")

if __name__ == "__main__":
    main() 