# Categorization Microservice

## Overview
This microservice automatically classifies user-entered tasks into one supported category using a lightweight Naïve Bayes–style text classifier.

The classifier is trained on structured task phrases with intentional keyword overlap (e.g., "organize desk" appearing in Work, Personal, Study, and Admin) to improve probabilistic accuracy and reduce simple keyword bias.

Supported Categories:
- Study
- Work
- Health
- Personal
- Finance
- Leisure
- Social

---

## Sprint Goal
To implement a REST API that:
- Accepts a task title
- Returns exactly one valid category
- Provides a consistent JSON response format
- Handles ambiguous input without crashing

---

## Communication Method
REST API

---

## User Stories

### 1. Automatic Categorization

**As a user adding a new task,**  
I want the system to automatically categorize my task  
so that I can stay organized without manually selecting a category.

**Acceptance Criteria**

Functional:
- Given a task title,
- When the microservice is called,
- Then it shall return exactly one category from the supported list.

Non-Functional:
- The returned category must be human-readable.
- The service must not crash on unclear input.

---

### 2. Label Correction

**As a user reviewing my tasks,**  
I want to update a category if it was misclassified  
so that my planner remains accurate.

**Acceptance Criteria**

Functional:
- Given an existing task with a category,
- When a new valid category is submitted,
- Then the updated category shall be stored.

Non-Functional:
- If an invalid category is submitted, the system must not crash.

---

### 3. Label Clarity

**As a user,**  
I want the category label returned in a consistent format  
so that I can clearly understand how my task was classified.

**Acceptance Criteria**

Functional:
- Given a valid request,
- When the service responds,
- Then the response must include a `category` field in a consistent format.

Non-Functional:
- Response time must be under 500ms.
- JSON structure must remain consistent across requests.

---

## API Specification

### Endpoint
POST `/categorize`

### Request Body
```json
{
  "title": "Organize Desk"
}
```

### Response Body 
```json
{
  "status": "success",
  "category": "Personal"
}
```
## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Jeeya7/Categorization-Microservice.git
cd Categorization-Microservice
```

---

## Option A: Using Conda

### 2. Create a Conda Environment

```bash
conda create -n categorizer-env python=3.10
```

### 3. Activate the Environment

```bash
conda activate categorizer-env
```

### 4. Install Dependencies

```bash
conda install --file requirements.txt
```

---

## Option B: Using pip (venv)

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

Mac/Linux:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run the Microservice

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```