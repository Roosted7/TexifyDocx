# TexifyDocx  📝➕🧮

Transform LaTeX formulas `$$ ... $$` in Microsoft Word documents directly into Math objects (MathML) with ease.
Made with the help of LLM's, to convert a paper written in Google Docs (and Auto Latex-Equations) for submission.

## 🚀 Features
- Convert inline and block LaTeX math to Word’s native math objects.
- Supports equation numbering with `\tag{}`.
- Preserves Word formatting (headings, bullet points, etc.).
- Handles common LaTeX commands like `\degree`.

## ⚡ Installation
```bash
pip install --user git+https://github.com/Roosted7/TexifyDocx.git
```

Or clone the repository:

```bash
git clone https://github.com/yourusername/TexifyDocx.git
cd TexifyDocx
pip install --user .
```

---

## 🛠️ Usage

### 1️⃣ **As a Python Library**

```python
from texifydocx import convert_docx

convert_docx('input.docx', 'output.docx')
```

### 2️⃣ **From the Command Line**

```bash
python -m texifydocx input.docx output.docx
```

---

## 📋 Example

Check the `examples/convert_example.py` for a demonstration.

---

## 📝 License

This project is licensed under the MIT License.