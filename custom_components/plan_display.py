from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

# Add a directive to create a box that displays a random number

from random import choice
import json, os

# @register_tag('plandisplay')
class PlanDisplay(Directive):
    required_arguments = 1  # JSON file path - not in use
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {}
    option_spec.update({
        'plan': directives.unchanged,
    })
    has_content = False

    def run(self):
        file_path = os.path.join('_sources/plans.json')

        with open(file_path) as f:
            data = json.load(f)

        # find the dict in the list 'data' that has 'plan_name' == self.arguments[1]
        for d in data:
            if d['plan_name'] == self.options.get('plan', ''):
                data = d
                break
        else:
            data = data[0]

        name = data['plan_name']
        goal = data['goal']
        code_template = data['code_template']
        
        code_lines = code_template['lines']
        changeable_areas = code_template.get('changeable_areas', {})
        changeable_areas_colors = code_template.get('changeable_areas_colors', {})

        # HTML structure
        html_code = '<div class="plan-display-container">'
        html_code += '<div class="plan-header">'
        # html_code += f'<h3 class="plan-name"></h3>'
        html_code += f'<h5 class="plan-goal">{name}: {goal}</h5>'
        html_code += '</div>'
        html_code += '<div class="code-container">'
        html_code += "<pre>"
        
        # Parse code with highlights and initial randomized values
        for line_data in code_lines:
            html_code += line_data + "\n"
        
        html_code += "</pre></div>"
        
        for placeholder, values in changeable_areas.items():
            random_value = values[0]
            # Wrap the randomized text in a span for highlighting and later updates
            html_code = html_code.replace(f"@@{placeholder}@@", f"<span class='changeable' style='background-color: {changeable_areas_colors[placeholder]}' data-original='{placeholder}'>{random_value}</span>")

        # Add the randomize button
        html_code += """
        <div class="button-container">
            <button class="plan-button" onclick="randomizeValues()">Show Examples</button>
            <button class="plan-button" onclick="replacePlaceholder()">Show Template</button>
        </div>
        </div>
        
        <script>
        // Possible replacements loaded directly from JSON
        const possibleValues = """ + json.dumps(changeable_areas) + """;

        function randomizeValues() {
            document.querySelectorAll('.changeable').forEach((elem) => {
                const key = elem.getAttribute('data-original');
                const values = possibleValues[key];
                elem.textContent = values[Math.floor(Math.random() * values.length)];
                elem.classList.add('highlight');
                setTimeout(() => elem.classList.remove('highlight'), 300);
            });
        }

        function replacePlaceholder() {
            document.querySelectorAll('.changeable').forEach((elem) => {
                const key = elem.getAttribute('data-original');
                elem.textContent = key;
                elem.classList.add('highlight');
                setTimeout(() => elem.classList.remove('highlight'), 300);
            });
        }
        </script>

        <style>
        .plan-display-container {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
            padding: 20px;
            font-family: system-ui, -apple-system, sans-serif;
        }

        .plan-header {
            margin-bottom: 20px;
        }

        .plan-name {
            font-size: 24px;
            color: #2c3e50;
            margin: 0 0 10px 0;
            font-weight: 600;
        }

        .plan-goal {
            color: #34495e;
            font-size: 16px;
            line-height: 1.5;
            margin: 0;
        }

        .code-container {
            background: #f8f9fa;
            border-radius: 6px;
            margin: 15px 0;
            overflow: auto;
        }

        .code-container pre {
            margin: 0;
            padding: 15px;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', monospace;
            font-size: 14px;
            line-height: 1.5;
            color: #2c3e50;
        }

        .button-container {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }

        .plan-button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: background-color 0.2s ease;
        }

        .plan-button:hover {
            background-color: #2980b9;
        }

        .changeable {
            padding: 2px 4px;
            border-radius: 4px;
            transition: all 0.2s ease;
        }

        .changeable.highlight {
            transform: scale(1.1);
        }
        </style>
        """
        
        return [nodes.raw('', html_code, format='html')]
