# TECHIN 510 Lab 1

A personal website for TECHIN 510 Lab 1.

## How to Run

Open the terminal and run the following commands:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## What's Included

- `app.py`: The main Flask application

## Lessons Learned

- How to use Streamlit to create a simple website
- How to use requirements.txt to manage Python dependencies
- How to use GitHub Actions to deploy a website to Azure App Service
- How to change the size of a picture

## Questions / Uncertainties

- What if I want to make the profile picture round?
    - Use <style> tag and define the border-radius as 50%
- How to use a two column layout?
    - Use *col1, col2 = st.columns(2)* function to define two columns. For each column, use *with col1* or *with col2* to define the column.