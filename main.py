import logging
from gunicorn.app.base import BaseApplication
from app_init import create_initialized_flask_app
from flask import render_template, request
import ast
import pylint.lint
from io import StringIO
import sys
import html5lib
import cssutils
import js2py
from abilities import llm_prompt
from app_init import create_initialized_flask_app
import logging

# Flask app creation should be done by create_initialized_flask_app to avoid circular dependency problems.
app = create_initialized_flask_app()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        code = request.form['code']
        language = request.form['language']
        analysis_result = analyze_code(code, language)
        return render_template('home.html', result=analysis_result)
    return render_template('home.html')

def analyze_code(code, language):
    basic_analysis = ""
    if language == 'python':
        basic_analysis = analyze_python(code)
    elif language == 'html':
        basic_analysis = analyze_html(code)
    elif language == 'css':
        basic_analysis = analyze_css(code)
    elif language == 'javascript':
        basic_analysis = analyze_javascript(code)
    else:
        return "Unsupported language"
    
    # Use LLM for detailed analysis
    prompt = f"Analyze the following {language} code and provide a list of issues and solutions. Focus on best practices, potential improvements, and any problems in the code. Format the response as a JSON object with 'issues' and 'solutions' as keys, each containing an array of strings:\n\n{code}\n\nBasic analysis result:\n{basic_analysis}"
    analysis = llm_prompt(prompt=prompt, image_url=None, response_type='json', model='gpt-4o', temperature=0.7)
    
    return analysis

def analyze_python(code):
    # Syntax check
    try:
        ast.parse(code)
    except SyntaxError as e:
        return f"Syntax Error: {str(e)}"

    # Pylint analysis
    pylint_output = StringIO()
    reporter = pylint.lint.TextReporter(pylint_output)
    pylint.lint.Run(['-', '--output-format=text'], reporter=reporter, exit=False)
    return pylint_output.getvalue()

def analyze_html(code):
    try:
        html5lib.parse(code)
        return "HTML is valid"
    except Exception as e:
        return f"HTML Error: {str(e)}"

def analyze_css(code):
    parser = cssutils.CSSParser(fetcher=None, log=None)
    try:
        parser.parseString(code)
        return "CSS is valid"
    except Exception as e:
        return f"CSS Error: {str(e)}"

def analyze_javascript(code):
    try:
        js2py.eval_js(code)
        return "JavaScript is valid"
    except Exception as e:
        return f"JavaScript Error: {str(e)}"

class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        # Apply configuration to Gunicorn
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == "__main__":
    options = {
        "bind": "0.0.0.0:8080",
        "workers": 4,
        "loglevel": "info",
        "accesslog": "-"
    }
    StandaloneApplication(app, options).run()