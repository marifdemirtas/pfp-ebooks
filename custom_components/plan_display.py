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
        html_code = '<div>'
        html_code += f"<div><strong>Name:</strong> {name}</div>"
        html_code += f"<div><strong>Goal:</strong> {goal}</div>"
        html_code += "<pre style='background-color: #e6f7df; padding: 10px;'>"
        
        # Parse code with highlights and initial randomized values
        for line_data in code_lines:
            html_code += line_data + "\n"
        
        html_code += "</pre>"
        
        for placeholder, values in changeable_areas.items():
            random_value = values[0]
            # Wrap the randomized text in a span for highlighting and later updates
            html_code = html_code.replace(f"@@{placeholder}@@", f"<span class='changeable' style='background-color: {changeable_areas_colors[placeholder]}' data-original='{placeholder}'>{random_value}</span>")


        # Add the randomize button
        html_code += """
        <button onclick="randomizeValues()">Show Examples</button>
        <button onclick="replacePlaceholder()">Show Template</button></div>
        
        <script>
        // Possible replacements loaded directly from JSON
        const possibleValues = """ + json.dumps(changeable_areas) + """;

        function randomizeValues() {
            document.querySelectorAll('.changeable').forEach((elem) => {
                const key = elem.getAttribute('data-original');
                const values = possibleValues[key];
                elem.textContent = values[Math.floor(Math.random() * values.length)];
            });
        }

        function replacePlaceholder() {
            document.querySelectorAll('.changeable').forEach((elem) => {
                const key = elem.getAttribute('data-original');
                elem.textContent = key;
            });
        }
        </script>

        <style>
        /* CSS to highlight changeable parts */
        .changeable {
            background-color: #ffeb3b;
            padding: 0 3px;
            border-radius: 3px;
        }
        </style>
        """
        
        return [nodes.raw('', html_code, format='html')]
