#!/usr/bin/env python3
"""
Visualize the Context Swapping Control Condition
Shows how this test distinguishes Theory of Mind reasoning from poker knowledge.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_control_mechanism_diagram():
    """Create a diagram showing how the control condition works."""
    
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(5, 11.5, 'Context Swapping Control Condition', 
            fontsize=20, fontweight='bold', ha='center')
    ax.text(5, 11, 'Testing Theory of Mind vs. Poker Knowledge', 
            fontsize=14, ha='center', style='italic')
    
    # Create boxes for different scenarios
    # Original Scenarios
    ax.text(2.5, 10, 'ORIGINAL SCENARIOS', fontsize=14, fontweight='bold', ha='center')
    
    # Scenario 1 Original
    s1_orig = FancyBboxPatch((0.5, 8.5), 4, 1.2, boxstyle="round,pad=0.1", 
                             facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(s1_orig)
    ax.text(2.5, 9.3, 'S1_Bluff: Aggressive Player', fontsize=11, fontweight='bold', ha='center')
    ax.text(2.5, 9.1, 'Context: "Triple-barrels missed draws"', fontsize=9, ha='center')
    ax.text(2.5, 8.9, 'Bet: $100 (80% pot)', fontsize=9, ha='center')
    ax.text(2.5, 8.7, 'Expected: BLUFF', fontsize=10, fontweight='bold', ha='center', color='red')
    
    # Scenario 1 Value Original  
    s1v_orig = FancyBboxPatch((0.5, 7), 4, 1.2, boxstyle="round,pad=0.1", 
                              facecolor='lightgreen', edgecolor='green', linewidth=2)
    ax.add_patch(s1v_orig)
    ax.text(2.5, 7.8, 'S1_Value: Conservative Player', fontsize=11, fontweight='bold', ha='center')
    ax.text(2.5, 7.6, 'Context: "Only commits with real hands"', fontsize=9, ha='center')
    ax.text(2.5, 7.4, 'Bet: $100 (80% pot)', fontsize=9, ha='center')
    ax.text(2.5, 7.2, 'Expected: VALUE', fontsize=10, fontweight='bold', ha='center', color='green')
    
    # Arrow pointing right
    ax.annotate('', xy=(6, 8.5), xytext=(5, 8.5), 
                arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax.text(5.5, 8.7, 'SWAP\nCONTEXT', fontsize=10, fontweight='bold', ha='center')
    
    # Swapped Scenarios
    ax.text(7.5, 10, 'CONTEXT-SWAPPED SCENARIOS', fontsize=14, fontweight='bold', ha='center')
    
    # Scenario 1 Swapped
    s1_swap = FancyBboxPatch((5.5, 8.5), 4, 1.2, boxstyle="round,pad=0.1", 
                             facecolor='lightyellow', edgecolor='orange', linewidth=2)
    ax.add_patch(s1_swap)
    ax.text(7.5, 9.3, 'S1_Bluff_Swapped: Conservative Player', fontsize=11, fontweight='bold', ha='center')
    ax.text(7.5, 9.1, 'Context: "Only commits with real hands"', fontsize=9, ha='center')
    ax.text(7.5, 8.9, 'Bet: $100 (80% pot)', fontsize=9, ha='center')
    ax.text(7.5, 8.7, 'Expected: VALUE', fontsize=10, fontweight='bold', ha='center', color='green')
    
    # Scenario 1 Value Swapped
    s1v_swap = FancyBboxPatch((5.5, 7), 4, 1.2, boxstyle="round,pad=0.1", 
                              facecolor='lightyellow', edgecolor='orange', linewidth=2)
    ax.add_patch(s1v_swap)
    ax.text(7.5, 7.8, 'S1_Value_Swapped: Aggressive Player', fontsize=11, fontweight='bold', ha='center')
    ax.text(7.5, 7.6, 'Context: "Triple-barrels missed draws"', fontsize=9, ha='center')
    ax.text(7.5, 7.4, 'Bet: $100 (80% pot)', fontsize=9, ha='center')
    ax.text(7.5, 7.2, 'Expected: BLUFF', fontsize=10, fontweight='bold', ha='center', color='red')
    
    # What stays the same vs changes
    same_box = FancyBboxPatch((0.5, 5.5), 9, 0.8, boxstyle="round,pad=0.1", 
                              facecolor='#f0f0f0', edgecolor='gray', linewidth=1)
    ax.add_patch(same_box)
    ax.text(5, 6, 'WHAT STAYS THE SAME: Hero hand, Board, Pot size, Bet size, Bet timing', 
            fontsize=11, fontweight='bold', ha='center')
    ax.text(5, 5.7, 'WHAT CHANGES: Only the opponent psychological profile description', 
            fontsize=11, fontweight='bold', ha='center', color='red')
    
    # Model predictions section
    ax.text(5, 4.8, 'MODEL PREDICTIONS & INTERPRETATION', 
            fontsize=16, fontweight='bold', ha='center')
    
    # Theory of Mind Model
    tom_box = FancyBboxPatch((0.5, 3), 4, 1.5, boxstyle="round,pad=0.1", 
                             facecolor='lightcyan', edgecolor='teal', linewidth=2)
    ax.add_patch(tom_box)
    ax.text(2.5, 4.2, 'HIGH THEORY OF MIND MODEL', fontsize=12, fontweight='bold', ha='center')
    ax.text(2.5, 3.9, '✓ Predictions FLIP when context swaps', fontsize=10, ha='center')
    ax.text(2.5, 3.7, '✓ S1_Bluff → VALUE (conservative player)', fontsize=9, ha='center')
    ax.text(2.5, 3.5, '✓ S1_Value → BLUFF (aggressive player)', fontsize=9, ha='center')
    ax.text(2.5, 3.3, '✓ Large Context Effect (>0.5)', fontsize=10, fontweight='bold', ha='center', color='teal')
    ax.text(2.5, 3.1, 'Uses opponent psychology for decisions', fontsize=9, ha='center', style='italic')
    
    # Poker Knowledge Model
    poker_box = FancyBboxPatch((5.5, 3), 4, 1.5, boxstyle="round,pad=0.1", 
                               facecolor='lightcoral', edgecolor='darkred', linewidth=2)
    ax.add_patch(poker_box)
    ax.text(7.5, 4.2, 'LOW THEORY OF MIND MODEL', fontsize=12, fontweight='bold', ha='center')
    ax.text(7.5, 3.9, '✗ Predictions STAY SAME despite context', fontsize=10, ha='center')
    ax.text(7.5, 3.7, '✗ S1_Bluff → BLUFF (ignores new context)', fontsize=9, ha='center')
    ax.text(7.5, 3.5, '✗ S1_Value → VALUE (ignores new context)', fontsize=9, ha='center')
    ax.text(7.5, 3.3, '✗ Small Context Effect (<0.2)', fontsize=10, fontweight='bold', ha='center', color='darkred')
    ax.text(7.5, 3.1, 'Uses only hand strength & bet size', fontsize=9, ha='center', style='italic')
    
    # Key insight box
    insight_box = FancyBboxPatch((1, 1), 8, 1.5, boxstyle="round,pad=0.15", 
                                 facecolor='gold', edgecolor='darkorange', linewidth=3)
    ax.add_patch(insight_box)
    ax.text(5, 2.2, '🔑 KEY INSIGHT', fontsize=14, fontweight='bold', ha='center')
    ax.text(5, 1.9, 'If models change predictions when ONLY opponent psychology changes,', fontsize=11, ha='center')
    ax.text(5, 1.7, 'then they are using Theory of Mind reasoning, not just poker heuristics.', fontsize=11, ha='center')
    ax.text(5, 1.4, 'This control distinguishes genuine mental state attribution from pattern matching.', 
            fontsize=11, ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('context_control_mechanism.pdf', dpi=300, bbox_inches='tight')
    plt.show()

def create_expected_results_plot():
    """Create a plot showing expected results from the control condition."""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Plot 1: Context Effect by Model Type
    model_types = ['High ToM\n(Hush-Qwen)', 'Medium ToM\n(OLMoE)', 'Low ToM\n(EXAONE)', 'No ToM\n(Llama)']
    context_effects = [0.78, 0.45, 0.23, 0.08]
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#E63946']
    
    bars = ax1.bar(model_types, context_effects, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax1.set_ylabel('Context Effect Magnitude', fontsize=12, fontweight='bold')
    ax1.set_title('Expected Context Sensitivity\n(Prediction Change When Context Swapped)', 
                  fontsize=14, fontweight='bold')
    ax1.set_ylim(0, 1)
    ax1.grid(True, alpha=0.3)
    
    # Add threshold lines
    ax1.axhline(y=0.5, color='green', linestyle='--', linewidth=2, alpha=0.7, label='Strong ToM Evidence')
    ax1.axhline(y=0.2, color='red', linestyle='--', linewidth=2, alpha=0.7, label='Weak ToM Evidence')
    ax1.legend()
    
    # Add value labels
    for bar, val in zip(bars, context_effects):
        ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.02,
                f'{val:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Plot 2: Original vs Swapped Accuracy
    scenarios = ['S1\nBluff→Value', 'S1\nValue→Bluff', 'S3\nBluff→Value', 'S3\nValue→Bluff']
    
    # High ToM model (should flip predictions)
    original_acc_high = [0.9, 0.85, 0.8, 0.9]  # Good original accuracy
    swapped_acc_high = [0.1, 0.15, 0.2, 0.1]   # Flipped when context swapped
    
    # Low ToM model (should ignore context)
    original_acc_low = [0.7, 0.8, 0.6, 0.75]   # Decent original accuracy  
    swapped_acc_low = [0.65, 0.75, 0.55, 0.7]  # Similar when context swapped
    
    x = np.arange(len(scenarios))
    width = 0.35
    
    ax2.bar(x - width/2, original_acc_high, width, label='High ToM: Original', 
            color='#2E86AB', alpha=0.8)
    ax2.bar(x + width/2, swapped_acc_high, width, label='High ToM: Swapped', 
            color='#2E86AB', alpha=0.4, hatch='///')
    
    ax2.bar(x - width/2, [-val for val in original_acc_low], width, label='Low ToM: Original', 
            color='#E63946', alpha=0.8)
    ax2.bar(x + width/2, [-val for val in swapped_acc_low], width, label='Low ToM: Swapped', 
            color='#E63946', alpha=0.4, hatch='///')
    
    ax2.set_ylabel('Accuracy (High ToM above, Low ToM below)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Context-Swapped Scenarios', fontsize=12, fontweight='bold')
    ax2.set_title('Expected Accuracy Patterns\n(Context Swapping Effect)', 
                  fontsize=14, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(scenarios)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='black', linewidth=1)
    
    plt.tight_layout()
    plt.savefig('expected_control_results.pdf', dpi=300, bbox_inches='tight')
    plt.show()

def create_context_control_summary_table():
    """Create a summary table for the control condition analysis."""
    
    latex_table = r"""
\begin{table}[htbp]
\centering
\caption{Context Swapping Control: Summary of Test Logic}
\label{tab:control_logic}
\begin{tabular}{@{}p{3cm}p{5cm}p{5cm}@{}}
\toprule
\textbf{Component} & \textbf{Theory of Mind Model} & \textbf{Poker Knowledge Model} \\
\midrule
\textbf{Context} & Uses opponent psychological & Ignores opponent psychology, \\
\textbf{Sensitivity} & profile to guide predictions & focuses on hand/bet mechanics \\
\addlinespace
\textbf{Expected} & Predictions flip when context & Predictions remain consistent \\
\textbf{Behavior} & is swapped (high sensitivity) & despite context swap (low sensitivity) \\
\addlinespace
\textbf{Statistical} & Large effect size (Cohen's d > 0.5) & Small effect size (Cohen's d < 0.2) \\
\textbf{Signature} & High variance in swapped scenarios & Low variance in swapped scenarios \\
\addlinespace
\textbf{Example} & S1\_Bluff (Aggressive) → BLUFF & S1\_Bluff → BLUFF (ignores swap) \\
\textbf{Predictions} & S1\_Bluff\_Swapped (Conservative) → VALUE & S1\_Bluff\_Swapped → BLUFF \\
\addlinespace
\textbf{Interpretation} & Evidence of mental state reasoning & Evidence of pattern matching only \\
\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item Note: This control condition isolates the contribution of opponent psychology
vs. poker-specific knowledge in model decision-making.
\end{tablenotes}
\end{table}
"""
    
    with open('context_control_summary_table.tex', 'w') as f:
        f.write(latex_table)
    
    print("✓ Created context_control_summary_table.tex")

def main():
    """Create all visualizations for the context control condition."""
    
    print("Creating Context Control Visualizations...")
    print("=" * 45)
    
    print("\n1. Creating Control Mechanism Diagram...")
    create_control_mechanism_diagram()
    
    print("2. Creating Expected Results Plot...")
    create_expected_results_plot()
    
    print("3. Creating Summary Table...")
    create_context_control_summary_table()
    
    print("\n✓ All visualizations created!")
    print("\nFiles generated:")
    print("- context_control_mechanism.pdf")
    print("- expected_control_results.pdf") 
    print("- context_control_summary_table.tex")
    
    print("\n🎯 This control condition is CRUCIAL for your paper because:")
    print("   • It addresses your professor's main criticism")
    print("   • It distinguishes ToM from poker knowledge")
    print("   • It provides strong evidence for your claims")
    print("   • It shows methodological rigor")

if __name__ == "__main__":
    main() 