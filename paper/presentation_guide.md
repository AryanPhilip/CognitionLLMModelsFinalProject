# Theory of Mind in Large Language Models: Poker Analysis Presentation Guide

## **🎯 15-Minute Technical Presentation Structure**

### **Slide 1: Title & Hook (1 min)** 
```
🧠 Theory of Mind in Large Language Models: 
Evidence from Poker Deception Detection

Can AI understand that humans bluff, lie, and deceive?

[Your Name] | Cognition & LM Class | [Date]
```

**Speaking notes:**
- Start with hook: "How many of you have been lied to today?"
- Introduce concept: "Theory of Mind = understanding others have different beliefs"
- Preview: "Today we test if LLMs can detect deception in poker"

---

### **Slide 2: The Theory of Mind Challenge (1 min)**
```
🤔 What is Theory of Mind?

• The ability to understand others have mental states different from your own
• Critical for deception detection, strategic reasoning, social interaction
• Milestone in human cognitive development (age 3-5)

🤖 Challenge for AI:
Can LLMs model opponent psychology and detect intentional deception?
```

**Speaking notes:**
- ToM = cornerstone of human social cognition
- Essential for understanding lies, bluffs, strategic behavior
- Open question whether LLMs possess this capability

---

### **Slide 3: Poker as a ToM Laboratory (1.5 min)**
```
🃏 Why Poker? The Perfect ToM Testing Ground

Basic Setup:
• Players have hidden cards (private information)
• Must decide: bet/call/fold based on incomplete information
• Success requires modeling opponent's mental state

Key Concepts:
🎭 BLUFF = Betting with a weak hand to make opponents fold
💎 VALUE BET = Betting with a strong hand to get called

🧠 This requires Theory of Mind reasoning about opponent intentions!
```

**Speaking notes:**
- Poker = natural ToM environment
- Players must constantly model "what does opponent think I have?"
- Bluffing = intentional deception requiring understanding of opponent's mind

---

### **Slide 4: Poker Example - Bluff Scenario (1.5 min)**
```
🎭 BLUFF SCENARIO EXAMPLE

Your Cards: A♠ Q♥
Board: K♥ T♥ 4♦ 2♠ 2♣
Pot: $1000, Opponent bets $150

Opponent Context:
"Known for triple-barreling missed draws. Recently showed down 
8♦6♦ after betting all three streets on a heart-heavy board."

Question: Is this bet a BLUFF or VALUE?

ToM Reasoning Required:
→ Opponent knows their hand is weak
→ Opponent believes YOU might fold 
→ Opponent acts to exploit YOUR mental state
```

**Speaking notes:**
- Walk through scenario step by step
- Emphasize the psychological reasoning required
- "This requires thinking about what opponent thinks YOU think"

---

### **Slide 5: Research Questions & Design (1 min)**
```
🔬 Research Questions

RQ1: Can LLMs accurately classify bets as "bluff" vs "value" 
     using contextual cues about opponent tendencies?

RQ2: Do LLM explanations show evidence of Theory of Mind reasoning?

🧪 Experimental Design:
• 4 State-of-the-art LLMs tested
• 15 poker scenarios × 2 contexts (bluff/value) = 30 stimuli  
• 3 runs per model = 360 total responses
• Temperature = 0.3 for consistency
```

**Speaking notes:**
- Clear hypotheses about ToM capabilities
- Rigorous experimental design
- Multiple models for generalizability

---

### **Slide 6: Key Results - Performance Hierarchy (2 min)**
*Use: `presentation_accuracy.png`*

```
📊 MAIN FINDING: Clear Performance Hierarchy

Best Model: Hush-Qwen2.5-7B (93.3% accuracy)
Worst Model: Llama-1B (12.2% accuracy)
Range: 81.1 percentage points difference

Statistical Significance:
✓ Hush-Qwen2.5-7B: p < 0.001
✗ EXAONE & OLMoE: Not significant vs. chance
```

**Speaking notes:**
- Dramatic performance differences between models
- Some models clearly above chance, others fail completely
- Size/architecture matters for ToM reasoning

---

### **Slide 7: The Bluff Detection Challenge (2 min)**
*Use: `presentation_bluff_challenge.png`*

```
🎭 CRITICAL FINDING: Bluff Detection = ToM Bottleneck

Value Detection: 63.3% average accuracy
Bluff Detection: 40.6% average accuracy  
Gap: 22.8 percentage points

Why Bluffs Are Harder:
• Requires modeling deceptive intent
• Counter-intuitive opponent behavior
• Second-order reasoning: "opponent thinks I think..."
```

**Speaking notes:**
- This is the money shot - clear evidence of ToM hierarchy
- Value bets = straightforward (opponent has good hand, bets)  
- Bluffs = complex psychology (opponent has bad hand, but bets anyway)
- Shows LLMs struggle with deception detection

---

### **Slide 8: Evidence of ToM Reasoning (1.5 min)**
```
🧠 QUALITATIVE EVIDENCE: ToM-Like Reasoning

High-Quality Bluff Detection Example:
"Given the opponent's history of triple-barreling missed draws... 
it is highly likely that this bet is a bluff. The opponent enjoys 
bluffing on such boards where few hands can make a strong draw..."

ToM Elements Present:
✓ References opponent tendencies
✓ Considers opponent's strategic motivation  
✓ Integrates board texture with psychology
✓ Shows understanding of deceptive intent
```

**Speaking notes:**
- Not just binary classification - explanations show reasoning
- LLMs explicitly reference opponent psychology
- Evidence of understanding strategic deception

---

### **Slide 9: Cognitive Implications (1.5 min)**
```
🔬 IMPLICATIONS FOR AI COGNITION

1. Scale Effects: Larger models → Better ToM reasoning
   (93% vs 12% accuracy between largest and smallest)

2. Task Hierarchy: Deception detection harder than sincere behavior
   (40% vs 63% accuracy)

3. Emergent Capability: ToM reasoning not explicitly trained
   (Models show sophisticated opponent modeling)

4. Context Integration: Success requires combining multiple cues
   (Opponent history + board texture + bet sizing)
```

**Speaking notes:**
- These findings have broader implications for AI
- Scale unlocks sophisticated reasoning capabilities
- Hierarchy suggests genuine cognitive complexity
- Emergence = not just pattern matching

---

### **Slide 10: Research Contributions (1 min)**
```
🏆 NOVEL CONTRIBUTIONS

1. New Benchmark: Poker bluff detection as ToM assessment
   • Ecologically valid social reasoning task
   • Quantifiable with clear ground truth
   • Scalable across different AI systems

2. Empirical Evidence: LLMs demonstrate measurable ToM
   • Clear performance hierarchy
   • Sophisticated reasoning in explanations
   • Context-dependent strategic understanding

3. Cognitive Framework: Hierarchy of social reasoning complexity
   • Sincere behavior detection (easier)
   • Deceptive intent detection (harder)
   • Foundation for future ToM research
```

**Speaking notes:**
- This work opens new research directions
- Practical applications for AI safety and alignment
- Framework for understanding AI social cognition

---

### **Slide 11: Limitations & Future Work (1 min)**
```
⚠️ LIMITATIONS

• Small model sample (4 LLMs)
• Simulated scenarios (not real poker games)  
• No human baseline comparison
• Manual coding of ToM indicators needed

🔮 FUTURE DIRECTIONS

• Test on larger model suite (GPT-4, Claude, Gemini)
• Real-time poker game integration
• Cross-cultural deception detection
• Applications to AI safety and alignment
```

**Speaking notes:**
- Honest about current limitations
- Clear path forward for research expansion
- Broader applications beyond poker

---

### **Slide 12: Conclusions (1 min)**
```
🎯 KEY TAKEAWAYS

1. Large Language Models CAN demonstrate Theory of Mind reasoning
   ✓ Best model: 93% accuracy at deception detection

2. Bluff detection reveals cognitive hierarchy in AI systems
   ✓ Deception harder than sincere behavior (23% gap)

3. Poker provides novel benchmark for AI social cognition
   ✓ Quantifiable, scalable, ecologically valid

Bottom Line: AI is developing sophisticated understanding 
of human psychology and deception - with important implications 
for safety, alignment, and social interaction.
```

**Speaking notes:**
- Summarize three main contributions
- End with broader implications
- Connect back to opening question about deception

---

## **🎨 Presentation Tips:**

### **Visual Design:**
- Use the generated PNG files for maximum impact
- Dark background with bright, contrasting text
- Large fonts (minimum 24pt)
- Consistent color scheme throughout

### **Delivery Strategy:**
- **Start strong** with deception hook
- **Use poker examples** early to build intuition  
- **Show data visualizations** prominently (slides 6-7)
- **Connect to broader AI implications** throughout
- **End with future vision** for AI cognition research

### **Time Management:**
- **Setup (3 slides): 3.5 minutes** - Build foundation
- **Methods (2 slides): 2 minutes** - Quick but thorough  
- **Results (4 slides): 6.5 minutes** - Main content focus
- **Implications (3 slides): 3 minutes** - Broader significance

### **Q&A Preparation:**
- **"How does this compare to human performance?"** → Great future work opportunity
- **"Could this be just pattern matching?"** → Point to explanation quality and context integration
- **"What about other ToM tasks?"** → Poker is one domain, broader applications possible
- **"Are there safety implications?"** → Yes, understanding AI deception detection is crucial

---

## **🎯 Key Messages to Emphasize:**

1. **Novel Benchmark**: Poker as ToM laboratory
2. **Clear Evidence**: 93% vs 12% performance range  
3. **Cognitive Hierarchy**: Bluff detection harder than value detection
4. **Emergent Capability**: Not explicitly trained, yet sophisticated
5. **Broader Implications**: AI safety, alignment, social interaction

This structure gives you a compelling 15-minute presentation that builds from poker basics to sophisticated AI cognition insights! 