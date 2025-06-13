#!/usr/bin/env python3
"""
Additional Presentation Visuals: Specific slide visualizations
=============================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.patches as mpatches

# Set presentation style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 14
plt.rcParams['axes.titlesize'] = 18

# Load data
results_df = pd.read_csv('poker_tom_results_20250602_081719.csv')
cognitive_df = pd.read_csv('detailed_cognitive_analysis.csv')

def create_slide_3_stimulus():
    """Slide 3: Sample Stimulus - Poker table visualization"""
    
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Create poker table (green ellipse)
    table = mpatches.Ellipse((0.5, 0.5), 0.8, 0.6, 
                            facecolor='darkgreen', alpha=0.3, edgecolor='black', linewidth=3)
    ax.add_patch(table)
    
    # Hero position (bottom)
    hero_box = FancyBboxPatch((0.4, 0.1), 0.2, 0.15, 
                             boxstyle="round,pad=0.02", 
                             facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(hero_box)
    ax.text(0.5, 0.175, 'HERO\nA♠ K♠', ha='center', va='center', 
           fontsize=16, fontweight='bold')
    
    # Opponent position (top)
    opp_box = FancyBboxPatch((0.4, 0.75), 0.2, 0.15, 
                            boxstyle="round,pad=0.02", 
                            facecolor='lightcoral', edgecolor='red', linewidth=2)
    ax.add_patch(opp_box)
    ax.text(0.5, 0.825, 'OPPONENT\n??', ha='center', va='center', 
           fontsize=16, fontweight='bold')
    
    # Board cards (center)
    cards = ['Q♠', 'J♠', '2♥']
    for i, card in enumerate(cards):
        card_x = 0.35 + i * 0.1
        card_box = Rectangle((card_x, 0.45), 0.08, 0.1, 
                           facecolor='white', edgecolor='black', linewidth=2)
        ax.add_patch(card_box)
        ax.text(card_x + 0.04, 0.5, card, ha='center', va='center', 
               fontsize=14, fontweight='bold')
    
    # Pot size
    ax.text(0.5, 0.35, 'POT: $150', ha='center', va='center', 
           fontsize=18, fontweight='bold', 
           bbox=dict(boxstyle="round,pad=0.3", facecolor='gold', alpha=0.7))
    
    # Opponent bet
    ax.text(0.5, 0.65, 'BET: $75 (50% pot)', ha='center', va='center', 
           fontsize=16, fontweight='bold',
           bbox=dict(boxstyle="round,pad=0.3", facecolor='orange', alpha=0.7))
    
    # Context bubble
    context_text = "CONTEXT:\nOpponent has shown\naggressive bluffs tonight"
    ax.text(0.85, 0.7, context_text, ha='center', va='center', 
           fontsize=12, fontweight='bold',
           bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', 
                    edgecolor='orange', linewidth=2))
    
    # Question
    ax.text(0.5, 0.02, 'Is this opponent bet a BLUFF or VALUE?', 
           ha='center', va='center', fontsize=20, fontweight='bold',
           bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.8))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('Sample Poker Stimulus: Theory of Mind Challenge', 
                fontsize=22, fontweight='bold', pad=30)
    ax.axis('off')
    
    plt.savefig('slide3_stimulus.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

def create_slide_4_bluff_scenario():
    """Slide 4: Bluff Scenario Example"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))
    
    # Left side: Scenario setup (similar to slide 3 but red-tinted)
    # Table
    table = mpatches.Ellipse((0.5, 0.5), 0.8, 0.6, 
                            facecolor='mistyrose', alpha=0.5, edgecolor='red', linewidth=3)
    ax1.add_patch(table)
    
    # Hero
    hero_box = FancyBboxPatch((0.4, 0.1), 0.2, 0.15, 
                             boxstyle="round,pad=0.02", 
                             facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax1.add_patch(hero_box)
    ax1.text(0.5, 0.175, 'HERO\nA♠ K♠', ha='center', va='center', 
           fontsize=14, fontweight='bold')
    
    # Board
    cards = ['Q♠', 'J♠', '2♥']
    for i, card in enumerate(cards):
        card_x = 0.35 + i * 0.1
        card_box = Rectangle((card_x, 0.45), 0.08, 0.1, 
                           facecolor='white', edgecolor='black', linewidth=2)
        ax1.add_patch(card_box)
        ax1.text(card_x + 0.04, 0.5, card, ha='center', va='center', 
               fontsize=12, fontweight='bold')
    
    # Bluff context
    ax1.text(0.5, 0.8, 'BLUFF CONTEXT:\n"Opponent has bluffed\n3 times tonight"', 
           ha='center', va='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle="round,pad=0.3", facecolor='lightcoral', alpha=0.8))
    
    ax1.text(0.5, 0.65, 'BET: $75', ha='center', va='center', 
           fontsize=14, fontweight='bold')
    
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_title('Bluff-Suggestive Context', fontweight='bold', color='red')
    ax1.axis('off')
    
    # Right side: Model responses
    models = ['Hush-Qwen', 'OLMoE', 'EXAONE', 'Llama-1B']
    predictions = ['BLUFF ✓', 'BLUFF ✓', 'VALUE ✗', 'VALUE ✗']
    colors = ['green', 'green', 'red', 'red']
    
    y_positions = [0.8, 0.6, 0.4, 0.2]
    
    for model, pred, color, y in zip(models, predictions, colors, y_positions):
        ax2.text(0.1, y, f'{model}:', fontsize=14, fontweight='bold')
        ax2.text(0.6, y, pred, fontsize=14, fontweight='bold', color=color)
        
    ax2.text(0.5, 0.95, 'Model Predictions', ha='center', fontsize=16, fontweight='bold')
    ax2.text(0.5, 0.05, 'Accuracy: 50%\n(2/4 correct)', ha='center', fontsize=14, 
           bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))
    
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    
    plt.tight_layout()
    plt.savefig('slide4_bluff_scenario.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

def create_slide_5_value_scenario():
    """Slide 5: Value Scenario Example"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))
    
    # Left side: Scenario setup (green-tinted for value)
    table = mpatches.Ellipse((0.5, 0.5), 0.8, 0.6, 
                            facecolor='lightgreen', alpha=0.3, edgecolor='green', linewidth=3)
    ax1.add_patch(table)
    
    # Hero
    hero_box = FancyBboxPatch((0.4, 0.1), 0.2, 0.15, 
                             boxstyle="round,pad=0.02", 
                             facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax1.add_patch(hero_box)
    ax1.text(0.5, 0.175, 'HERO\nA♠ K♠', ha='center', va='center', 
           fontsize=14, fontweight='bold')
    
    # Board
    cards = ['Q♠', 'J♠', '2♥']
    for i, card in enumerate(cards):
        card_x = 0.35 + i * 0.1
        card_box = Rectangle((card_x, 0.45), 0.08, 0.1, 
                           facecolor='white', edgecolor='black', linewidth=2)
        ax1.add_patch(card_box)
        ax1.text(card_x + 0.04, 0.5, card, ha='center', va='center', 
               fontsize=12, fontweight='bold')
    
    # Value context
    ax1.text(0.5, 0.8, 'VALUE CONTEXT:\n"Opponent plays tight,\nrarely bluffs"', 
           ha='center', va='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.8))
    
    ax1.text(0.5, 0.65, 'BET: $75', ha='center', va='center', 
           fontsize=14, fontweight='bold')
    
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_title('Value-Suggestive Context', fontweight='bold', color='green')
    ax1.axis('off')
    
    # Right side: Model responses  
    models = ['Hush-Qwen', 'OLMoE', 'EXAONE', 'Llama-1B']
    predictions = ['VALUE ✓', 'VALUE ✓', 'VALUE ✓', 'BLUFF ✗']
    colors = ['green', 'green', 'green', 'red']
    
    y_positions = [0.8, 0.6, 0.4, 0.2]
    
    for model, pred, color, y in zip(models, predictions, colors, y_positions):
        ax2.text(0.1, y, f'{model}:', fontsize=14, fontweight='bold')
        ax2.text(0.6, y, pred, fontsize=14, fontweight='bold', color=color)
        
    ax2.text(0.5, 0.95, 'Model Predictions', ha='center', fontsize=16, fontweight='bold')
    ax2.text(0.5, 0.05, 'Accuracy: 75%\n(3/4 correct)', ha='center', fontsize=14, 
           bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.7))
    
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    
    plt.tight_layout()
    plt.savefig('slide5_value_scenario.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

def create_slide_9_bottleneck():
    """Slide 9: Deception Detection Bottleneck"""
    
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
    
    # Right: Model-specific performance heatmap - FIXED DATA SOURCE
    # Calculate performance from cognitive_df correctly
    model_context_perf = cognitive_df.groupby(['Model', 'Context_Type'])['Is_Correct'].mean().unstack()
    
    # Shorten model names for display
    model_names = ['Hush-Qwen', 'OLMoE', 'EXAONE', 'Llama-1B']
    model_context_perf.index = model_names
    
    sns.heatmap(model_context_perf * 100, annot=True, fmt='.1f', cmap='RdYlGn', 
                ax=ax2, cbar_kws={'label': 'Accuracy (%)'}, 
                vmin=0, vmax=100)
    ax2.set_title('Model × Context Performance', fontweight='bold', fontsize=18)
    ax2.set_xlabel('Context Type', fontweight='bold')
    ax2.set_ylabel('Model', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('slide9_bottleneck.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

def create_slide_10_tom_evidence():
    """Slide 10: Theory of Mind Evidence Examples"""
    
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # Find best examples of different ToM levels
    level_0_example = cognitive_df[cognitive_df['ToM_Level'] == 0].iloc[0]
    level_2_example = cognitive_df[cognitive_df['ToM_Level'] == 2].iloc[0]
    
    # Create comparison boxes
    # Level 0 box (top)
    level0_box = FancyBboxPatch((0.05, 0.55), 0.9, 0.4, 
                               boxstyle="round,pad=0.02", 
                               facecolor='#FFE5E5', edgecolor='#FF6B6B', linewidth=3)
    ax.add_patch(level0_box)
    
    ax.text(0.5, 0.9, 'LEVEL 0: No Theory of Mind', ha='center', va='center', 
           fontsize=18, fontweight='bold', color='#CC0000')
    
    # Truncate example text
    level0_text = level_0_example['Explanation_Text'][:200] + "..."
    ax.text(0.5, 0.75, f'Example: "{level0_text}"', ha='center', va='center', 
           fontsize=12, wrap=True, style='italic')
    
    ax.text(0.5, 0.6, '❌ No opponent mental state attribution\n❌ Focus on cards/math only', 
           ha='center', va='center', fontsize=14, fontweight='bold')
    
    # Level 2 box (bottom)
    level2_box = FancyBboxPatch((0.05, 0.05), 0.9, 0.4, 
                               boxstyle="round,pad=0.02", 
                               facecolor='#E5F4FF', edgecolor='#45B7D1', linewidth=3)
    ax.add_patch(level2_box)
    
    ax.text(0.5, 0.4, 'LEVEL 2: Sophisticated Theory of Mind', ha='center', va='center', 
           fontsize=18, fontweight='bold', color='#0066CC')
    
    # Truncate example text
    level2_text = level_2_example['Explanation_Text'][:200] + "..."
    ax.text(0.5, 0.25, f'Example: "{level2_text}"', ha='center', va='center', 
           fontsize=12, wrap=True, style='italic')
    
    ax.text(0.5, 0.1, '✅ "Opponent thinks..." reasoning\n✅ "Exploit your range" strategy\n✅ Second-order mental modeling', 
           ha='center', va='center', fontsize=14, fontweight='bold')
    
    # Title and subtitle
    ax.text(0.5, 0.98, 'Theory of Mind Evidence in LLM Explanations', 
           ha='center', va='center', fontsize=22, fontweight='bold')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.savefig('slide10_tom_evidence.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

def main():
    """Generate additional presentation visuals"""
    print("🎨 Creating additional presentation visuals...")
    
    create_slide_3_stimulus()
    print("✅ Slide 3: Sample Stimulus created")
    
    create_slide_4_bluff_scenario()
    print("✅ Slide 4: Bluff Scenario created")
    
    create_slide_5_value_scenario()
    print("✅ Slide 5: Value Scenario created")
    
    create_slide_9_bottleneck()
    print("✅ Slide 9: Deception Bottleneck created")
    
    create_slide_10_tom_evidence()
    print("✅ Slide 10: ToM Evidence created")
    
    print("\n🎯 Additional presentation visuals complete!")
    print("Files generated:")
    print("- slide3_stimulus.png")
    print("- slide4_bluff_scenario.png")
    print("- slide5_value_scenario.png")
    print("- slide9_bottleneck.png")
    print("- slide10_tom_evidence.png")

if __name__ == "__main__":
    main() 