# Get Started with Information Extraction in Microsoft Foundry

## Overview

This lab introduces Azure Content Understanding in Microsoft Foundry.

In this lab, we use Content Understanding to extract text, understand document layout, and extract structured information from documents and images.

## Prerequisites

- Microsoft Azure account provided for the lab
- Microsoft Foundry access
- Python 3.9 or later
- Azure Content Understanding
- Azure Identity SDK

## Lab Steps

### 1. Create a Microsoft Foundry Project

1. Open Microsoft Foundry.
2. Sign in using the Azure credentials provided for the lab.
3. Enable **New Foundry** if required.
4. Create or select a Foundry project.
5. Use the provided resource group for the lab.

### 2. Open Content Understanding

1. Open the **Build** section in Microsoft Foundry.
2. Select **Services** from the left menu.
3. Open **Content Understanding**.

### 3. OCR / Read

1. Select **OCR/Read**.
2. Make sure the modality is set to **Document**.
3. Select a sample image.
4. Click **Run analysis**.
5. Review the **Markdown**, **Paragraphs**, and **Result** tabs.
6. Upload a PCB image containing readable text.
7. Run the analysis and review the extracted text.

### 4. Layout Analysis

1. Select the **Layout** analyzer.
2. Select a sample image or uploaded PCB image.
3. Click **Run analysis**.
4. Review the **Markdown**, **Paragraphs**, **Tables**, and **Result** tabs.

### 5. Receipt Analysis

1. Select **Procurement** as the analyzer type.
2. Select the **Receipt** analyzer.
3. Review the prepared analysis results.
4. Check the **Fields**, **Markdown**, **Paragraphs**, and **Result** tabs.
5. Observe how information is extracted into structured fields.

### 6. Python SDK

The Content Understanding Python SDK can be used to perform document analysis programmatically.

Install the required packages:

```bash
python -m pip install --pre azure-ai-contentunderstanding azure-identity
```
