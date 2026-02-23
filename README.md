# Categorization Microservice

## Overview
This microservice automatically classifies user-entered tasks into one supported category using a lightweight Naïve Bayes–style text classifier.

The classifier is trained on structured task phrases with intentional keyword overlap (e.g., "organize desk" appearing in Work, Personal, Study) to improve probabilistic accuracy and reduce simple keyword bias.

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

# How to REQUEST Data from the Microservice

The microservice exposes a REST API endpoint.

### Endpoint

```
POST /categorize
```

### Full URL (Local Development)

```
http://127.0.0.1:5000/categorize
```

### Required Request Format

- Method: POST  
- Header: `Content-Type: application/json`  
- Body: JSON object containing a `title` field  

### Example Request (Python)

```python
import requests

response = requests.post(
    "http://127.0.0.1:5000/categorize",
    json={"title": "Organize Desk"}
)

print(response.json())
```

### Example Request (cURL)

```bash
curl -X POST http://127.0.0.1:5000/categorize \
-H "Content-Type: application/json" \
-d '{"title":"Organize Desk"}'
```

---

# How to RECEIVE Data from the Microservice

The microservice returns a structured JSON response.

### Success Response Format

```json
{
  "status": "success",
  "category": "Personal"
}
```

### Error Response Format

If the `title` field is missing:

```json
{
  "status": "error",
  "message": "Missing title field"
}
```

### How to Programmatically Handle the Response (Python)

```python
response = requests.post(
    "http://127.0.0.1:5000/categorize",
    json={"title": "Finish math homework"}
)

data = response.json()

if data["status"] == "success":
    print("Predicted Category:", data["category"])
else:
    print("Error:", data["message"])
```

The client program should:
1. Parse the JSON response.
2. Check the `status` field.
3. Use the `category` value for display or storage.

---

# UML Sequence Diagram

The following sequence diagram illustrates how data is requested and received.

```
Client Application            Categorization API             Prediction Service
       |                               |                             |
       | POST /categorize              |                             |
       | {"title": "..."}              |                             |
       |------------------------------>|                             |
       |                               | Validate JSON               |
       |                               |---------------------------->|
       |                               | Call prediction_service()   |
       |                               |---------------------------->|
       |                               |                             | Analyze text
       |                               |                             | Compute probabilities
       |                               |                             | Return category
       |                               |<----------------------------|
       |                               | Build JSON response         |
       |<------------------------------|                             |
       |  {"status":"success",         |                             |
       |   "category":"Work"}          |                             |
       |                               |                             |
```

### Sequence Explanation

1. The client sends a POST request containing a task title.
2. The API validates the JSON payload.
3. The API calls the internal `prediction_service()` function.
4. The prediction service processes the text and selects the most probable category.
5. The category is returned to the API.
6. The API builds a structured JSON response.
7. The client receives and parses the JSON result.

---

# Communication Method

REST API over HTTP.

---

# Performance & Reliability

- Returns exactly one category per request.
- Responds in under 500ms for single-task classification.
- Always returns structured JSON.
- Does not crash on ambiguous input.

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
python -m api.app
```

The API will be available at:

```
http://127.0.0.1:5000
```