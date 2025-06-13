#!/usr/bin/env python3
"""
Fix Slide 9: Corrected Deception Detection Bottleneck
=====================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle
import matplotlib.patches as mpatches

# Load data
cognitive_df = pd.read_csv('detailed_cognitive_analysis.csv')

def create_slide_9_bottleneck_fixed():
    """Slide 9: Deception Detection Bottleneck - CORRECTED"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Left: Overall context difficulty
    contexts = ['Value\nDetection', 'Bluff\nDetection']
    accuracies = [63.3, 40.6]
    colors = ['#4ECDC4', '#FF6B6B']
    
    bars = ax1.bar(contexts, accuracies, color=colors, alpha=0.8, edgecolor='white', linewidth=3)
    ax1.set_title('The Deception Detection Challenge', fontweight='bold', fontsize=18)
    ax1.set_ylabel('Overall Accuracy (%)', fontweight='bold')
    ax1.set_ylim(0, 80)
    ax1.axhline(y=50, color='black', linestyle='--', alpha=0.5, linewidth=2, label='Chance Level')
    
    # Add accuracy labels and difficulty gap
    for bar, acc in zip(bars, accuracies):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{acc}%', ha='center', va='bottom', fontweight='bold', fontsize=16)
    
    # Show the gap
    ax1.annotate('', xy=(1, 40.6), xytext=(1, 63.3),
                arrowprops=dict(arrowstyle='<->', color='red', lw=3))
    ax1.text(1.2, 52, '22.7%\nGAP', ha='center', va='center', 
           fontsize=14, fontweight='bold', color='red')
    
    ax1.legend()
    
    # Right: Model-specific performance heatmap - CORRECTED
    # Calculate actual performance from the data
    model_performance = cognitive_df.groupby(['Model', 'Context_Type'])['Is_Correct'].mean() * 100
    
    # Create the correct data structure for heatmap
    models = ['Hush-Qwen2.5-7B', 'OLMoE-1B-7B-0125-Instruct', 'EXAONE-3.5-2.4B-Instruct', 'Llama-3.2-SUN-HDIC-1B-Ins']
    contexts = ['Bluff', 'Value']
    
    # Create matrix with correct values
    perf_matrix = np.zeros((len(models), len(contexts)))
    for i, model in enumerate(models):
        for j, context in enumerate(contexts):
            if (model, context) in model_performance.index:
                perf_matrix[i, j] = model_performance[(model, context)]
    
    # Create DataFrame for heatmap
    perf_df = pd.DataFrame(perf_matrix, 
                          index=['Hush-Qwen', 'OLMoE', 'EXAONE', 'Llama-1B'],
                          columns=['Bluff', 'Value'])
    
    sns.heatmap(perf_df, annot=True, fmt='.1f', cmap='RdYlGn', 
                ax=ax2, cbar_kws={'label': 'Accuracy (%)'}, 
                vmin=0, vmax=100)
    ax2.set_title('Model × Context Performance', fontweight='bold', fontsize=18)
    ax2.set_xlabel('Context Type', fontweight='bold')
    ax2.set_ylabel('Model', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('slide9_bottleneck_corrected.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    
    # Print the actual values for verification
    print("=== CORRECTED VALUES ===")
    print(perf_df)
    print(f"\nHush-Qwen: {perf_df.loc['Hush-Qwen', 'Bluff']:.1f}% bluff, {perf_df.loc['Hush-Qwen', 'Value']:.1f}% value")

def main():
    """Generate corrected slide 9"""
    print("🔧 Creating CORRECTED Slide 9...")
    create_slide_9_bottleneck_fixed()
    print("✅ Corrected slide 9 created: slide9_bottleneck_corrected.png")

if __name__ == "__main__":
    main() 