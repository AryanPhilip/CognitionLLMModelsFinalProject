# Theory of Mind Poker Presentation - Complete File Summary

## 🎯 **Your Complete Presentation Package**

You now have a comprehensive set of analysis files and visualizations for your 15-minute Technical Presentation on Theory of Mind in Large Language Models.

---

## 📊 **Core Visualizations (Ready for Slides)**

### **1. `presentation_accuracy.png`** 
- **Use in:** Slide 6 (Main Results)
- **Shows:** Clear performance hierarchy across 4 LLMs
- **Key insight:** 93.3% (Hush-Qwen) vs 12.2% (Llama-1B) - dramatic range
- **Perfect for:** Demonstrating that some LLMs have genuine ToM capabilities

### **2. `presentation_bluff_challenge.png`**
- **Use in:** Slide 7 (Critical Finding) 
- **Shows:** Bluff vs Value detection comparison
- **Key insight:** 22.8% gap (63.3% value vs 40.6% bluff accuracy)
- **Perfect for:** Proving bluff detection is the ToM bottleneck

### **3. `tom_poker_dashboard.png`**
- **Use in:** Appendix or detailed discussion
- **Shows:** 6-panel comprehensive analysis dashboard
- **Contains:** Accuracy, heatmaps, significance, confusion matrices
- **Perfect for:** Deep-dive questions during Q&A

### **4. `confusion_matrices.png`**
- **Use in:** Appendix or methods section
- **Shows:** Model-specific prediction patterns
- **Perfect for:** Understanding where each model fails

### **5. `tom_indicators.png`**
- **Use in:** Slide 8 (ToM Evidence) or appendix
- **Shows:** Theory of Mind cognitive indicators by model
- **Perfect for:** Demonstrating sophisticated reasoning patterns

---

## 📈 **Statistical Analysis Files**

### **6. `model_performance_summary.csv`**
```
Model                     | Accuracy | Bluff_Acc | Value_Acc | Significant
Hush-Qwen2.5-7B          | 93.3%    | 88.9%     | 97.8%     | *** 
Llama-3.2-SUN-HDIC-1B    | 12.2%    | 13.3%     | 11.1%     | ***
OLMoE-1B-7B-0125         | 57.8%    | 35.6%     | 80.0%     | ns
EXAONE-3.5-2.4B          | 44.4%    | 24.4%     | 64.4%     | ns
```
- **Use for:** Exact statistics in slides
- **Key numbers:** Performance hierarchy, significance levels

### **7. `tom_poker_final_report.md`**
- **Contains:** Executive summary, key findings, implications
- **Use for:** Speaking notes, conclusions slide
- **Key stats:** 51.9% overall accuracy, 22.8% bluff-value gap

---

## 🧠 **Research Foundation Files**

### **8. `poker_tom_results_20250602_081719.csv`**
- **Raw data:** 360 LLM responses with classifications and explanations
- **Contains:** Stimulus IDs, model responses, accuracy scores
- **Use for:** Deep analysis, example explanations

### **9. `poker_stimuli_20250527_212428.csv`**
- **Original stimuli:** 30 poker scenarios (15 bluff + 15 value contexts)
- **Use for:** Understanding experimental design
- **Perfect for:** Showing example scenarios in slides

### **10. `presentation_guide.md`**
- **Complete slide-by-slide structure** for 15-minute presentation
- **Speaking notes** and timing for each section
- **Q&A preparation** with likely questions and answers
- **Delivery tips** for maximum impact

---

## 🎨 **Supporting Assets**

### **11. `poker_hands.png`**
- **Poker hand ranking chart**
- **Use for:** Context slide if audience unfamiliar with poker

### **12. `Levels-of-Thinking-in-Online-Poker-Infographics-scaled.jpg`**
- **Poker strategy levels infographic**
- **Use for:** Explaining psychological complexity of poker

---

## 🛠 **Technical Infrastructure Files**

### **13. `tom_poker_analysis.py`**
- **Complete analysis pipeline** 
- **Reproducible results** - run anytime for updated analysis
- **Customizable** for different datasets or models

### **14. Supporting files:**
- `requirements.txt` - Python dependencies
- `config.py` - Experimental parameters  
- `model_adapters.py` - LLM interface code
- `poker_tom_experiment.py` - Original experiment runner

---

## 🎯 **Presentation Recommendations**

### **Essential Files for Presentation:**
1. **`presentation_accuracy.png`** → Slide 6 (Main finding)
2. **`presentation_bluff_challenge.png`** → Slide 7 (Critical insight)  
3. **`model_performance_summary.csv`** → Statistics for slides
4. **`presentation_guide.md`** → Your complete script

### **Backup Files for Q&A:**
- `tom_poker_dashboard.png` - Comprehensive analysis
- `tom_poker_final_report.md` - Summary statistics
- `poker_stimuli_20250527_212428.csv` - Example scenarios

### **Optional Context Files:**
- `poker_hands.png` - If audience needs poker basics
- `confusion_matrices.png` - For technical deep-dive

---

## 📋 **Pre-Presentation Checklist**

✅ **Verify all visualizations display correctly**  
✅ **Practice with timer** (15 minutes including transitions)  
✅ **Prepare backup slides** from dashboard PNG  
✅ **Review statistical significance** levels and interpretations  
✅ **Rehearse poker example** explanation (Slide 4)  
✅ **Plan Q&A responses** using guide suggestions  

---

## 🚀 **Key Numbers to Memorize**

- **4 models tested**, **360 total responses**
- **93.3% best accuracy** (Hush-Qwen2.5-7B)
- **22.8% bluff-value gap** (the ToM bottleneck)
- **51.9% overall accuracy** across all models
- **p < 0.001** for significance vs. chance (best model)

---

## 💡 **Presentation Impact Strategy**

1. **Hook with deception question** (universal human experience)
2. **Build poker intuition** before diving into results  
3. **Show dramatic performance differences** (93% vs 12%)
4. **Emphasize bluff detection challenge** (core ToM finding)
5. **Connect to broader AI implications** (safety, alignment)
6. **End with future research vision**

Your presentation package is complete and ready for a compelling 15-minute technical presentation that will demonstrate sophisticated understanding of Theory of Mind in AI systems! 🎯 