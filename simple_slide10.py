#!/usr/bin/env python3
"""
Simple Slide 10: Theory of Mind Evidence - Clean Bullet Point Design
=====================================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.patches as mpatches

# Set clean presentation style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.size'] = 14
plt.rcParams['axes.titlesize'] = 20

# Load data
cognitive_df = pd.read_csv('detailed_cognitive_analysis.csv')

def create_simple_slide10():
    """Simple Slide 10: Theory of Mind Evidence with bullet points"""
    
    fig, (ax_visual, ax_text) = plt.subplots(1, 2, figsize=(18, 10), gridspec_kw={'width_ratios': [1, 1.2]})
    fig.suptitle('Theory of Mind Evidence in LLM Explanations', 
                fontsize=24, fontweight='bold', y=0.95)
    
    # ============= LEFT SIDE: SIMPLE VISUAL =============
    
    # Calculate ToM distribution
    tom_dist = cognitive_df['ToM_Level'].value_counts(normalize=True) * 100
    tom_counts = cognitive_df['ToM_Level'].value_counts()
    
    # Create a simple pie chart
    levels = ['Level 0\n(Surface)', 'Level 1\n(1st Order)', 'Level 2\n(2nd Order)']
    percentages = [tom_dist.get(0, 0), tom_dist.get(1, 0), tom_dist.get(2, 0)]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    wedges, texts, autotexts = ax_visual.pie(percentages, labels=levels, colors=colors, 
                                            autopct='%1.1f%%', startangle=90,
                                            textprops={'fontsize': 12, 'fontweight': 'bold'})
    
    # Enhance the pie chart
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(14)
    
    ax_visual.set_title('Distribution of ToM Levels\nAcross All LLM Responses', 
                       fontsize=16, fontweight='bold', pad=20)
    
    # ============= RIGHT SIDE: BULLET POINTS =============
    
    ax_text.axis('off')
    
    # Main evidence points
    evidence_text = """
THEORY OF MIND EVIDENCE:

• Mental State Attribution (64.7%)
  - LLMs attribute beliefs, intentions to opponents
  - "The opponent thinks they have a strong hand"
  - "They believe their hand is ahead"

• Strategic Reasoning (5.6% advanced)
  - Recognition of deceptive intentions
  - "Trying to exploit your perceived range" 
  - "Betting to induce folds"

• Context Integration Drives Performance
  - r = 0.420 correlation with accuracy
  - Sophisticated reasoning = higher accuracy
  - Bluff detection much harder than value

• Model Hierarchy Emerges
  - Hush-Qwen2.5: 93.3% accuracy, 11.1% Level 2
  - Clear cognitive sophistication differences
  - Better ToM = Better performance

• Deception as Cognitive Bottleneck
  - 40.6% vs 63.3% accuracy (bluff vs value)
  - Requires second-order reasoning
  - Separates advanced from basic models
"""
    
    ax_text.text(0.05, 0.95, evidence_text, 
                ha='left', va='top', fontsize=12, 
                transform=ax_text.transAxes,
                bbox=dict(boxstyle="round,pad=0.5", facecolor='#F8F9FA', 
                         edgecolor='#E9ECEF', linewidth=2))
    
    # Add key insight box at bottom
    insight_text = "KEY INSIGHT: LLMs show measurable Theory of Mind capabilities,\nwith deception detection serving as the ultimate cognitive test"
    
    ax_text.text(0.5, 0.15, insight_text, 
                ha='center', va='center', fontsize=14, fontweight='bold',
                transform=ax_text.transAxes, color='#2C3E50',
                bbox=dict(boxstyle="round,pad=0.4", facecolor='#E3F2FD', 
                         edgecolor='#1976D2', linewidth=3))
    
    plt.tight_layout()
    plt.savefig('slide10_tom_evidence_simple.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.show()

def main():
    """Generate simple slide 10"""
    print("🎨 Creating simple Theory of Mind evidence slide...")
    create_simple_slide10()
    print("✅ Simple slide 10 created: slide10_tom_evidence_simple.png")

if __name__ == "__main__":
    main() 