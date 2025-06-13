#!/usr/bin/env python3
"""
Premium Slide 10: Theory of Mind Evidence - Ultimate Design
============================================================
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
plt.rcParams['figure.figsize'] = (20, 14)
plt.rcParams['font.size'] = 14
plt.rcParams['axes.titlesize'] = 22
plt.rcParams['font.family'] = 'sans-serif'

# Load data
cognitive_df = pd.read_csv('detailed_cognitive_analysis.csv')

def create_premium_slide10():
    """Premium Slide 10: Theory of Mind Evidence with ultimate design"""
    
    fig = plt.figure(figsize=(22, 16))
    fig.patch.set_facecolor('#FFFFFF')
    
    # Create main title
    fig.suptitle('Theory of Mind Evidence in LLM Explanations', 
                fontsize=28, fontweight='bold', y=0.96, color='#1A202C')
    
    # Create layout
    gs = fig.add_gridspec(3, 4, height_ratios=[1, 1, 1], width_ratios=[2.5, 0.3, 2.5, 1.2],
                         hspace=0.15, wspace=0.1)
    
    # ============= LEVEL 0 SECTION =============
    ax0 = fig.add_subplot(gs[0, 0])
    
    # Create Level 0 box
    level0_box = FancyBboxPatch((0.05, 0.05), 0.9, 0.9, 
                               boxstyle="round,pad=0.04", 
                               facecolor='#FFF5F5', edgecolor='#E53E3E', linewidth=4)
    ax0.add_patch(level0_box)
    
    # Level 0 header
    header_box0 = FancyBboxPatch((0.1, 0.8), 0.8, 0.12, 
                                boxstyle="round,pad=0.02", 
                                facecolor='#E53E3E', edgecolor='none')
    ax0.add_patch(header_box0)
    ax0.text(0.5, 0.86, 'LEVEL 0: Surface Analysis', 
           ha='center', va='center', fontsize=16, fontweight='bold', 
           color='white', transform=ax0.transAxes)
    
    # Level 0 example text
    example0_text = '"Given the board texture with Q-J-2 and potential draws, the 50% pot bet sizing suggests a value bet. The opponent likely has a made hand like two pair or better and is betting for value rather than bluffing."'
    
    wrapped_text0 = textwrap.fill(example0_text, width=55)
    ax0.text(0.5, 0.55, wrapped_text0, 
           ha='center', va='center', fontsize=11, style='italic',
           transform=ax0.transAxes, color='#2D3748')
    
    # Level 0 characteristics
    ax0.text(0.5, 0.25, 'X  No opponent mental states\nX  Cards and math focus only\nX  No psychological reasoning', 
           ha='center', va='center', fontsize=12, fontweight='bold',
           color='#C53030', transform=ax0.transAxes)
    
    ax0.set_xlim(0, 1)
    ax0.set_ylim(0, 1)
    ax0.axis('off')
    
    # ============= LEVEL 1 SECTION =============
    ax1 = fig.add_subplot(gs[1, 0])
    
    # Create Level 1 box
    level1_box = FancyBboxPatch((0.05, 0.05), 0.9, 0.9, 
                               boxstyle="round,pad=0.04", 
                               facecolor='#F0FFF4', edgecolor='#38A169', linewidth=4)
    ax1.add_patch(level1_box)
    
    # Level 1 header
    header_box1 = FancyBboxPatch((0.1, 0.8), 0.8, 0.12, 
                                boxstyle="round,pad=0.02", 
                                facecolor='#38A169', edgecolor='none')
    ax1.add_patch(header_box1)
    ax1.text(0.5, 0.86, 'LEVEL 1: First-Order ToM', 
           ha='center', va='center', fontsize=16, fontweight='bold', 
           color='white', transform=ax1.transAxes)
    
    # Level 1 example text
    example1_text = '"The opponent thinks they have a strong hand here. Given their tight playing style, they likely believe their hand is ahead. The bet suggests they want to extract value from what they perceive as a strong holding."'
    
    wrapped_text1 = textwrap.fill(example1_text, width=55)
    ax1.text(0.5, 0.55, wrapped_text1, 
           ha='center', va='center', fontsize=11, style='italic',
           transform=ax1.transAxes, color='#2D3748')
    
    # Highlight key phrases
    ax1.text(0.5, 0.35, 'Key: "opponent thinks", "they believe", "they perceive"', 
           ha='center', va='center', fontsize=10, fontweight='bold',
           color='#276749', transform=ax1.transAxes, 
           bbox=dict(boxstyle="round,pad=0.2", facecolor='#C6F6D5'))
    
    # Level 1 characteristics
    ax1.text(0.5, 0.2, '✓  Mental state attribution\n✓  Opponent belief reasoning\n~  Sincere behavior focus', 
           ha='center', va='center', fontsize=12, fontweight='bold',
           color='#276749', transform=ax1.transAxes)
    
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')
    
    # ============= LEVEL 2 SECTION =============
    ax2 = fig.add_subplot(gs[2, 0])
    
    # Create Level 2 box
    level2_box = FancyBboxPatch((0.05, 0.05), 0.9, 0.9, 
                               boxstyle="round,pad=0.04", 
                               facecolor='#EBF8FF', edgecolor='#3182CE', linewidth=4)
    ax2.add_patch(level2_box)
    
    # Level 2 header
    header_box2 = FancyBboxPatch((0.1, 0.8), 0.8, 0.12, 
                                boxstyle="round,pad=0.02", 
                                facecolor='#3182CE', edgecolor='none')
    ax2.add_patch(header_box2)
    ax2.text(0.5, 0.86, 'LEVEL 2: Second-Order ToM', 
           ha='center', va='center', fontsize=16, fontweight='bold', 
           color='white', transform=ax2.transAxes)
    
    # Level 2 example text
    example2_text = '"The opponent is trying to exploit your range here. They know you perceive them as aggressive, so they\'re betting to induce folds from medium-strength hands. This is a sophisticated bluff designed to make you think they have you beat."'
    
    wrapped_text2 = textwrap.fill(example2_text, width=55)
    ax2.text(0.5, 0.55, wrapped_text2, 
           ha='center', va='center', fontsize=11, style='italic',
           transform=ax2.transAxes, color='#2D3748')
    
    # Highlight key phrases
    ax2.text(0.5, 0.35, 'Key: "exploit your range", "they know you perceive", "induce folds"', 
           ha='center', va='center', fontsize=10, fontweight='bold',
           color='#2C5282', transform=ax2.transAxes,
           bbox=dict(boxstyle="round,pad=0.2", facecolor='#BEE3F8'))
    
    # Level 2 characteristics
    ax2.text(0.5, 0.2, '✓  Second-order reasoning\n✓  Strategic deception\n✓  Sophisticated psychology', 
           ha='center', va='center', fontsize=12, fontweight='bold',
           color='#2C5282', transform=ax2.transAxes)
    
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    
    # ============= ARROWS =============
    # Arrow from Level 0 to Level 1
    arrow_ax1 = fig.add_subplot(gs[0:2, 1])
    arrow_ax1.annotate('', xy=(0.5, 0.9), xytext=(0.5, 0.1),
                      arrowprops=dict(arrowstyle='->', lw=4, color='#4A5568'))
    arrow_ax1.text(0.5, 0.5, 'Mental\nState\nAttribution', 
                  ha='center', va='center', fontsize=12, fontweight='bold',
                  color='#4A5568', transform=arrow_ax1.transAxes,
                  bbox=dict(boxstyle="round,pad=0.3", facecolor='#F7FAFC'))
    arrow_ax1.set_xlim(0, 1)
    arrow_ax1.set_ylim(0, 1)
    arrow_ax1.axis('off')
    
    # Arrow from Level 1 to Level 2
    arrow_ax2 = fig.add_subplot(gs[1:3, 1])
    arrow_ax2.annotate('', xy=(0.5, 0.9), xytext=(0.5, 0.1),
                      arrowprops=dict(arrowstyle='->', lw=4, color='#4A5568'))
    arrow_ax2.text(0.5, 0.5, 'Strategic\nDeception\nReasoning', 
                  ha='center', va='center', fontsize=12, fontweight='bold',
                  color='#4A5568', transform=arrow_ax2.transAxes,
                  bbox=dict(boxstyle="round,pad=0.3", facecolor='#F7FAFC'))
    arrow_ax2.set_xlim(0, 1)
    arrow_ax2.set_ylim(0, 1)
    arrow_ax2.axis('off')
    
    # ============= EVOLUTION VISUAL =============
    evolution_ax = fig.add_subplot(gs[:, 2])
    
    # Create evolution timeline
    evolution_box = FancyBboxPatch((0.05, 0.05), 0.9, 0.9, 
                                  boxstyle="round,pad=0.04", 
                                  facecolor='#FAFAFA', edgecolor='#2D3748', linewidth=3)
    evolution_ax.add_patch(evolution_box)
    
    evolution_ax.text(0.5, 0.95, 'Cognitive Evolution', 
                     ha='center', va='top', fontsize=18, fontweight='bold',
                     color='#2D3748', transform=evolution_ax.transAxes)
    
    # Brain evolution visualization
    brain_levels = ['Surface\nAnalysis', 'Mental State\nAttribution', 'Strategic\nDeception']
    brain_colors = ['#E53E3E', '#38A169', '#3182CE']
    brain_y = [0.75, 0.5, 0.25]
    
    for i, (level, color, y) in enumerate(zip(brain_levels, brain_colors, brain_y)):
        # Draw brain circles
        circle_size = 0.12 + i * 0.02  # Growing brain size
        circle = Circle((0.2, y), circle_size, facecolor=color, alpha=0.3, edgecolor=color, linewidth=3)
        evolution_ax.add_patch(circle)
        
        # Add text
        evolution_ax.text(0.55, y, level, ha='left', va='center', 
                         fontsize=14, fontweight='bold', color=color,
                         transform=evolution_ax.transAxes)
        
        # Add complexity indicators
        complexity_dots = '●' * (i + 1)
        evolution_ax.text(0.85, y, complexity_dots, ha='center', va='center', 
                         fontsize=16, color=color, transform=evolution_ax.transAxes)
    
    evolution_ax.set_xlim(0, 1)
    evolution_ax.set_ylim(0, 1)
    evolution_ax.axis('off')
    
    # ============= STATISTICS PANEL =============
    stats_ax = fig.add_subplot(gs[:, 3])
    
    # Create statistics box
    stats_box = FancyBboxPatch((0.05, 0.05), 0.9, 0.9, 
                              boxstyle="round,pad=0.04", 
                              facecolor='#F7FAFC', edgecolor='#2D3748', linewidth=3)
    stats_ax.add_patch(stats_box)
    
    # Statistics title
    stats_ax.text(0.5, 0.95, 'Distribution', 
                 ha='center', va='top', fontsize=16, fontweight='bold',
                 color='#2D3748', transform=stats_ax.transAxes)
    
    # Calculate actual statistics
    tom_dist = cognitive_df['ToM_Level'].value_counts(normalize=True) * 100
    
    # Create mini bar chart
    levels = [0, 1, 2]
    percentages = [tom_dist.get(i, 0) for i in levels]
    colors = ['#E53E3E', '#38A169', '#3182CE']
    
    y_pos = [0.75, 0.6, 0.45]
    for level, pct, color, y in zip(levels, percentages, colors, y_pos):
        # Bar
        bar_width = pct / 100 * 0.7
        bar = Rectangle((0.15, y-0.03), bar_width, 0.06, 
                       facecolor=color, alpha=0.7, edgecolor=color)
        stats_ax.add_patch(bar)
        
        # Label
        stats_ax.text(0.1, y, f'L{level}:', fontsize=12, fontweight='bold', 
                     color=color, ha='right', va='center', transform=stats_ax.transAxes)
        stats_ax.text(0.9, y, f'{pct:.1f}%', fontsize=12, fontweight='bold', 
                     color=color, ha='right', va='center', transform=stats_ax.transAxes)
    
    # Key insight
    stats_ax.text(0.5, 0.3, 'BREAKTHROUGH', ha='center', fontsize=14, fontweight='bold',
                 color='#2D3748', transform=stats_ax.transAxes)
    
    stats_ax.text(0.5, 0.2, 'Clear evidence of\nsophisticated ToM\nin LLM reasoning', 
                 ha='center', va='center', fontsize=11, fontweight='bold',
                 color='#3182CE', transform=stats_ax.transAxes,
                 bbox=dict(boxstyle="round,pad=0.3", facecolor='#EBF8FF'))
    
    # Model highlight
    stats_ax.text(0.5, 0.08, 'Hush-Qwen: 11.1% Level 2\n93.3% accuracy', 
                 ha='center', va='center', fontsize=10, fontweight='bold',
                 color='#2C5282', transform=stats_ax.transAxes,
                 bbox=dict(boxstyle="round,pad=0.2", facecolor='#BEE3F8'))
    
    stats_ax.set_xlim(0, 1)
    stats_ax.set_ylim(0, 1)
    stats_ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('slide10_tom_evidence_premium.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.show()

def main():
    """Generate premium slide 10"""
    print("🎨 Creating premium Theory of Mind evidence slide...")
    create_premium_slide10()
    print("✅ Premium slide 10 created: slide10_tom_evidence_premium.png")

if __name__ == "__main__":
    main() 