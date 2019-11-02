import markdown
import os

def convert_md_html(file_name):
    cd = os.getcwd()
    folder = os.path.join(cd, 'website/content')
    md_file =os.path.join( folder, file_name)
    input_file = open(md_file, mode="r", encoding="utf-8")
    text = input_file.read()
    return markdown.markdown(text)