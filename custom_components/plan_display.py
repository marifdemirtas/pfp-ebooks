from docutils import nodes
from docutils.parsers.rst import Directive

# Add a directive to create a box that displays a random number

from random import choice
import json, os

# @register_tag('plandisplay')
class PlanDisplay(Directive):
    required_arguments = 1  # JSON file path

    def run(self):
        file_path = self.arguments[0]
        # with open(file_path) as f:
        #     data = json.load(f)

        data = {
            "goal": "Get info from a single tag",
            "code": [
                {
                    "line": "# Get first tag of a certain type from the soup"
                },
                {
                    "line": "tag = soup.find('$$a$$', class_='$$item-teaser--more$$')",
                    "changeable": {
                        "a": ["a", "div", "span"],
                        "item-teaser--more": ["item-teaser--more", "item-header", "card"]
                    }
                },
                {
                    "line": "# Get info from tag"
                },
                {
                    "line": "info = tag.get('$$href$$')",
                    "changeable": {
                        "href": ["href", "src", "title"]
                    }
                }
            ]
        }
        
        goal = data['goal']
        code_lines = data['code']
        
        # HTML structure
        html_code = f"<div><div><strong>Goal:</strong> {goal}</div>"
        html_code += "<pre style='background-color: #e6f7df; padding: 10px;'>"
        
        # Parse code with highlights and initial randomized values
        for line_data in code_lines:
            line = line_data['line']
            if 'changeable' in line_data:
                for original_text, possible_replacements in line_data['changeable'].items():
                    # Randomize initial value
                    # random_value = choice(possible_replacements)
                    random_value = possible_replacements[0]
                    # Wrap the randomized text in a span for highlighting and later updates
                    line = line.replace(f"$${original_text}$$", f"<span class='changeable'>{random_value}</span>")
            html_code += line + "\n"
        
        html_code += "</pre>"
        
        # Add the randomize button
        html_code += """
        <button onclick="randomizeValues()">Randomize</button></div>
        
        <script>
        // Possible replacements loaded directly from JSON
        const possibleValues = """ + json.dumps(
            {key: values for line in code_lines if 'changeable' in line for key, values in line['changeable'].items()}
        ) + """;

        function randomizeValues() {
            document.querySelectorAll('.changeable').forEach((elem) => {
                const key = elem.getAttribute('data-original');
                const values = possibleValues[key];
                elem.textContent = values[Math.floor(Math.random() * values.length)];
            });
        }

        // Set data-original attribute to match JSON keys for easy access
        document.querySelectorAll('.changeable').forEach((elem) => {
            elem.setAttribute('data-original', elem.textContent);
        });
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
