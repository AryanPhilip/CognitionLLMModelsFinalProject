
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
