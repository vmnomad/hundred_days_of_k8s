import markdown
import os
module_path = os.path.abspath(__file__)
dir_path = os.path.dirname(module_path)
def convert_md_html(file_name):

    folder = os.path.join(dir_path, 'content')
    md_file =os.path.join( folder, file_name)
    input_file = open(md_file, mode="r", encoding="utf-8")
    text = input_file.read()
    return markdown.markdown(text)