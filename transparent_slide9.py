#!/usr/bin/env python3
"""
Generate Slide 9 Implications with Transparent Background
=========================================================
"""

import matplotlib.pyplot as plt
import numpy as np

def create_slide_9_implications_transparent():
    """Slide 9: Implications - Key takeaways with transparent background"""
    
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
    
    # Save with transparent background
    plt.savefig('slide9_implications.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.show()
    print("✅ Slide 9 implications created with transparent background")

if __name__ == "__main__":
    create_slide_9_implications_transparent() 