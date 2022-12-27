import jinja2
import glob
import os
from pathlib import Path


def compile_directory(source_directory: str, target_directory: str, data={}):
  for source_filename in glob.glob(f"{source_directory}/**/*.sql", recursive=True):
    with open(source_filename) as f:
      j2_template = jinja2.Template(f.read(), undefined=jinja2.StrictUndefined)
    target_filename = os.path.join(target_directory, source_filename.replace(source_directory + "/", ""))
    
    target_directory = os.path.dirname(target_filename)
    Path(target_directory).mkdir(parents=True, exist_ok=True)

    with open(target_filename, "w") as f:
      f.write(j2_template.render(data))


if __name__ == "__main__":
  compile_directory("./sqls", "./compiled", {'logical_date': "2022-12-12"})
