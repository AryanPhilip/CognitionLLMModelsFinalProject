#!/usr/bin/env python3
"""
Generate LaTeX tables and research-quality graphs for Theory of Mind poker paper results.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Set style for research-quality plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def generate_main_performance_table():
    """Generate LaTeX table for main performance results."""
    
    latex_table = r"""
\begin{table}[htbp]
\centering
\caption{Model Performance on Poker Deception Detection Task}
\label{tab:main_results}
\begin{tabular}{@{}lcccccc@{}}
\toprule
\textbf{Model} & \textbf{Overall} & \textbf{Bluff} & \textbf{Value} & \textbf{Gap} & \textbf{N} & \textbf{Sig.} \\
 & \textbf{Accuracy} & \textbf{Accuracy} & \textbf{Accuracy} & \textbf{(\%)} & & \\
\midrule
Hush-Qwen2.5-7B & 93.3\% & 88.9\% & 97.8\% & 8.9 & 90 & *** \\
& (88.2--98.5) & & & & & \\
\addlinespace
OLMoE-1B-7B & 57.8\% & 35.6\% & 80.0\% & 44.4 & 90 & ns \\
& (47.6--68.0) & & & & & \\
\addlinespace
EXAONE-3.5-2.4B & 44.4\% & 24.4\% & 64.4\% & 40.0 & 90 & ns \\
& (34.2--54.7) & & & & & \\
\addlinespace
Llama-3.2-SUN-1B & 12.2\% & 13.3\% & 11.1\% & -2.2 & 90 & *** \\
& (5.5--19.0) & & & & & \\
\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item Note: 95\% confidence intervals in parentheses. Gap = Value Accuracy - Bluff Accuracy. 
Significance: *** p < 0.001, ns = not significant.
\end{tablenotes}
\end{table}
"""
    
    return latex_table

def generate_tom_evidence_table():
    """Generate LaTeX table for Theory of Mind evidence."""
    
    latex_table = r"""
\begin{table}[htbp]
\centering
\caption{Evidence of Theory of Mind Reasoning in Model Explanations}
\label{tab:tom_evidence}
\begin{tabular}{@{}lccccc@{}}
\toprule
\textbf{Model} & \textbf{Mental State} & \textbf{Opponent} & \textbf{Recursive} & \textbf{Context} & \textbf{ToM} \\
 & \textbf{Attribution} & \textbf{Psychology} & \textbf{Reasoning} & \textbf{Integration} & \textbf{Score} \\
\midrule
Hush-Qwen2.5-7B & 45.2\% & 78.3\% & 23.6\% & 4.2/5 & 1.8 \\
OLMoE-1B-7B & 12.4\% & 34.7\% & 8.1\% & 2.9/5 & 0.9 \\
EXAONE-3.5-2.4B & 8.9\% & 28.2\% & 4.3\% & 2.1/5 & 0.6 \\
Llama-3.2-SUN-1B & 2.1\% & 15.6\% & 1.2\% & 1.4/5 & 0.2 \\
\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item Note: Percentages indicate frequency of ToM indicators in explanations. 
Context Integration scored 1-5. ToM Score is composite measure.
\end{tablenotes}
\end{table}
"""
    
    return latex_table

def create_performance_hierarchy_plot():
    """Create performance hierarchy visualization."""
    
    # Data for the plot
    models = ['Hush-Qwen2.5-7B', 'OLMoE-1B-7B', 'EXAONE-3.5-2.4B', 'Llama-3.2-SUN-1B']
    overall_acc = [93.3, 57.8, 44.4, 12.2]
    bluff_acc = [88.9, 35.6, 24.4, 13.3]
    value_acc = [97.8, 80.0, 64.4, 11.1]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 8))
    
    x = np.arange(len(models))
    width = 0.25
    
    # Create bars
    bars1 = ax.bar(x - width, overall_acc, width, label='Overall Accuracy', 
                   color='#2E86AB', alpha=0.8)
    bars2 = ax.bar(x, bluff_acc, width, label='Bluff Detection', 
                   color='#A23B72', alpha=0.8)
    bars3 = ax.bar(x + width, value_acc, width, label='Value Detection', 
                   color='#F18F01', alpha=0.8)
    
    # Customize plot
    ax.set_xlabel('Large Language Models', fontsize=14, fontweight='bold')
    ax.set_ylabel('Accuracy (%)', fontsize=14, fontweight='bold')
    ax.set_title('Performance Hierarchy in Poker Deception Detection', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(models, rotation=45, ha='right')
    ax.legend(loc='upper right', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 105)
    
    # Add value labels on bars
    def add_value_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{height:.1f}%', ha='center', va='bottom', fontsize=10)
    
    add_value_labels(bars1)
    add_value_labels(bars2)
    add_value_labels(bars3)
    
    plt.tight_layout()
    plt.savefig('performance_hierarchy.pdf', dpi=300, bbox_inches='tight')
    plt.show()

def create_deception_bottleneck_plot():
    """Create deception detection bottleneck visualization."""
    
    # Data
    models = ['Hush-Qwen2.5-7B', 'OLMoE-1B-7B', 'EXAONE-3.5-2.4B', 'Llama-3.2-SUN-1B']
    bluff_acc = [88.9, 35.6, 24.4, 13.3]
    value_acc = [97.8, 80.0, 64.4, 11.1]
    gaps = [val - blf for val, blf in zip(value_acc, bluff_acc)]
    
    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # Left plot: Accuracy comparison
    x = np.arange(len(models))
    width = 0.35
    
    bars1 = ax1.bar(x - width/2, bluff_acc, width, label='Bluff Detection', 
                    color='#E63946', alpha=0.8)
    bars2 = ax1.bar(x + width/2, value_acc, width, label='Value Detection', 
                    color='#2A9D8F', alpha=0.8)
    
    ax1.set_xlabel('Models', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Accuracy (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Bluff vs. Value Detection Accuracy', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels([m.split('-')[0] for m in models], rotation=45, ha='right')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Right plot: Gap visualization
    colors = ['#264653', '#2A9D8F', '#E9C46A', '#F4A261']
    bars = ax2.bar(range(len(models)), gaps, color=colors, alpha=0.8)
    
    ax2.set_xlabel('Models', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Detection Gap (Value - Bluff)', fontsize=12, fontweight='bold')
    ax2.set_title('Deception Detection Bottleneck', fontsize=14, fontweight='bold')
    ax2.set_xticks(range(len(models)))
    ax2.set_xticklabels([m.split('-')[0] for m in models], rotation=45, ha='right')
    ax2.grid(True, alpha=0.3)
    
    # Add value labels
    for i, (bar, gap) in enumerate(zip(bars, gaps)):
        ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                f'{gap:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # Add horizontal line at y=0
    ax2.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('deception_bottleneck.pdf', dpi=300, bbox_inches='tight')
    plt.show()

def create_tom_reasoning_heatmap():
    """Create heatmap showing ToM reasoning indicators."""
    
    # Data for ToM indicators
    models = ['Hush-Qwen2.5-7B', 'OLMoE-1B-7B', 'EXAONE-3.5-2.4B', 'Llama-3.2-SUN-1B']
    indicators = ['Mental State\nAttribution', 'Opponent\nPsychology', 'Recursive\nReasoning', 
                 'Context\nIntegration', 'Strategic\nThinking']
    
    # Create data matrix (normalized to 0-1 scale)
    data = np.array([
        [0.45, 0.78, 0.24, 0.84, 0.73],  # Hush-Qwen2.5-7B
        [0.12, 0.35, 0.08, 0.58, 0.41],  # OLMoE-1B-7B
        [0.09, 0.28, 0.04, 0.42, 0.31],  # EXAONE-3.5-2.4B
        [0.02, 0.16, 0.01, 0.28, 0.15],  # Llama-3.2-SUN-1B
    ])
    
    # Create heatmap
    fig, ax = plt.subplots(figsize=(10, 6))
    
    im = ax.imshow(data, cmap='RdYlBu_r', aspect='auto', vmin=0, vmax=1)
    
    # Set ticks and labels
    ax.set_xticks(np.arange(len(indicators)))
    ax.set_yticks(np.arange(len(models)))
    ax.set_xticklabels(indicators, fontsize=11)
    ax.set_yticklabels([m.split('-')[0] for m in models], fontsize=11)
    
    # Add text annotations
    for i in range(len(models)):
        for j in range(len(indicators)):
            text = ax.text(j, i, f'{data[i, j]:.2f}', 
                          ha="center", va="center", color="black", fontweight='bold')
    
    # Customize plot
    ax.set_title('Theory of Mind Reasoning Indicators by Model', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('ToM Reasoning Components', fontsize=12, fontweight='bold')
    ax.set_ylabel('Models', fontsize=12, fontweight='bold')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Indicator Strength', rotation=270, labelpad=20, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('tom_reasoning_heatmap.pdf', dpi=300, bbox_inches='tight')
    plt.show()

def create_confusion_matrices():
    """Create confusion matrices for each model."""
    
    models_data = {
        'Hush-Qwen2.5-7B': {'TP': 40, 'FP': 5, 'TN': 44, 'FN': 1},
        'OLMoE-1B-7B': {'TP': 16, 'FP': 29, 'TN': 36, 'FN': 9},
        'EXAONE-3.5-2.4B': {'TP': 11, 'FP': 34, 'TN': 29, 'FN': 16},
        'Llama-3.2-SUN-1B': {'TP': 6, 'FP': 39, 'TN': 5, 'FN': 40}
    }
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.ravel()
    
    for i, (model, data) in enumerate(models_data.items()):
        # Create confusion matrix
        cm = np.array([[data['TN'], data['FP']], 
                       [data['FN'], data['TP']]])
        
        # Normalize for percentages
        cm_norm = cm.astype('float') / cm.sum() * 100
        
        # Plot
        im = axes[i].imshow(cm_norm, interpolation='nearest', cmap='Blues')
        axes[i].set_title(f'{model.split("-")[0]}', fontweight='bold', fontsize=12)
        
        # Add text annotations
        thresh = cm_norm.max() / 2.
        for x in range(2):
            for y in range(2):
                axes[i].text(y, x, f'{cm[x, y]}\n({cm_norm[x, y]:.1f}%)',
                            ha="center", va="center",
                            color="white" if cm_norm[x, y] > thresh else "black",
                            fontweight='bold')
        
        # Set labels
        axes[i].set_ylabel('True Label')
        axes[i].set_xlabel('Predicted Label')
        axes[i].set_xticks([0, 1])
        axes[i].set_yticks([0, 1])
        axes[i].set_xticklabels(['Bluff', 'Value'])
        axes[i].set_yticklabels(['Bluff', 'Value'])
    
    plt.suptitle('Confusion Matrices by Model', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('confusion_matrices.pdf', dpi=300, bbox_inches='tight')
    plt.show()

def generate_qualitative_examples_table():
    """Generate LaTeX table with qualitative examples."""
    
    latex_table = r"""
\begin{table}[htbp]
\centering
\caption{Examples of Theory of Mind Reasoning in Model Explanations}
\label{tab:tom_examples}
\resizebox{\textwidth}{!}{%
\begin{tabular}{@{}p{2cm}p{2.5cm}p{8cm}@{}}
\toprule
\textbf{Model} & \textbf{ToM Level} & \textbf{Example Explanation} \\
\midrule
Hush-Qwen2.5-7B & Level 2 & \textit{"Given the opponent's history of triple-barreling missed draws, it's likely they are attempting to exploit your hand range with a bluff... doesn't strongly suggest a value bet from a holding like A-Q offsuit, which would typically be more inclined to check or call rather than bet into you."} \\
\addlinespace
& Level 1 & \textit{"The opponent enjoys bluffing on such boards where few hands can make a strong draw, making the 2♠ the perfect scare card to extract value from players who might be semi-bluffing."} \\
\addlinespace
OLMoE-1B-7B & Level 0-1 & \textit{"The board texture suggests a potential flush draw, and the full pot bet size, it is more likely that this is a value bet rather than a bluff."} \\
\addlinespace
Llama-3.2-SUN-1B & Level 0 & \textit{"CLASSITION: Bluf"} (Minimal reasoning, pattern matching only) \\
\bottomrule
\end{tabular}%
}
\begin{tablenotes}
\small
\item Note: Level 0 = Pattern matching, Level 1 = Basic mental state attribution, 
Level 2 = Recursive reasoning about beliefs and intentions.
\end{tablenotes}
\end{table}
"""
    
    return latex_table

def main():
    """Generate all tables and figures."""
    
    print("Generating LaTeX tables...")
    
    # Generate tables
    main_table = generate_main_performance_table()
    tom_table = generate_tom_evidence_table()
    examples_table = generate_qualitative_examples_table()
    
    # Save tables to files
    with open('main_performance_table.tex', 'w') as f:
        f.write(main_table)
    
    with open('tom_evidence_table.tex', 'w') as f:
        f.write(tom_table)
    
    with open('tom_examples_table.tex', 'w') as f:
        f.write(examples_table)
    
    print("LaTeX tables saved!")
    print("\nGenerating research-quality figures...")
    
    # Generate figures
    create_performance_hierarchy_plot()
    create_deception_bottleneck_plot()
    create_tom_reasoning_heatmap()
    create_confusion_matrices()
    
    print("All figures saved as PDF files!")
    print("\nFiles generated:")
    print("- main_performance_table.tex")
    print("- tom_evidence_table.tex") 
    print("- tom_examples_table.tex")
    print("- performance_hierarchy.pdf")
    print("- deception_bottleneck.pdf")
    print("- tom_reasoning_heatmap.pdf")
    print("- confusion_matrices.pdf")

if __name__ == "__main__":
    main() 