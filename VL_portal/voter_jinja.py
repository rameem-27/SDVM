from flask import request, render_template
from jinja2 import Template
import json
import os

def jinja_voter(uid_value):
    with open(f"{uid_value}.json") as f:
        json_data = json.load(f)
        template_str = """
        Aadhaar ID: {{ json_data["uid"] }}
        Name: {{ json_data["name"] }}
        Gender: {{ json_data["gender"] }}
        Care of: {{ json_data["co"] }}
        House: {{ json_data["house"] }}
        Locality: {{json_data["loc"]}}
        Year of Birth: {{ json_data["yob"] }}
        """
        template = Template(template_str)
        rendered_template = template.render(json_data=json_data)
        print(rendered_template)
        os.remove(f"{uid_value}.json")
    return render_template('VoterFound.html',json_data=json_data)