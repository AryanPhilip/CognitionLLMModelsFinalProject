#!/usr/bin/env python3
"""
Cognitive Theory of Mind Analysis: Examining Reasoning Patterns in LLM Explanations
==================================================================================
This script analyzes LLM explanations through various cognitive science frameworks.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from collections import Counter, defaultdict
import warnings
warnings.filterwarnings('ignore')

# Set up plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 12

class CognitiveToMAnalyzer:
    """Analyzes Theory of Mind reasoning patterns in LLM explanations from a cognitive science perspective."""
    
    def __init__(self, data_file):
        """Initialize with the results CSV file."""
        self.df = pd.read_csv(data_file)
        self.prepare_data()
        self.analyze_cognitive_patterns()
        
    def prepare_data(self):
        """Clean and prepare data for cognitive analysis."""
        # Create model short names
        self.df['Model_Short'] = self.df['LLM_Model'].str.split('/').str[-1].str.replace('-Preview', '').str[:25]
        
        # Filter out rows with missing explanations
        self.df = self.df.dropna(subset=['Explanation_Text'])
        
        print(f"🧠 Cognitive Analysis initialized: {len(self.df)} explanations from {self.df['Model_Short'].nunique()} models")
        
    def analyze_cognitive_patterns(self):
        """Main cognitive pattern analysis pipeline."""
        print("🔍 Analyzing cognitive patterns...")
        
        # Initialize analysis results
        self.cognitive_metrics = []
        
        for idx, row in self.df.iterrows():
            explanation = row['Explanation_Text']
            model = row['Model_Short']
            context_type = row['Context_Type']
            is_correct = row['Is_Classification_Correct']
            
            # Analyze this explanation
            metrics = self.analyze_single_explanation(explanation, model, context_type, is_correct)
            self.cognitive_metrics.append(metrics)
        
        # Convert to DataFrame for analysis
        self.cognitive_df = pd.DataFrame(self.cognitive_metrics)
        print(f"✅ Cognitive analysis complete: {len(self.cognitive_df)} explanations analyzed")
        
    def analyze_single_explanation(self, explanation, model, context_type, is_correct):
        """Analyze a single explanation for cognitive patterns."""
        
        # Convert to lowercase for analysis
        text = explanation.lower()
        
        # 1. THEORY OF MIND LEVELS
        tom_level = self.detect_tom_level(text)
        
        # 2. MENTAL STATE ATTRIBUTION
        mental_states = self.detect_mental_state_attribution(text)
        
        # 3. CAUSAL REASONING PATTERNS
        causal_patterns = self.detect_causal_reasoning(text)
        
        # 4. CONTEXTUAL INTEGRATION
        context_integration = self.detect_context_integration(text)
        
        # 5. STRATEGIC REASONING
        strategic_reasoning = self.detect_strategic_reasoning(text)
        
        # 6. TEMPORAL REASONING
        temporal_reasoning = self.detect_temporal_reasoning(text)
        
        # 7. UNCERTAINTY AND CONFIDENCE
        uncertainty_markers = self.detect_uncertainty_markers(text)
        
        # 8. OPPONENT MODELING
        opponent_modeling = self.detect_opponent_modeling(text)
        
        # 9. GAME THEORY CONCEPTS
        game_theory = self.detect_game_theory_concepts(text)
        
        # 10. REASONING SOPHISTICATION
        sophistication = self.calculate_reasoning_sophistication(text)
        
        return {
            'Model': model,
            'Context_Type': context_type,
            'Is_Correct': is_correct,
            'Explanation_Length': len(explanation),
            
            # Theory of Mind
            'ToM_Level': tom_level,
            'Mental_State_Words': mental_states['count'],
            'Mental_State_Types': len(mental_states['types']),
            'Belief_Attribution': mental_states['belief_attribution'],
            'Intention_Attribution': mental_states['intention_attribution'],
            
            # Reasoning Patterns
            'Causal_Connectives': causal_patterns['connectives'],
            'Causal_Chains': causal_patterns['chains'],
            'Context_Integration_Score': context_integration,
            'Strategic_Reasoning_Score': strategic_reasoning,
            'Temporal_Reasoning': temporal_reasoning,
            
            # Uncertainty and Confidence
            'Uncertainty_Markers': uncertainty_markers['count'],
            'Confidence_Level': uncertainty_markers['confidence'],
            'Hedge_Words': uncertainty_markers['hedges'],
            
            # Opponent Modeling
            'Opponent_References': opponent_modeling['references'],
            'Opponent_Psychology': opponent_modeling['psychology'],
            'Opponent_Tendencies': opponent_modeling['tendencies'],
            'Opponent_History': opponent_modeling['history'],
            
            # Game Theory
            'Game_Theory_Terms': game_theory['terms'],
            'Strategic_Concepts': game_theory['concepts'],
            'EV_Reasoning': game_theory['ev_reasoning'],
            
            # Overall Sophistication
            'Reasoning_Sophistication': sophistication,
            'Explanation_Text': explanation
        }
    
    def detect_tom_level(self, text):
        """Detect Theory of Mind reasoning level (0, 1, or 2)."""
        
        # Level 0: No mental state attribution
        # Level 1: First-order ToM (opponent thinks/believes/wants X)
        # Level 2: Second-order ToM (opponent thinks I think Y)
        
        # First-order ToM patterns
        first_order_patterns = [
            r'opponent.*(?:thinks|believes|wants|knows|assumes|expects|hopes)',
            r'(?:they|he).*(?:think|believe|want|know|assume|expect|hope)',
            r'opponent.*(?:is trying|is attempting|is looking)',
            r'(?:they|he).*(?:trying|attempting|looking)',
            r'opponent.*(?:has|holds|represents)',
        ]
        
        # Second-order ToM patterns
        second_order_patterns = [
            r'opponent.*thinks.*(?:i|you|hero).*(?:think|believe|have)',
            r'(?:they|he).*(?:think|believe).*(?:i|you|hero).*(?:think|believe|have)',
            r'exploit.*(?:your|hero).*(?:range|hand|position)',
            r'induce.*(?:folds|calls).*from.*(?:you|hero)',
            r'make.*(?:you|hero).*(?:think|believe|fold)',
        ]
        
        # Check for patterns
        first_order_found = any(re.search(pattern, text) for pattern in first_order_patterns)
        second_order_found = any(re.search(pattern, text) for pattern in second_order_patterns)
        
        if second_order_found:
            return 2  # Second-order ToM
        elif first_order_found:
            return 1  # First-order ToM  
        else:
            return 0  # No clear ToM
    
    def detect_mental_state_attribution(self, text):
        """Detect mental state attribution patterns."""
        
        # Mental state verbs
        belief_verbs = ['thinks', 'believes', 'assumes', 'expects', 'supposes', 'imagines']
        intention_verbs = ['wants', 'intends', 'tries', 'attempts', 'aims', 'seeks', 'hopes']
        knowledge_verbs = ['knows', 'realizes', 'understands', 'recognizes']
        
        all_mental_verbs = belief_verbs + intention_verbs + knowledge_verbs
        
        # Count mental state words
        mental_state_count = sum(text.count(verb) for verb in all_mental_verbs)
        
        # Identify types of mental states
        types_found = set()
        if any(verb in text for verb in belief_verbs):
            types_found.add('belief')
        if any(verb in text for verb in intention_verbs):
            types_found.add('intention')
        if any(verb in text for verb in knowledge_verbs):
            types_found.add('knowledge')
        
        # Specific attribution patterns
        belief_attribution = bool(re.search(r'opponent.*(?:thinks|believes|assumes)', text))
        intention_attribution = bool(re.search(r'opponent.*(?:wants|intends|trying|attempting)', text))
        
        return {
            'count': mental_state_count,
            'types': types_found,
            'belief_attribution': belief_attribution,
            'intention_attribution': intention_attribution
        }
    
    def detect_causal_reasoning(self, text):
        """Detect causal reasoning patterns."""
        
        # Causal connectives
        causal_words = ['because', 'since', 'given', 'due to', 'as a result', 'therefore', 
                       'thus', 'hence', 'consequently', 'leads to', 'causes', 'results in']
        
        connective_count = sum(text.count(word) for word in causal_words)
        
        # Causal chain detection (multiple causal links)
        causal_chain_patterns = [
            r'given.*(?:and|,).*(?:this|it).*(?:suggests|indicates|means)',
            r'because.*(?:and|,).*(?:therefore|thus|so)',
            r'since.*(?:and|,).*(?:making|suggesting|indicating)'
        ]
        
        chains = sum(1 for pattern in causal_chain_patterns if re.search(pattern, text))
        
        return {
            'connectives': connective_count,
            'chains': chains
        }
    
    def detect_context_integration(self, text):
        """Detect how well the explanation integrates multiple contextual cues."""
        
        # Context categories
        context_cues = {
            'opponent_history': ['history', 'previous', 'past', 'shown', 'demonstrated', 'pattern'],
            'board_texture': ['board', 'texture', 'flush', 'straight', 'draw', 'cards'],
            'bet_sizing': ['bet size', 'pot size', 'sizing', 'small', 'large', 'overbet', '%'],
            'position': ['position', 'range', 'fold', 'call', 'exploit']
        }
        
        # Count integrated cues
        integrated_cues = 0
        for category, keywords in context_cues.items():
            if any(keyword in text for keyword in keywords):
                integrated_cues += 1
        
        # Bonus for explicit integration language
        integration_phrases = ['aligns with', 'consistent with', 'combined with', 'together with', 
                              'considering', 'given that', 'along with']
        integration_bonus = sum(1 for phrase in integration_phrases if phrase in text)
        
        return min(integrated_cues + integration_bonus, 5)  # Cap at 5
    
    def detect_strategic_reasoning(self, text):
        """Detect strategic reasoning sophistication."""
        
        strategic_concepts = [
            'exploit', 'induce', 'extract value', 'maximize', 'minimize', 'protect', 
            'represent', 'range', 'equity', 'fold equity', 'implied odds',
            'bluffing frequency', 'polarized', 'balanced', 'deceptive'
        ]
        
        strategy_score = sum(1 for concept in strategic_concepts if concept in text)
        
        # Advanced strategic reasoning
        advanced_patterns = [
            r'exploit.*range',
            r'induce.*folds',
            r'extract.*value',
            r'protect.*equity',
            r'represent.*(?:strength|hand)'
        ]
        
        advanced_bonus = sum(1 for pattern in advanced_patterns if re.search(pattern, text))
        
        return min(strategy_score + advanced_bonus, 5)  # Cap at 5
    
    def detect_temporal_reasoning(self, text):
        """Detect temporal reasoning about past, present, and future."""
        
        temporal_markers = {
            'past': ['previously', 'earlier', 'before', 'had', 'was', 'shown', 'demonstrated'],
            'present': ['now', 'currently', 'this', 'here', 'is', 'are'],
            'future': ['will', 'would', 'likely', 'probably', 'expect', 'predict']
        }
        
        temporal_score = 0
        for timeframe, markers in temporal_markers.items():
            if any(marker in text for marker in markers):
                temporal_score += 1
        
        return temporal_score
    
    def detect_uncertainty_markers(self, text):
        """Detect uncertainty and confidence markers."""
        
        # Uncertainty markers
        uncertainty_words = ['likely', 'probably', 'possibly', 'might', 'could', 'may', 
                            'seems', 'appears', 'suggests', 'indicates', 'reasonable']
        
        uncertainty_count = sum(text.count(word) for word in uncertainty_words)
        
        # Confidence markers
        confidence_words = ['clearly', 'obviously', 'definitely', 'certainly', 'undoubtedly',
                           'strongly', 'highly likely', 'very likely', 'almost certainly']
        
        confidence_count = sum(text.count(word) for word in confidence_words)
        
        # Hedge words
        hedge_words = ['somewhat', 'rather', 'quite', 'fairly', 'relatively', 'mostly', 'generally']
        hedge_count = sum(text.count(word) for word in hedge_words)
        
        # Calculate confidence level (more confidence words = higher confidence)
        confidence_level = min(confidence_count / max(uncertainty_count + 1, 1), 2.0)
        
        return {
            'count': uncertainty_count,
            'confidence': confidence_level,
            'hedges': hedge_count
        }
    
    def detect_opponent_modeling(self, text):
        """Detect sophistication of opponent modeling."""
        
        # Direct opponent references
        opponent_refs = text.count('opponent') + text.count('they') + text.count('he') + text.count('their')
        
        # Psychological attribution
        psychology_patterns = [
            r'opponent.*(?:enjoys|likes|dislikes|prefers|tends)',
            r'opponent.*(?:style|pattern|behavior|tendency)',
            r'(?:they|he).*(?:enjoy|like|dislike|prefer|tend)',
            r'(?:aggressive|tight|loose|conservative|wild|tricky)'
        ]
        
        psychology_score = sum(1 for pattern in psychology_patterns if re.search(pattern, text))
        
        # Tendency attribution
        tendency_patterns = [
            r'history of',
            r'pattern of',
            r'tendency to',
            r'known for',
            r'shown.*to',
            r'demonstrated'
        ]
        
        tendency_score = sum(1 for pattern in tendency_patterns if re.search(pattern, text))
        
        # Historical reference
        history_patterns = [
            r'previous.*(?:hand|action|bet|play)',
            r'earlier.*(?:showed|demonstrated)',
            r'past.*(?:behavior|actions)',
            r'shown down',
            r'has.*(?:been|shown)'
        ]
        
        history_score = sum(1 for pattern in history_patterns if re.search(pattern, text))
        
        return {
            'references': min(opponent_refs, 5),
            'psychology': min(psychology_score, 3),
            'tendencies': min(tendency_score, 3),
            'history': min(history_score, 3)
        }
    
    def detect_game_theory_concepts(self, text):
        """Detect game theory and poker theory concepts."""
        
        # Game theory terms
        game_theory_terms = [
            'equilibrium', 'nash', 'optimal', 'strategy', 'payoff', 'utility',
            'expectation', 'expected value', 'ev', 'gto', 'exploitative'
        ]
        
        theory_count = sum(1 for term in game_theory_terms if term in text)
        
        # Strategic concepts
        strategic_concepts = [
            'range', 'polarized', 'merged', 'balanced', 'frequency',
            'fold equity', 'implied odds', 'reverse implied odds',
            'blockers', 'combinatorics', 'outs'
        ]
        
        concept_count = sum(1 for concept in strategic_concepts if concept in text)
        
        # Expected value reasoning
        ev_patterns = [
            r'extract.*value',
            r'maximize.*value',
            r'positive.*expectation',
            r'profitable',
            r'expected.*return'
        ]
        
        ev_reasoning = sum(1 for pattern in ev_patterns if re.search(pattern, text))
        
        return {
            'terms': theory_count,
            'concepts': concept_count,
            'ev_reasoning': ev_reasoning
        }
    
    def calculate_reasoning_sophistication(self, text):
        """Calculate overall reasoning sophistication score."""
        
        # Components of sophisticated reasoning
        components = {
            'length': min(len(text) / 200, 2),  # Longer explanations (up to 2 points)
            'vocabulary': len(set(text.split())) / len(text.split()) if text.split() else 0,  # Vocabulary diversity
            'specificity': text.count('$') + text.count('%') + text.count('♠') + text.count('♥') + text.count('♦') + text.count('♣'),  # Specific references
            'logical_structure': text.count('.') + text.count(','),  # Sentence complexity
        }
        
        # Normalize and combine
        sophistication = (
            components['length'] +
            components['vocabulary'] * 2 +
            min(components['specificity'] / 3, 1) +
            min(components['logical_structure'] / 10, 1)
        )
        
        return min(sophistication, 5)  # Cap at 5
    
    def create_cognitive_dashboard(self):
        """Create comprehensive cognitive analysis dashboard."""
        
        fig, axes = plt.subplots(3, 3, figsize=(20, 18))
        fig.suptitle('🧠 Cognitive Theory of Mind Analysis Dashboard', fontsize=20, fontweight='bold', y=0.98)
        
        # 1. Theory of Mind Levels by Model
        tom_by_model = self.cognitive_df.groupby(['Model', 'ToM_Level']).size().unstack(fill_value=0)
        tom_by_model_pct = tom_by_model.div(tom_by_model.sum(axis=1), axis=0) * 100
        
        tom_by_model_pct.plot(kind='bar', stacked=True, ax=axes[0,0], 
                             color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        axes[0,0].set_title('Theory of Mind Levels by Model', fontweight='bold')
        axes[0,0].set_ylabel('Percentage of Explanations')
        axes[0,0].legend(['Level 0 (None)', 'Level 1 (First-order)', 'Level 2 (Second-order)'])
        axes[0,0].tick_params(axis='x', rotation=45)
        
        # 2. Mental State Attribution
        mental_state_cols = ['Mental_State_Words', 'Belief_Attribution', 'Intention_Attribution']
        mental_state_data = self.cognitive_df.groupby('Model')[mental_state_cols].mean()
        
        mental_state_data.plot(kind='bar', ax=axes[0,1])
        axes[0,1].set_title('Mental State Attribution by Model', fontweight='bold')
        axes[0,1].set_ylabel('Average Score')
        axes[0,1].legend(['Mental State Words', 'Belief Attribution', 'Intention Attribution'])
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # 3. Context Integration vs Performance
        context_acc = self.cognitive_df.groupby(['Model', 'Context_Integration_Score'])['Is_Correct'].mean().unstack()
        
        sns.heatmap(context_acc, annot=True, fmt='.2f', cmap='RdYlGn', ax=axes[0,2],
                   cbar_kws={'label': 'Accuracy'})
        axes[0,2].set_title('Context Integration vs Accuracy', fontweight='bold')
        axes[0,2].set_xlabel('Context Integration Score')
        axes[0,2].set_ylabel('Model')
        
        # 4. Opponent Modeling Sophistication
        opponent_cols = ['Opponent_References', 'Opponent_Psychology', 'Opponent_Tendencies', 'Opponent_History']
        opponent_data = self.cognitive_df.groupby('Model')[opponent_cols].mean()
        
        opponent_data.plot(kind='bar', ax=axes[1,0])
        axes[1,0].set_title('Opponent Modeling by Model', fontweight='bold')
        axes[1,0].set_ylabel('Average Score')
        axes[1,0].legend(['References', 'Psychology', 'Tendencies', 'History'], bbox_to_anchor=(1.05, 1))
        axes[1,0].tick_params(axis='x', rotation=45)
        
        # 5. Reasoning Sophistication Distribution
        sns.boxplot(data=self.cognitive_df, x='Model', y='Reasoning_Sophistication', ax=axes[1,1])
        axes[1,1].set_title('Reasoning Sophistication Distribution', fontweight='bold')
        axes[1,1].set_ylabel('Sophistication Score')
        axes[1,1].tick_params(axis='x', rotation=45)
        
        # 6. Bluff vs Value Reasoning Differences
        bluff_value_comparison = self.cognitive_df.groupby(['Model', 'Context_Type']).agg({
            'ToM_Level': 'mean',
            'Strategic_Reasoning_Score': 'mean',
            'Uncertainty_Markers': 'mean'
        }).round(2)
        
        # Plot ToM level differences
        tom_comparison = bluff_value_comparison['ToM_Level'].unstack()
        
        x = np.arange(len(tom_comparison.index))
        width = 0.35
        
        axes[1,2].bar(x - width/2, tom_comparison['Bluff'], width, label='Bluff', alpha=0.8, color='#FF6B6B')
        axes[1,2].bar(x + width/2, tom_comparison['Value'], width, label='Value', alpha=0.8, color='#4ECDC4')
        axes[1,2].set_title('ToM Level: Bluff vs Value Detection', fontweight='bold')
        axes[1,2].set_ylabel('Average ToM Level')
        axes[1,2].set_xticks(x)
        axes[1,2].set_xticklabels(tom_comparison.index, rotation=45)
        axes[1,2].legend()
        
        # 7. Uncertainty vs Confidence by Context
        uncertainty_by_context = self.cognitive_df.groupby(['Model', 'Context_Type']).agg({
            'Uncertainty_Markers': 'mean',
            'Confidence_Level': 'mean'
        })
        
        uncertainty_data = uncertainty_by_context['Uncertainty_Markers'].unstack()
        uncertainty_data.plot(kind='bar', ax=axes[2,0], color=['#FF6B6B', '#4ECDC4'])
        axes[2,0].set_title('Uncertainty Markers by Context', fontweight='bold')
        axes[2,0].set_ylabel('Average Uncertainty Markers')
        axes[2,0].legend(['Bluff', 'Value'])
        axes[2,0].tick_params(axis='x', rotation=45)
        
        # 8. Causal Reasoning Patterns
        causal_data = self.cognitive_df.groupby('Model').agg({
            'Causal_Connectives': 'mean',
            'Causal_Chains': 'mean'
        })
        
        causal_data.plot(kind='bar', ax=axes[2,1])
        axes[2,1].set_title('Causal Reasoning by Model', fontweight='bold')
        axes[2,1].set_ylabel('Average Score')
        axes[2,1].legend(['Causal Connectives', 'Causal Chains'])
        axes[2,1].tick_params(axis='x', rotation=45)
        
        # 9. Overall Cognitive Complexity
        cognitive_complexity = self.cognitive_df.groupby('Model').agg({
            'ToM_Level': 'mean',
            'Context_Integration_Score': 'mean',
            'Strategic_Reasoning_Score': 'mean',
            'Reasoning_Sophistication': 'mean'
        })
        
        # Create radar chart - remove the axes assignment and create new polar subplot
        axes[2,2].remove()  # Remove the regular axes
        ax_polar = fig.add_subplot(3, 3, 9, projection='polar')
        
        angles = np.linspace(0, 2*np.pi, len(cognitive_complexity.columns), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))
        
        ax_polar.set_theta_offset(np.pi / 2)
        ax_polar.set_theta_direction(-1)
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        for i, (model, scores) in enumerate(cognitive_complexity.iterrows()):
            values = scores.values.tolist()
            values += [values[0]]  # Complete the circle
            ax_polar.plot(angles, values, 'o-', linewidth=2, label=model[:15], color=colors[i % len(colors)])
            ax_polar.fill(angles, values, alpha=0.25, color=colors[i % len(colors)])
        
        ax_polar.set_xticks(angles[:-1])
        ax_polar.set_xticklabels(['ToM Level', 'Context Integration', 'Strategic Reasoning', 'Sophistication'])
        ax_polar.set_title('Cognitive Complexity Profile', fontweight='bold', pad=20)
        ax_polar.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
        
        plt.tight_layout()
        plt.savefig('cognitive_tom_dashboard.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def generate_cognitive_insights(self):
        """Generate insights from cognitive analysis."""
        
        print("\n" + "="*80)
        print("🧠 COGNITIVE THEORY OF MIND INSIGHTS")
        print("="*80)
        
        # Overall ToM levels
        tom_distribution = self.cognitive_df['ToM_Level'].value_counts(normalize=True) * 100
        print(f"\n🎯 THEORY OF MIND LEVELS:")
        print(f"Level 0 (None): {tom_distribution.get(0, 0):.1f}%")
        print(f"Level 1 (First-order): {tom_distribution.get(1, 0):.1f}%")
        print(f"Level 2 (Second-order): {tom_distribution.get(2, 0):.1f}%")
        
        # Model comparison
        model_tom = self.cognitive_df.groupby('Model')['ToM_Level'].mean().sort_values(ascending=False)
        print(f"\n🤖 MODEL COGNITIVE RANKINGS:")
        for model, tom_score in model_tom.items():
            print(f"{model[:25]}: {tom_score:.2f} average ToM level")
        
        # Bluff vs Value cognitive differences
        context_comparison = self.cognitive_df.groupby('Context_Type').agg({
            'ToM_Level': 'mean',
            'Strategic_Reasoning_Score': 'mean',
            'Uncertainty_Markers': 'mean',
            'Opponent_Psychology': 'mean'
        }).round(3)
        
        print(f"\n🎭 COGNITIVE DIFFERENCES: BLUFF vs VALUE")
        print(context_comparison)
        
        # Correlation with accuracy
        cognitive_cols = ['ToM_Level', 'Context_Integration_Score', 'Strategic_Reasoning_Score', 
                         'Opponent_Psychology', 'Reasoning_Sophistication']
        correlations = self.cognitive_df[cognitive_cols + ['Is_Correct']].corr()['Is_Correct'].sort_values(ascending=False)[:-1]
        
        print(f"\n📊 COGNITIVE FACTORS CORRELATED WITH ACCURACY:")
        for factor, correlation in correlations.items():
            print(f"{factor}: {correlation:.3f}")
        
        # Best explanations analysis
        best_explanations = self.cognitive_df[
            (self.cognitive_df['Is_Correct'] == 1) & 
            (self.cognitive_df['ToM_Level'] == 2)
        ].sort_values('Reasoning_Sophistication', ascending=False).head(3)
        
        print(f"\n🏆 TOP THEORY OF MIND EXPLANATIONS:")
        for idx, explanation in best_explanations.iterrows():
            print(f"\nModel: {explanation['Model']}")
            print(f"Context: {explanation['Context_Type']}")
            print(f"ToM Level: {explanation['ToM_Level']}")
            print(f"Sophistication: {explanation['Reasoning_Sophistication']:.2f}")
            print(f"Text: {explanation['Explanation_Text'][:200]}...")
            print("-" * 60)
        
        return {
            'tom_distribution': tom_distribution,
            'model_rankings': model_tom,
            'context_differences': context_comparison,
            'accuracy_correlations': correlations
        }
        
    def export_cognitive_analysis(self):
        """Export detailed cognitive analysis results."""
        
        # Summary statistics by model
        model_summary = self.cognitive_df.groupby('Model').agg({
            'ToM_Level': ['mean', 'std'],
            'Mental_State_Words': 'mean',
            'Context_Integration_Score': 'mean',
            'Strategic_Reasoning_Score': 'mean',
            'Opponent_Psychology': 'mean',
            'Reasoning_Sophistication': 'mean',
            'Is_Correct': 'mean'
        }).round(3)
        
        model_summary.to_csv('cognitive_analysis_summary.csv')
        
        # Detailed explanation analysis
        self.cognitive_df.to_csv('detailed_cognitive_analysis.csv', index=False)
        
        print("📁 Cognitive analysis exported:")
        print("  - cognitive_analysis_summary.csv")
        print("  - detailed_cognitive_analysis.csv")


def main():
    """Main cognitive analysis pipeline."""
    print("🧠 Starting Cognitive Theory of Mind Analysis...")
    
    # Initialize analyzer
    analyzer = CognitiveToMAnalyzer('poker_tom_results_20250602_081719.csv')
    
    # Create visualizations
    print("\n📊 Creating cognitive dashboard...")
    analyzer.create_cognitive_dashboard()
    
    # Generate insights
    print("\n💡 Generating cognitive insights...")
    insights = analyzer.generate_cognitive_insights()
    
    # Export results
    print("\n📁 Exporting analysis...")
    analyzer.export_cognitive_analysis()
    
    print("\n✅ Cognitive analysis complete!")
    print("\nFiles generated:")
    print("- cognitive_tom_dashboard.png")
    print("- cognitive_analysis_summary.csv")
    print("- detailed_cognitive_analysis.csv")


if __name__ == "__main__":
    main() 