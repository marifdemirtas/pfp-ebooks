from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

# Add a directive to create a box that displays a random number

from random import choice
import json, os

# @register_tag('plandisplay')
class ChangeableAreas(Directive):
    required_arguments = 1  # JSON file path
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {}
    option_spec.update({
        'plan': directives.unchanged,
    })
    has_content = False

    def run(self):
        file_path = os.path.join('_sources/_static/plans.json')

        with open(file_path) as f:
            data = json.load(f)

        # find the dict in the list 'data' that has 'plan_name' == self.arguments[1]
        for d in data:
            if d['plan_name'] == self.options.get('plan'):
                data = d
                break
        else:
            return [nodes.raw('', "This plan does not require any changeable areas.", format='html')]

        name = data['plan_name']
        goal = data['goal']
        code_template = data['code_template']
        
        code_lines = code_template['lines']
        changeable_areas = code_template.get('changeable_areas', {})
        changeable_areas_annotations = code_template.get('changeable_areas_annotations', {})
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
                
        # colors = [
        #     '#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6',
        #     '#ffffcc', '#e5d8bd', '#fddaec', '#f2f2f2', '#b3e2cd',
        #     '#fdcdac', '#cbd5e8', '#f4cae4', '#e6f5c9', '#fff2ae',
        #     '#f1e2cc', '#cccccc'
        # ]# from cm1Pastel1
        for i, ((placeholder, values), (_, color)) in enumerate(zip(changeable_areas.items(), changeable_areas_colors.items())):
            # Wrap the randomized text in a span for highlighting and later updates
            html_code = html_code.replace(f"$${placeholder}$$", f"<span class='changeable' style='background-color: {color}' data-original='{placeholder}'>{placeholder}</span>")

        html_code += "<div>\n"

        for i, (placeholder, description) in enumerate(changeable_areas_annotations.items()):
            html_code += f"<span style='background-color: {changeable_areas_colors[placeholder]}'>- {placeholder}: {description}</span><br>\n"


        html_code += """
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
