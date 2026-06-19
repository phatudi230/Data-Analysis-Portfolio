# GlobalLink Logistics — Operational Bottleneck & Financial Impact Analysis
### Combined Data Analytics & Business Analysis Case Study

<img width="1371" height="753" alt="Screenshot 2026-01-31 205615" src="https://github.com/phatudi230/Data-Analysis-Portfolio/blob/main/GlobalLink%20Logistics%20-%20Bottleneck%20Analysis/Screenshot%202026-06-19%20225739.png" />

---

##  Project Overview

A self-initiated, end-to-end consulting-style project combining 
Data Analytics and Business Analysis to identify, quantify and 
solve an operational bottleneck for a simulated logistics company 
GlobalLink Logistics. This project demonstrates the full 
analytical lifecycle: data engineering, exploratory analysis, 
financial impact modelling, interactive dashboarding and 
strategic business recommendations.

---

##  Business Problem

**Business Context:** Acting as Lead Analyst for GlobalLink 
Logistics, a warehouse operation reported a 12% drop in order 
fulfillment speed over the last quarter. The Warehouse Operations 
Manager is frustrated overtime costs are rising, but orders 
aren't leaving the floor any faster.

**Mission:** Identify the "Bottleneck of Death" the specific 
station causing the most downstream financial and operational 
impact, and recommend a data-backed restructuring plan.

---

## Tools & Methods

- Python (Pandas, NumPy, Matplotlib) — Data generation & analysis
- Power BI & DAX — Interactive dashboard & financial modelling
- Business Case Writing — Executive summary & action plan
- Pareto Analysis (80/20 Principle)
- Financial Impact Modelling
- Process & Shift Optimization Strategy

---

## Methodology

### 1. Data Engineering
Since no public dataset matched the exact business scenario, a 
realistic synthetic dataset was generated using Python, 2,000 
orders across 4 stations (A, B, C, D) and 2 shifts (Day/Night), 
with intentional, realistic performance variation built into 
each station and shift combination.

### 2. Data Integrity Validation
During Peak Hour Analysis, a shift-timestamp misalignment was 
identified in the initial dataset (e.g., "Night" shift orders 
appearing at 11:00). Shifts were corrected based on actual 
timestamps:
- **Day Shift:** 06:00 – 17:00
- **Night Shift:** 18:00 – 05:00

This correction significantly changed the analysis outcome, 
shifting the primary bottleneck period from Night to Day 
operations — reinforcing the importance of data validation 
before drawing business conclusions.

### 3. Financial Impact Calculation
- **Rework Cost** = (Rework Time / 60) × Hourly Labor Rate
- **Delay Cost** = ((Total Time − 15min Threshold) / 60) × Hourly Labor Rate
- Bottleneck Threshold defined as any process exceeding 15 minutes

### 4. Rate-Normalized Analysis
Initial analysis comparing Day vs Night total costs revealed an 
apparent "Night Savings" pattern. Further investigation using 
**Cost-Per-Order** (rather than total cost) revealed this was 
largely a volume effect, not a genuine performance difference,
demonstrating the importance of normalizing data before drawing 
conclusions.

---

## Key Findings

| Station | Day Cost/Order | Night Cost/Order | Verdict |
|---------|----------------|-------------------|---------|
| Station B | R0.24 | R0.24 | Star performer: consistent both shifts |
| Station A | R0.49 | R0.54 | Solid Day performer: monitor at night |
| Station D | R1.20 | R1.17 | Reliable mid-tier performer |
| Station C | R3.64 | R3.48 | Bottleneck of Death: 15x Station B's cost |

**Headline Finding:** Station C costs **15 times more per order** 
than Station B, regardless of shift, confirming it as the 
primary, consistent cost driver across all operations.

---

##  Recommendations

### The 80/20 Restructuring Plan

| Shift | Stations | Purpose |
|-------|----------|---------|
| Day (06:00–17:00) | A, B, D | High-volume peak operations |
| Night (18:00–05:00) | C | Training + low-volume controlled rework |

1. **Restrict Station C to Night shift only** — reduces exposure 
during high-volume peak Day operations
2. **Redistribute Station C's Day volume** to Stations A, B and D
3. **Use Station C's Night shift as a training ground** — staff 
develop capability fixing real defects in a low-risk, low-volume 
environment
4. **Expand Station B operations** — proven consistent performer, 
ideal candidate for increased capacity
5. **Monitor Station A night performance** — shows marginally 
higher costs at night, requires oversight

---

## Projected Impact

- Significant reduction in Day shift peak operational losses
- Zero additional capital investment required, restructuring 
existing resources, not purchasing new equipment
- Long-term Station C capability improvement through structured 
night-shift training
- Projected annual savings calculated via Before/After simulation 
in Power BI dashboard

---

## Dashboard Pages

1. **Executive Overview** — KPI cards, Pareto chart, interactive 
filters
2. **Station Deep Dive** — Cost and defect rate breakdown by 
station and shift
3. **Shift Analysis** — Day vs Night comparison, rate-normalized 
findings
4. **Recommendations & Impact** — Before/After simulation, action 
plan, ROI projection

---

## Files

| File | Description |
|------|-------------|
| `data/Ops_data.py` | Synthetic dataset generation script |
| `data/globallink_operations_final.csv` | Generated dataset |
| `data/analysis.ipynb` | Full EDA & financial analysis notebook |
| `data/Operation BottleneckReport.pbix` | Interactive Power BI dashboard |
| `data/Screenshots/` | Dashboard page screenshots |

---

## Limitations & Next Steps

- Dataset is synthetically generated to simulate realistic 
operational conditions; real-world data may reveal additional 
complexity
- Recommendations would benefit from real implementation 
validation and A/B testing
- Future iteration could incorporate predictive modelling to 
forecast bottleneck risk before it occurs

---

## Contact

- **LinkedIn:** [Phatudi Daniel Modiba](http://www.linkedin.com/in/phatudi-daniel-modiba)
- **Portfolio:** [phatudi230.github.io/Phatudi_Portfolio](https://phatudi230.github.io/Phatudi_Portfolio)
