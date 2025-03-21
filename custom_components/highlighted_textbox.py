from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

class HighlightedTextbox(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'title': directives.unchanged,
        'color': directives.unchanged,
        'highlight-color': directives.unchanged,
        'initially-visible': directives.flag,
    }
    has_content = True

    def run(self):
        title = self.options.get('title', 'Note')
        color = self.options.get('color', '#f9f9c6')  # Default light yellow
        highlight_color = self.options.get('highlight-color', '#ffeb3b')  # Default bright yellow
        initially_visible = 'initially-visible' in self.options
        
        # Generate a unique ID for this textbox
        import random
        unique_id = f"highlighted-textbox-{random.randint(1000, 9999)}"
        
        content = '\n'.join(self.content)
        
        display_style = "block" if initially_visible else "none"
        toggle_text = "Hide" if initially_visible else "Show"
        toggle_icon = "▼" if initially_visible else "▶"
        
        html = f"""
        <div class="highlighted-textbox-container">
            <button class="highlighted-textbox-toggle" onclick="toggleTextbox('{unique_id}', this)">
                <span class="toggle-icon" id="{unique_id}-icon">{toggle_icon}</span> {title}
            </button>
            <div class="highlighted-textbox" id="{unique_id}" style="background-color: {color}; display: {display_style};">
                <div class="highlighted-textbox-content">
                    {content}
                </div>
            </div>
        </div>
        
        <script>
        function toggleTextbox(id, button) {{
            var textbox = document.getElementById(id);
            var icon = document.getElementById(id + '-icon');
            
            if (textbox.style.display === 'none') {{
                textbox.style.display = 'block';
                // Apply highlight animation
                textbox.style.backgroundColor = '{highlight_color}';
                setTimeout(function() {{
                    textbox.style.backgroundColor = '{color}';
                }}, 500);
                icon.textContent = '▼';
            }} else {{
                textbox.style.display = 'none';
                icon.textContent = '▶';
            }}
        }}
        </script>
        
        <style>
        .highlighted-textbox-container {{
            margin: 20px 0;
            font-family: system-ui, -apple-system, sans-serif;
        }}
        
        .highlighted-textbox-toggle {{
            width: 100%;
            padding: 10px 15px;
            background: #f8f9fa;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            text-align: left;
            cursor: pointer;
            display: flex;
            align-items: center;
            font-size: 16px;
            font-weight: 600;
            color: #2c3e50;
            transition: background-color 0.2s ease;
        }}
        
        .highlighted-textbox-toggle:hover {{
            background: #eaecef;
        }}
        
        .toggle-icon {{
            margin-right: 8px;
            font-size: 12px;
            transition: transform 0.2s ease;
        }}
        
        .highlighted-textbox {{
            margin-top: 10px;
            border-radius: 8px;
            border: 1px solid #e1e4e8;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            padding: 15px;
            transition: all 0.5s ease;
        }}
        
        .highlighted-textbox-content {{
            color: #34495e;
            font-size: 15px;
            line-height: 1.5;
        }}
        </style>
        """
        
        return [nodes.raw('', html, format='html')] 