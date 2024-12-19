# Project01: Document Layout Analysis

This repository contains code, notebooks, and resources for document layout analysis using various models, including YOLOv10, LayoutXLM, and LiLT. The project includes scripts for pre-processing documents, performing inference, and visualizing results.

---

## **Usage Guide**

### **Step 1: Document Classification**
Use `read_documents.ipynb` to classify and organize your input files into categories. This notebook helps ensure the documents are correctly prepared for the subsequent steps.

### **Step 2: Convert PDF to Images**
Run `run.py` to convert PDF documents into images. This script processes each page of the input PDFs and saves them as images, which are used as input for the models.

### **Step 3: YOLOv10 Inference**
For document layout analysis using the YOLOv10 model:
- Refer to the official repository: [YOLOv10-Document-Layout-Analysis](https://github.com/moured/YOLOv10-Document-Layout-Analysis).
- Follow the usage instructions provided in the repository for setting up the model and running inference.

### **Step 4: LayoutXLM and LiLT Inference**
For running inference with LayoutXLM and LiLT models:
- Refer to the notebook available in the following repository for detailed instructions: [LayoutXLM Base Model Inference](https://github.com/piegu/language-models/blob/master/inference_on_LayoutXLM_base_model_finetuned_on_DocLayNet_base_in_any_language_at_levellines_ml384.ipynb).
- These models are pre-trained for document layout analysis tasks and can handle various languages.

### **Step 5: Visualization of Results**
Use `result_visualization.ipynb` to visualize the results of the model inferences. This notebook provides a visual representation of the analyzed document layouts.

---

## **Additional Files**

- `NLP_Presentation.pptx`: PowerPoint presentation from the 12th of December (12.13), summarizing the project progress and findings.
- `Project_Report_Group01.pdf`: Final report detailing the project methodology, results, and conclusions.

---

## **Dependencies**
Make sure to install the required Python libraries before running the scripts or notebooks. Use the following command to install the dependencies:
```bash
pip install -r requirements.txt
