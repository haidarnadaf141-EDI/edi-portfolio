# EDI Portfolio – 850 Purchase Order Example

This repository showcases a complete **EDI mapping and transformation workflow** using an **EDI 850 Purchase Order** document.  
It demonstrates how raw EDI data is mapped, transformed, and validated into a structured format for downstream systems.  

---

## 📂 Repository Contents

| File | Description |
|------|-------------|
| `850_example.edi` | Raw ANSI X12 850 Purchase Order sample. |
| `mapping_spec.csv` | Mapping specification from EDI fields → target fields. |
| `mapping_doc_850.md` | Detailed mapping document with explanations. |
| `transform.py` | Transformation logic (Python example) that parses and maps the EDI file. |
| `output_sample.csv` | Sample transformed output after running `transform.py`. |
| `inbound_bpml_example.xml` | Example IBM Sterling Integrator BPML workflow for inbound processing. |
| `README.md` | Documentation for this project (you’re reading it!). |

---

## 🔄 Workflow Overview

1. **Inbound EDI 850**  
   File received in `.edi` format from trading partner.

2. **Mapping**  
   - `mapping_spec.csv` defines how each EDI segment/element maps to business fields.  
   - `mapping_doc_850.md` provides documentation of the mapping rules.

3. **Transformation**  
   - `transform.py` simulates mapping logic.  
   - Outputs a clean `.csv` file (`output_sample.csv`) for easy consumption.

4. **Workflow Integration**  
   - `inbound_bpml_example.xml` shows how Sterling Integrator (SI) could orchestrate the process.  
   - Steps: pickup → validate → transform → send to ERP.

---

📌 Tested On:
- IBM Sterling Integrator (example BPM flow)
- Cleo Clarify (mapping spec alignment)
- Open-source BOTS EDI translator (Python-based transform)

## 🚀 How to Run Transformation

1. Clone this repository:
   ```bash
   git clone https://github.com/haidarnadaf141/edi-portfolio.git
   cd edi-portfolio
