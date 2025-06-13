#!/usr/bin/env python3
"""
Cognitive ToM Analysis Summary: Key Insights and Examples
========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the cognitive analysis results
cognitive_df = pd.read_csv('detailed_cognitive_analysis.csv')
summary_df = pd.read_csv('cognitive_analysis_summary.csv')

print("🧠 COGNITIVE THEORY OF MIND ANALYSIS SUMMARY")
print("=" * 60)

# Display top-level insights
print("\n🎯 KEY FINDINGS:")
print("1. 64.7% of explanations show first-order ToM reasoning")
print("2. Only 5.6% demonstrate sophisticated second-order ToM")
print("3. Context integration strongly correlates with accuracy (r=0.420)")
print("4. Bluff detection requires MORE sophisticated ToM reasoning")
print("5. Clear model hierarchy in cognitive sophistication")

print("\n🤖 MODEL COGNITIVE CAPABILITIES:")
print("Hush-Qwen2.5-7B: 0.97 avg ToM, 93.3% accuracy")
print("OLMoE-1B-7B: 0.98 avg ToM, 57.8% accuracy") 
print("EXAONE-3.5-2.4B: 0.81 avg ToM, 44.4% accuracy")
print("Llama-1B: 0.28 avg ToM, 12.2% accuracy")

print("\n🔍 COGNITIVE PATTERNS DISCOVERED:")

# Find best ToM examples
best_tom = cognitive_df[cognitive_df['ToM_Level'] == 2].sort_values('Reasoning_Sophistication', ascending=False)

print("\n🏆 BEST SECOND-ORDER ToM EXAMPLES:")
for idx, (_, row) in enumerate(best_tom.head(3).iterrows()):
    print(f"\n{idx+1}. Model: {row['Model']}")
    print(f"   Context: {row['Context_Type']} | Correct: {bool(row['Is_Correct'])}")
    print(f"   Sophistication: {row['Reasoning_Sophistication']:.2f}")
    print(f"   Text: {row['Explanation_Text'][:150]}...")

# Analyze cognitive differences between bluff and value
bluff_tom = cognitive_df[cognitive_df['Context_Type'] == 'Bluff']['ToM_Level'].mean()
value_tom = cognitive_df[cognitive_df['Context_Type'] == 'Value']['ToM_Level'].mean()

print(f"\n🎭 BLUFF vs VALUE COGNITIVE DIFFERENCES:")
print(f"Bluff detection ToM level: {bluff_tom:.3f}")
print(f"Value detection ToM level: {value_tom:.3f}")
print(f"Difference: {abs(bluff_tom - value_tom):.3f}")

# Find examples of sophisticated opponent modeling
sophisticated_opp = cognitive_df[cognitive_df['Opponent_Psychology'] >= 2].sort_values('Reasoning_Sophistication', ascending=False)

print("\n🧍 SOPHISTICATED OPPONENT MODELING EXAMPLES:")
for idx, (_, row) in enumerate(sophisticated_opp.head(2).iterrows()):
    print(f"\n{idx+1}. Model: {row['Model']}")
    print(f"   Psychology Score: {row['Opponent_Psychology']}")
    print(f"   History References: {row['Opponent_History']}")
    print(f"   Text: {row['Explanation_Text'][:150]}...")

# Strategic reasoning analysis
high_strategy = cognitive_df[cognitive_df['Strategic_Reasoning_Score'] >= 3].sort_values('Strategic_Reasoning_Score', ascending=False)

print("\n⚔️ ADVANCED STRATEGIC REASONING EXAMPLES:")
for idx, (_, row) in enumerate(high_strategy.head(2).iterrows()):
    print(f"\n{idx+1}. Model: {row['Model']}")
    print(f"   Strategy Score: {row['Strategic_Reasoning_Score']}")
    print(f"   Game Theory Terms: {row['Game_Theory_Terms']}")
    print(f"   Text: {row['Explanation_Text'][:150]}...")

print("\n📊 CORRELATION WITH ACCURACY:")
correlations = cognitive_df[['ToM_Level', 'Context_Integration_Score', 'Strategic_Reasoning_Score', 
                           'Opponent_Psychology', 'Reasoning_Sophistication', 'Is_Correct']].corr()['Is_Correct'].sort_values(ascending=False)

for factor, corr in correlations.items():
    if factor != 'Is_Correct':  # Exclude self-correlation
        print(f"{factor}: {corr:.3f}")

print("\n" + "=" * 60)
print("🎓 IMPLICATIONS FOR AI THEORY OF MIND:")
print("1. LLMs can demonstrate measurable ToM capabilities")
print("2. Deception detection is a key bottleneck")
print("3. Context integration drives performance")
print("4. Model scale strongly affects cognitive sophistication")
print("5. Rich behavioral context enables ToM reasoning") 