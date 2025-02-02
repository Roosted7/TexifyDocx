# utils.py

import re
from docx.oxml import parse_xml
import latex2mathml.converter
import mathml2omml

def extract_latex_and_tag(latex_string):
    """
    Extracts LaTeX content and equation tags from a string.
    Supports \tag{A.1} or \tagA.1 formats.
    """
    tag_match = re.search(r'\\tag(?:\{([^}]+)\}|([A-Za-z0-9.]+))', latex_string)
    if tag_match:
        tag = tag_match.group(1) if tag_match.group(1) else tag_match.group(2)
        latex_content = re.sub(r'\\tag(?:\{[^}]+\}|[A-Za-z0-9.]+)', '', latex_string).strip()
        return latex_content, tag
    return latex_string, None

def create_math_xml(latex_string, inline=True):
    """
    Converts LaTeX to OMML (Office Math Markup Language) for Word compatibility.
    Supports inline and block math formatting.
    """
    latex_string = latex_string.replace(r'\degree', '^{\circ}')
    mathml_output = latex2mathml.converter.convert(latex_string)
    omml_output = mathml2omml.convert(mathml_output)
    
    if inline:
        xml_output = (
            f'<m:oMath xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
            f'{omml_output}'
            f'</m:oMath>'
        )
    else:
        xml_output = (
            f'<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
            f'{omml_output}'
            f'</m:oMathPara>'
        )
    
    return parse_xml(xml_output)[0]
