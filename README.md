# Multilingual Sentiment Analysis App

## Overview

This project is a simple web application built using Streamlit that analyzes the sentiment of text in multiple languages. Users can enter one or more sentences, and the app classifies each sentence as positive, neutral, or negative using a pre-trained BERT model.

---

## Features

* Supports multiple languages such as English and Hindi
* Allows input of multiple sentences at once
* Provides clear sentiment output for each sentence
* Uses a pre-trained transformer model for reliable results
* Simple and clean user interface

---

## Tech Stack

**Language:**

* Python

**Libraries and Frameworks:**

* Streamlit (for frontend interface)
* Transformers by Hugging Face (for NLP model)
* PyTorch (for model execution)

**Model Used:**

* bert-base-multilingual-uncased-sentiment

**Concepts:**

* Natural Language Processing (NLP)
* Transformers (BERT)
* Transfer Learning
* Text Classification

---

## Installation

```bash
pip install streamlit transformers torch
```

---

## How to Run

```bash
streamlit run app.py
```

---

## How It Works

The user enters text, with each sentence on a new line. The application sends each sentence to a pre-trained BERT model, which returns a rating from 1 to 5. This rating is then converted into a sentiment label: negative, neutral, or positive.

---

## Example

**Input:**
I love this product
यह बहुत अच्छा है

**Output:**
Both sentences are classified as positive

---

## Future Improvements

* Add confidence scores for predictions
* Allow file uploads for bulk analysis
* Deploy the application online
* Extend to emotion detection

---


