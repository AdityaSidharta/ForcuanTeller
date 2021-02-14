import os

project_dir = os.path.dirname(os.path.dirname(os.path.dirname((os.path.realpath(__file__)))))

config_dir = os.path.join(project_dir, 'config')
data_dir = os.path.join(project_dir, 'data')
script_dir = os.path.join(project_dir, 'script')
notebook_dir = os.path.join(project_dir, 'notebook')

load_dir = os.path.join(data_dir, "load")
report_dir = os.path.join(data_dir, 'report')
transform_dir = os.path.join(data_dir, 'transform')

config_path = os.path.join(config_dir, 'config.yaml')
