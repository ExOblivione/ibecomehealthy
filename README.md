## WIP!

# I Become Healthy 🌱

A health and wellness application to help you on your journey to becoming healthier.

## Getting Started

Follow these simple steps to set up and run the application:

### 1. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Azure AI Foundry
Create a `config.py` file in the project root with your Azure AI Foundry endpoint:

```python
def get_config():
    return {
        "agent": {
            "endpoint": "https://<your-service>.services.ai.azure.com/api/projects/<your-project>"
        }
    }
```

> **Note:** Replace `<your-service>` and `<your-project>` with your actual Azure AI Foundry service and project names.

### 4. Run the Application
```bash
python test.py
```

## What's Next?

Once you have the application running, you can start exploring the features and begin your healthy lifestyle journey!

