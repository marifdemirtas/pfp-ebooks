'''
Create copies of ./templates/plan_template.rst under ./_sources with the following structure:

From ./_sources/_static/_new/plans.json:
Enumerate each plan starting with group, then order, and then name if their groups and orders are the same
Create a page for each plan in the JSON file, with the following structure:

Naming: plan_{group}_{order}_{plan_name}.rst
In the copied file, replace:
{plan_name} with the plan_name from the JSON file, spaces removed
{plan_id} with the Plan{your_enumeration} (e.g. Plan1)
{plan_metadata_description} with plan['metadata']['description']
{plan_metadata_usage} with plan['metadata']['usage']

'''

from pathlib import Path
import json, re
from shutil import copyfile
import random

with open('./_sources/_static/new/plans.json') as f:
    data = json.load(f)

for i, plan in enumerate(sorted(data, key=lambda x: (x['group'], x['order'], x['plan_name']))):
    group = plan['group']
    order = plan['order']
    name = plan['plan_name']
    plan_id = f"Plan{i + 1}"
    plan_name = name.replace(" ", "")
    plan_metadata_description = plan['plan_metadata']['description']
    plan_metadata_usage = plan['plan_metadata']['usage']

    # Copy the template
    source = Path('./templates/plan_template.rst')
    destination = Path(f'./_sources/plan_{group}_{order}_{plan_name}.rst')
    copyfile(source, destination)

    # Replace the placeholders
    with open(destination, 'r') as f:
        content = f.read()

    content = content.replace("{plan_name}", name)
    content = content.replace("{plan_id}", plan_id)
    content = content.replace("{plan_metadata_description}", plan_metadata_description)
    content = content.replace("{plan_metadata_usage}", plan_metadata_usage)


    ### Replace {plan_code_click} with the code template lines concatenated
    clickable_code = ""
    for line_data in plan['code_template']['lines']:
        line_data = f"    :click-incorrect:{line_data}:endclick:"
        if '$$' in line_data:
            splitted_line = line_data.split('$$')
            new_line = ""
            for piece in splitted_line:
                if piece in plan['code_template']['changeable_areas']:
                    piece = f":endclick::click-correct:{random.choice(plan['code_template']['changeable_areas'][piece])}:endclick::click-incorrect:"
                new_line += piece
            #matches = re.findall(r'\$\$(.*?)\$\$')
            #replacements = [random.choice(plan['code_template']['changeable_areas'][match]) for match in matches]
            #line_data = re.sub(r'\$\$(.*?)\$\$', r':endclick::click-correct:$$replace$$:endclick::click-incorrect:', line_data)
            line_data = new_line
        clickable_code += line_data + "\n"

    content = content.replace("{plan_code_click}", clickable_code)

    ### Replace {plan_code_fill} with the code template lines concatenated
    fillable_code = "   Fill in the plan to...\n\n"
    blank_chosen = False
    for line_data in plan['code_template']['lines']:
        if line_data == "":
            continue # fillable_code += "whitespace character, not space"
        if '$$' not in line_data or blank_chosen: 
            fillable_code += f"   ``{line_data}``" + "\n\n"
        else:
            splitted_line = line_data.split('$$')
            end_line = "".join(splitted_line[2:])
            if end_line == "":
                fillable_code += f"   ``{splitted_line[0]}``" + " |blank| " + "\n\n"
            else:
                fillable_code += f"   ``{splitted_line[0]}``" + " |blank| " + f"``{end_line}``" + "\n\n"
            answers = plan['code_template']['changeable_areas'][splitted_line[1]]
            blank_chosen = True

    fillable_code += "\n"
    for ans in answers:
        ans_escaped = ans.replace(' ', '\s').replace(':', '\:')
        fillable_code += "   {dash}    :{answer}: Correct.\n".format(answer=ans_escaped, dash='-' if ans==answers[0] else ' ')
    fillable_code += "        :.*: Incorrect.\n"

    content = content.replace("{plan_code_fill}", fillable_code)

    # Replace {plan_code_fill} with the code template lines concatenated

    content = content.replace('\t', '    ')

    with open(destination, 'w') as f:
        f.write(content)

    print(f"Created: {destination}")

print("Done")

