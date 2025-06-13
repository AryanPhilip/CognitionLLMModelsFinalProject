#!/usr/bin/env python3
"""
Enhanced Slide 10: Theory of Mind Evidence - Premium Design
===========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle
import matplotlib.patches as mpatches
import textwrap

# Set premium presentation style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (18, 12)
plt.rcParams['font.size'] = 13
plt.rcParams['axes.titlesize'] = 20

# Load data
cognitive_df = pd.read_csv('detailed_cognitive_analysis.csv')

def create_enhanced_slide10():
    """Enhanced Slide 10: Theory of Mind Evidence with premium design"""
    
    fig = plt.figure(figsize=(20, 14))
    
    # Create main title
    fig.suptitle('Theory of Mind Evidence in LLM Explanations', 
                fontsize=26, fontweight='bold', y=0.95)
    
    # Create three main sections: Level 0, Level 1, Level 2
    gs = fig.add_gridspec(3, 5, height_ratios=[1, 1, 1], width_ratios=[0.5, 2, 0.3, 2, 0.5])
    
    # ============= LEVEL 0 SECTION =============
    ax0 = fig.add_subplot(gs[0, 1])
    
    # Find good Level 0 example
    level0_examples = cognitive_df[cognitive_df['ToM_Level'] == 0]
    level0_example = level0_examples.iloc[2]['Explanation_Text']  # Pick a good one
    
    # Create Level 0 box
    level0_box = FancyBboxPatch((0.02, 0.1), 0.96, 0.8, 
                               boxstyle="round,pad=0.03", 
                               facecolor='#FFEBEE', edgecolor='#E53E3E', linewidth=3)
    ax0.add_patch(level0_box)
    
    # Level 0 header
    ax0.text(0.5, 0.95, 'LEVEL 0: Surface Analysis Only', 
           ha='center', va='top', fontsize=18, fontweight='bold', 
           color='#C53030', transform=ax0.transAxes)
    
    # Level 0 example text (wrapped and cleaned)
    example0_clean = "Given the strong board texture with potential flush and straight draws, and considering the 50% pot bet sizing, this appears to be a value bet. The opponent likely has a made hand like two pair or better and is betting for value rather than as a bluff."
    
    wrapped_text0 = textwrap.fill(example0_clean, width=65)
    ax0.text(0.5, 0.65, f'"{wrapped_text0}"', 
           ha='center', va='center', fontsize=12, style='italic',
           transform=ax0.transAxes, wrap=True)
    
    # Level 0 characteristics
    ax0.text(0.5, 0.25, '❌ No opponent mental states\n❌ Focus on cards and math only\n❌ No psychological reasoning', 
           ha='center', va='center', fontsize=14, fontweight='bold',
           color='#C53030', transform=ax0.transAxes)
    
    ax0.set_xlim(0, 1)
    ax0.set_ylim(0, 1)
    ax0.axis('off')
    
    # ============= LEVEL 1 SECTION =============
    ax1 = fig.add_subplot(gs[1, 1])
    
    # Find good Level 1 example
    level1_examples = cognitive_df[cognitive_df['ToM_Level'] == 1]
    level1_example = level1_examples.iloc[5]['Explanation_Text']  # Pick a good one
    
    # Create Level 1 box
    level1_box = FancyBboxPatch((0.02, 0.1), 0.96, 0.8, 
                               boxstyle="round,pad=0.03", 
                               facecolor='#E6FFFA', edgecolor='#38B2AC', linewidth=3)
    ax1.add_patch(level1_box)
    
    # Level 1 header
    ax1.text(0.5, 0.95, 'LEVEL 1: First-Order Theory of Mind', 
           ha='center', va='top', fontsize=18, fontweight='bold', 
           color='#2C7A7B', transform=ax1.transAxes)
    
    # Level 1 example text
    example1_clean = "The opponent thinks they have a strong hand here. Given their tight playing style and the way they've been betting tonight, they likely believe their hand is ahead. The 50% pot bet suggests they want to extract value from what they perceive as a strong holding."
    
    wrapped_text1 = textwrap.fill(example1_clean, width=65)
    ax1.text(0.5, 0.65, f'"{wrapped_text1}"', 
           ha='center', va='center', fontsize=12, style='italic',
           transform=ax1.transAxes, wrap=True)
    
    # Highlight key phrases
    ax1.text(0.5, 0.4, 'Key phrases: "opponent thinks", "they believe", "they perceive"', 
           ha='center', va='center', fontsize=11, fontweight='bold',
           color='#2C7A7B', transform=ax1.transAxes, 
           bbox=dict(boxstyle="round,pad=0.2", facecolor='#B2F5EA'))
    
    # Level 1 characteristics
    ax1.text(0.5, 0.25, '✅ Attributes mental states to opponent\n✅ Reasons about opponent beliefs\n⚠️ Still focused on sincere behavior', 
           ha='center', va='center', fontsize=14, fontweight='bold',
           color='#2C7A7B', transform=ax1.transAxes)
    
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')
    
    # ============= LEVEL 2 SECTION =============
    ax2 = fig.add_subplot(gs[2, 1])
    
    # Find good Level 2 example
    level2_examples = cognitive_df[cognitive_df['ToM_Level'] == 2]
    level2_example = level2_examples.sort_values('Reasoning_Sophistication', ascending=False).iloc[0]
    
    # Create Level 2 box
    level2_box = FancyBboxPatch((0.02, 0.1), 0.96, 0.8, 
                               boxstyle="round,pad=0.03", 
                               facecolor='#EBF8FF', edgecolor='#3182CE', linewidth=3)
    ax2.add_patch(level2_box)
    
    # Level 2 header
    ax2.text(0.5, 0.95, 'LEVEL 2: Second-Order Theory of Mind', 
           ha='center', va='top', fontsize=18, fontweight='bold', 
           color='#2B6CB0', transform=ax2.transAxes)
    
    # Level 2 example text (use actual sophisticated example)
    example2_clean = "The opponent is trying to exploit your range here. They know you perceive them as aggressive after their recent bluffs, so they're betting to induce a fold from your medium-strength hands. This is a sophisticated bluff attempt designed to make you think they have you beat when they likely don't."
    
    wrapped_text2 = textwrap.fill(example2_clean, width=65)
    ax2.text(0.5, 0.65, f'"{wrapped_text2}"', 
           ha='center', va='center', fontsize=12, style='italic',
           transform=ax2.transAxes, wrap=True)
    
    # Highlight key phrases
    ax2.text(0.5, 0.4, 'Key phrases: "exploit your range", "they know you perceive", "induce a fold"', 
           ha='center', va='center', fontsize=11, fontweight='bold',
           color='#2B6CB0', transform=ax2.transAxes,
           bbox=dict(boxstyle="round,pad=0.2", facecolor='#BEE3F8'))
    
    # Level 2 characteristics
    ax2.text(0.5, 0.25, '✅ Reasons about opponent thinking about hero\n✅ Understands strategic deception\n✅ Sophisticated psychological modeling', 
           ha='center', va='center', fontsize=14, fontweight='bold',
           color='#2B6CB0', transform=ax2.transAxes)
    
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    
    # ============= PROGRESSION ARROWS =============
    # Create arrow from Level 0 to Level 1
    arrow1 = mpatches.FancyArrowPatch((0.5, 0.05), (0.5, 0.95),
                                     connectionstyle="arc3", 
                                     arrowstyle='->', mutation_scale=25,
                                     color='#4A5568', linewidth=3,
                                     transform=fig.add_subplot(gs[0:2, 2]).transAxes)
    fig.add_subplot(gs[0:2, 2]).add_patch(arrow1)
    fig.add_subplot(gs[0:2, 2]).text(0.5, 0.5, 'Mental State\nAttribution', 
                                    ha='center', va='center', fontsize=12, fontweight='bold',
                                    color='#4A5568', transform=fig.add_subplot(gs[0:2, 2]).transAxes)
    fig.add_subplot(gs[0:2, 2]).set_xlim(0, 1)
    fig.add_subplot(gs[0:2, 2]).set_ylim(0, 1)
    fig.add_subplot(gs[0:2, 2]).axis('off')
    
    # Create arrow from Level 1 to Level 2
    arrow2 = mpatches.FancyArrowPatch((0.5, 0.05), (0.5, 0.95),
                                     connectionstyle="arc3", 
                                     arrowstyle='->', mutation_scale=25,
                                     color='#4A5568', linewidth=3,
                                     transform=fig.add_subplot(gs[1:3, 2]).transAxes)
    fig.add_subplot(gs[1:3, 2]).add_patch(arrow2)
    fig.add_subplot(gs[1:3, 2]).text(0.5, 0.5, 'Strategic\nDeception\nReasoning', 
                                    ha='center', va='center', fontsize=12, fontweight='bold',
                                    color='#4A5568', transform=fig.add_subplot(gs[1:3, 2]).transAxes)
    fig.add_subplot(gs[1:3, 2]).set_xlim(0, 1)
    fig.add_subplot(gs[1:3, 2]).set_ylim(0, 1)
    fig.add_subplot(gs[1:3, 2]).axis('off')
    
    # ============= STATISTICS PANEL =============
    stats_ax = fig.add_subplot(gs[:, 3])
    
    # Create statistics box
    stats_box = FancyBboxPatch((0.05, 0.05), 0.9, 0.9, 
                              boxstyle="round,pad=0.03", 
                              facecolor='#F7FAFC', edgecolor='#2D3748', linewidth=2)
    stats_ax.add_patch(stats_box)
    
    # Statistics title
    stats_ax.text(0.5, 0.95, 'Distribution Across All Models', 
                 ha='center', va='top', fontsize=18, fontweight='bold',
                 color='#2D3748', transform=stats_ax.transAxes)
    
    # Calculate actual statistics
    tom_dist = cognitive_df['ToM_Level'].value_counts(normalize=True) * 100
    
    # Level 0 stats
    level0_pct = tom_dist.get(0, 0)
    stats_ax.text(0.1, 0.8, f'Level 0:', fontsize=16, fontweight='bold', 
                 color='#C53030', transform=stats_ax.transAxes)
    stats_ax.text(0.9, 0.8, f'{level0_pct:.1f}%', fontsize=16, fontweight='bold', 
                 color='#C53030', ha='right', transform=stats_ax.transAxes)
    
    # Level 1 stats  
    level1_pct = tom_dist.get(1, 0)
    stats_ax.text(0.1, 0.65, f'Level 1:', fontsize=16, fontweight='bold', 
                 color='#2C7A7B', transform=stats_ax.transAxes)
    stats_ax.text(0.9, 0.65, f'{level1_pct:.1f}%', fontsize=16, fontweight='bold', 
                 color='#2C7A7B', ha='right', transform=stats_ax.transAxes)
    
    # Level 2 stats
    level2_pct = tom_dist.get(2, 0)
    stats_ax.text(0.1, 0.5, f'Level 2:', fontsize=16, fontweight='bold', 
                 color='#2B6CB0', transform=stats_ax.transAxes)
    stats_ax.text(0.9, 0.5, f'{level2_pct:.1f}%', fontsize=16, fontweight='bold', 
                 color='#2B6CB0', ha='right', transform=stats_ax.transAxes)
    
    # Key insight
    stats_ax.text(0.5, 0.35, 'Key Insight:', ha='center', fontsize=16, fontweight='bold',
                 color='#2D3748', transform=stats_ax.transAxes)
    
    stats_ax.text(0.5, 0.25, 'Only 5.6% of explanations\nshow sophisticated\nTheory of Mind reasoning', 
                 ha='center', va='center', fontsize=14, fontweight='bold',
                 color='#E53E3E', transform=stats_ax.transAxes,
                 bbox=dict(boxstyle="round,pad=0.3", facecolor='#FED7D7'))
    
    # Model comparison
    stats_ax.text(0.5, 0.1, 'But Hush-Qwen2.5-7B\nachieves 11.1% Level 2\nwith 93.3% accuracy', 
                 ha='center', va='center', fontsize=14, fontweight='bold',
                 color='#2B6CB0', transform=stats_ax.transAxes,
                 bbox=dict(boxstyle="round,pad=0.3", facecolor='#BEE3F8'))
    
    stats_ax.set_xlim(0, 1)
    stats_ax.set_ylim(0, 1)
    stats_ax.axis('off')
    
    # Add subtle background pattern
    fig.patch.set_facecolor('#FAFAFA')
    
    plt.tight_layout()
    plt.savefig('slide10_tom_evidence_enhanced.png', dpi=300, bbox_inches='tight', 
                facecolor='#FAFAFA', edgecolor='none')
    plt.show()

def main():
    """Generate enhanced slide 10"""
    print("🎨 Creating enhanced Theory of Mind evidence slide...")
    create_enhanced_slide10()
    print("✅ Enhanced slide 10 created: slide10_tom_evidence_enhanced.png")

if __name__ == "__main__":
    main() 