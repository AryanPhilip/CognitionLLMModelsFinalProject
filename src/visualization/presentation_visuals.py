#!/usr/bin/env python3
"""
Presentation Visuals: Clean, Focused Charts for Technical Slides
===============================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set presentation style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 14
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['legend.fontsize'] = 14

# Load data
results_df = pd.read_csv('poker_tom_results_20250602_081719.csv')
cognitive_df = pd.read_csv('detailed_cognitive_analysis.csv')

def create_slide_1_tom_challenge():
    """Slide 1: The Theory of Mind Challenge - Simple concept visualization"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Left: ToM Levels
    tom_levels = ['Level 0\n(None)', 'Level 1\n(First-order)', 'Level 2\n(Second-order)']
    tom_percentages = [29.7, 64.7, 5.6]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    bars = ax1.bar(tom_levels, tom_percentages, color=colors, alpha=0.8, edgecolor='white', linewidth=2)
    ax1.set_title('Theory of Mind Levels in LLM Explanations', fontweight='bold', pad=20)
    ax1.set_ylabel('Percentage of Explanations', fontweight='bold')
    ax1.set_ylim(0, 70)
    
    # Add percentage labels on bars
    for bar, pct in zip(bars, tom_percentages):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{pct}%', ha='center', va='bottom', fontweight='bold', fontsize=16)
    
    # Right: Bluff vs Value Difficulty
    contexts = ['Value\nDetection', 'Bluff\nDetection']
    accuracies = [63.3, 40.6]
    colors_bv = ['#4ECDC4', '#FF6B6B']
    
    bars = ax2.bar(contexts, accuracies, color=colors_bv, alpha=0.8, edgecolor='white', linewidth=2)
    ax2.set_title('Deception Detection Challenge', fontweight='bold', pad=20)
    ax2.set_ylabel('Accuracy (%)', fontweight='bold')
    ax2.set_ylim(0, 70)
    ax2.axhline(y=50, color='black', linestyle='--', alpha=0.5, label='Chance Level')
    
    # Add accuracy labels
    for bar, acc in zip(bars, accuracies):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{acc}%', ha='center', va='bottom', fontweight='bold', fontsize=16)
    
    ax2.legend()
    plt.tight_layout()
    plt.savefig('slide1_tom_challenge.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

def create_slide_2_framework():
    """Slide 2: Theoretical Framework - Clean ToM hierarchy"""
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Create a stepped visualization of ToM levels
    levels = ['Level 0\n"Board suggests flush"', 
              'Level 1\n"Opponent thinks they have\na strong hand"',
              'Level 2\n"Opponent is trying to\nexploit my range"']
    
    y_positions = [0.2, 0.5, 0.8]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    for i, (level, y, color) in enumerate(zip(levels, y_positions, colors)):
        # Draw boxes
        rect = plt.Rectangle((0.1, y-0.08), 0.8, 0.16, 
                           facecolor=color, alpha=0.3, edgecolor=color, linewidth=3)
        ax.add_patch(rect)
        
        # Add text
        ax.text(0.5, y, level, ha='center', va='center', fontsize=16, fontweight='bold')
        
        # Add arrows between levels
        if i < len(levels) - 1:
            ax.arrow(0.5, y+0.08, 0, 0.14, head_width=0.03, head_length=0.02, 
                    fc='gray', ec='gray', alpha=0.7)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('Theory of Mind Complexity Hierarchy', fontsize=20, fontweight='bold', pad=30)
    ax.axis('off')
    
    plt.savefig('slide2_framework.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

def create_slide_6_design():
    """Slide 6: Experimental Design - Clean methodology overview"""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Top left: Sample composition
    models = ['Hush-Qwen2.5-7B', 'OLMoE-1B-7B', 'EXAONE-3.5-2.4B', 'Llama-1B']
    sample_sizes = [90, 90, 90, 90]
    
    ax1.bar(range(len(models)), sample_sizes, color=['#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'])
    ax1.set_title('Sample Composition', fontweight='bold')
    ax1.set_ylabel('Responses per Model')
    ax1.set_xticks(range(len(models)))
    ax1.set_xticklabels([m.split('-')[0] for m in models], rotation=45)
    
    # Top right: Context distribution
    contexts = ['Bluff\nContext', 'Value\nContext']
    context_counts = [180, 180]
    
    ax2.pie(context_counts, labels=contexts, autopct='%1.0f%%', startangle=90,
           colors=['#FF6B6B', '#4ECDC4'])
    ax2.set_title('Context Distribution', fontweight='bold')
    
    # Bottom left: Stimulus parameters
    parameters = ['Scenarios', 'Contexts', 'Models', 'Runs', 'Total']
    values = [15, 2, 4, 3, 360]
    
    bars = ax3.barh(parameters, values, color=['#45B7D1', '#4ECDC4', '#96CEB4', '#FFEAA7', '#DDA0DD'])
    ax3.set_title('Experimental Parameters', fontweight='bold')
    ax3.set_xlabel('Count')
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, values)):
        ax3.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
                str(val), va='center', fontweight='bold')
    
    # Bottom right: Temperature and token settings
    ax4.text(0.5, 0.7, 'Generation Settings', ha='center', fontsize=18, fontweight='bold')
    ax4.text(0.5, 0.5, 'Temperature: 0.3\nMax Tokens: 350\nRuns per stimulus: 3', 
            ha='center', va='center', fontsize=14,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.5))
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.axis('off')
    
    plt.tight_layout()
    plt.savefig('slide6_design.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

def create_slide_7_results():
    """Slide 7: Main Results - Performance comparison"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Left: Model accuracy comparison
    models = ['Hush-Qwen2.5-7B', 'OLMoE-1B-7B', 'EXAONE-3.5-2.4B', 'Llama-1B']
    accuracies = [93.3, 57.8, 44.4, 12.2]
    colors = ['#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
    
    bars = ax1.bar(range(len(models)), accuracies, color=colors, alpha=0.8, edgecolor='white', linewidth=2)
    ax1.set_title('Model Performance Comparison', fontweight='bold', pad=20)
    ax1.set_ylabel('Accuracy (%)', fontweight='bold')
    ax1.set_xticks(range(len(models)))
    ax1.set_xticklabels([m.split('-')[0] for m in models], rotation=45)
    ax1.axhline(y=50, color='red', linestyle='--', alpha=0.7, label='Chance Level')
    ax1.set_ylim(0, 100)
    
    # Add accuracy labels
    for bar, acc in zip(bars, accuracies):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{acc}%', ha='center', va='bottom', fontweight='bold', fontsize=14)
    
    ax1.legend()
    
    # Right: Cognitive sophistication vs accuracy
    cog_scores = cognitive_df.groupby('Model').agg({
        'ToM_Level': 'mean',
        'Is_Correct': 'mean'
    }).reset_index()
    
    # Map model names
    model_mapping = {
        'Hush-Qwen2.5-7B': 'Hush-Qwen',
        'OLMoE-1B-7B-0125-Instruct': 'OLMoE',
        'EXAONE-3.5-2.4B-Instruct': 'EXAONE',
        'Llama-3.2-SUN-HDIC-1B-Ins': 'Llama-1B'
    }
    cog_scores['Model_Short'] = cog_scores['Model'].map(model_mapping)
    
    scatter = ax2.scatter(cog_scores['ToM_Level'], cog_scores['Is_Correct']*100, 
                         s=200, alpha=0.7, c=colors)
    
    # Add model labels
    for i, row in cog_scores.iterrows():
        ax2.annotate(row['Model_Short'], 
                    (row['ToM_Level'], row['Is_Correct']*100),
                    xytext=(5, 5), textcoords='offset points', fontweight='bold')
    
    ax2.set_title('ToM Level vs Performance', fontweight='bold', pad=20)
    ax2.set_xlabel('Average Theory of Mind Level', fontweight='bold')
    ax2.set_ylabel('Accuracy (%)', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('slide7_results.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

def create_slide_8_cognitive():
    """Slide 8: Cognitive Analysis - ToM patterns"""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Top left: ToM level distribution by model
    tom_by_model = cognitive_df.groupby(['Model', 'ToM_Level']).size().unstack(fill_value=0)
    tom_by_model_pct = tom_by_model.div(tom_by_model.sum(axis=1), axis=0) * 100
    
    model_short = {
        'Hush-Qwen2.5-7B': 'Hush-Qwen',
        'OLMoE-1B-7B-0125-Instruct': 'OLMoE',
        'EXAONE-3.5-2.4B-Instruct': 'EXAONE',
        'Llama-3.2-SUN-HDIC-1B-Ins': 'Llama-1B'
    }
    tom_by_model_pct.index = [model_short[idx] for idx in tom_by_model_pct.index]
    
    tom_by_model_pct.plot(kind='bar', stacked=True, ax=ax1, 
                         color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    ax1.set_title('ToM Level Distribution by Model', fontweight='bold')
    ax1.set_ylabel('Percentage of Explanations')
    ax1.legend(['Level 0', 'Level 1', 'Level 2'], loc='upper right')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
    
    # Top right: Bluff vs Value ToM requirements
    context_tom = cognitive_df.groupby('Context_Type')['ToM_Level'].mean()
    
    bars = ax2.bar(context_tom.index, context_tom.values, 
                  color=['#FF6B6B', '#4ECDC4'], alpha=0.8)
    ax2.set_title('ToM Requirements by Context', fontweight='bold')
    ax2.set_ylabel('Average ToM Level')
    
    for bar, val in zip(bars, context_tom.values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{val:.3f}', ha='center', va='bottom', fontweight='bold')
    
    # Bottom left: Cognitive factors correlation with accuracy
    corr_factors = ['Context_Integration_Score', 'Reasoning_Sophistication', 
                   'ToM_Level', 'Opponent_Psychology', 'Strategic_Reasoning_Score']
    correlations = cognitive_df[corr_factors + ['Is_Correct']].corr()['Is_Correct'][:-1].sort_values(ascending=True)
    
    bars = ax3.barh(range(len(correlations)), correlations.values, 
                   color=['#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#FFB6C1'])
    ax3.set_title('Cognitive Predictors of Accuracy', fontweight='bold')
    ax3.set_xlabel('Correlation with Accuracy')
    ax3.set_yticks(range(len(correlations)))
    ax3.set_yticklabels([name.replace('_', ' ').title() for name in correlations.index])
    
    # Add correlation values
    for bar, val in zip(bars, correlations.values):
        ax3.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
                f'{val:.3f}', va='center', fontweight='bold')
    
    # Bottom right: Successful vs failed bluff detection
    bluff_correct = cognitive_df[(cognitive_df['Context_Type'] == 'Bluff') & (cognitive_df['Is_Correct'] == 1)]
    bluff_incorrect = cognitive_df[(cognitive_df['Context_Type'] == 'Bluff') & (cognitive_df['Is_Correct'] == 0)]
    
    metrics = ['ToM Level', 'Psychology Score', 'Strategic Reasoning']
    success_scores = [bluff_correct['ToM_Level'].mean(), 
                     bluff_correct['Opponent_Psychology'].mean(),
                     bluff_correct['Strategic_Reasoning_Score'].mean()]
    fail_scores = [bluff_incorrect['ToM_Level'].mean(),
                  bluff_incorrect['Opponent_Psychology'].mean(), 
                  bluff_incorrect['Strategic_Reasoning_Score'].mean()]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    ax4.bar(x - width/2, success_scores, width, label='Successful', color='#4ECDC4', alpha=0.8)
    ax4.bar(x + width/2, fail_scores, width, label='Failed', color='#FF6B6B', alpha=0.8)
    
    ax4.set_title('Bluff Detection: Success vs Failure', fontweight='bold')
    ax4.set_ylabel('Average Score')
    ax4.set_xticks(x)
    ax4.set_xticklabels(metrics)
    ax4.legend()
    
    plt.tight_layout()
    plt.savefig('slide8_cognitive.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

def create_slide_9_implications():
    """Slide 9: Implications - Key takeaways visualization"""
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Create a conceptual diagram of implications
    implications = [
        "LLMs demonstrate\nmeasurable ToM",
        "Deception detection\nis cognitive bottleneck", 
        "Context integration\ndrives performance",
        "Model scale affects\nToM sophistication",
        "Rich context enables\nToM reasoning"
    ]
    
    # Position implications in a circle
    angles = np.linspace(0, 2*np.pi, len(implications), endpoint=False)
    radius = 0.3
    
    colors = ['#45B7D1', '#FF6B6B', '#4ECDC4', '#96CEB4', '#FFEAA7']
    
    for i, (impl, angle, color) in enumerate(zip(implications, angles, colors)):
        x = 0.5 + radius * np.cos(angle)
        y = 0.5 + radius * np.sin(angle)
        
        # Draw circle
        circle = plt.Circle((x, y), 0.12, facecolor=color, alpha=0.3, edgecolor=color, linewidth=3)
        ax.add_patch(circle)
        
        # Add text
        ax.text(x, y, impl, ha='center', va='center', fontsize=12, fontweight='bold', wrap=True)
        
        # Draw lines to center
        ax.plot([0.5, x], [0.5, y], color='gray', alpha=0.5, linewidth=2)
    
    # Center title
    ax.text(0.5, 0.5, 'AI Theory\nof Mind\nImplications', ha='center', va='center', 
           fontsize=16, fontweight='bold',
           bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='black', linewidth=2))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('Research Implications', fontsize=20, fontweight='bold', pad=30)
    ax.axis('off')
    
    plt.savefig('slide9_implications.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.show()

# Generate all presentation visuals
def main():
    print("🎨 Creating presentation-ready visualizations...")
    
    create_slide_1_tom_challenge()
    print("✅ Slide 1: ToM Challenge created")
    
    create_slide_2_framework()
    print("✅ Slide 2: Framework created")
    
    create_slide_6_design()
    print("✅ Slide 6: Experimental Design created")
    
    create_slide_7_results()
    print("✅ Slide 7: Main Results created")
    
    create_slide_8_cognitive()
    print("✅ Slide 8: Cognitive Analysis created")
    
    create_slide_9_implications()
    print("✅ Slide 9: Implications created")
    
    print("\n🎯 Presentation visuals complete!")
    print("Files generated:")
    print("- slide1_tom_challenge.png")
    print("- slide2_framework.png") 
    print("- slide6_design.png")
    print("- slide7_results.png")
    print("- slide8_cognitive.png")
    print("- slide9_implications.png")

if __name__ == "__main__":
    main() 