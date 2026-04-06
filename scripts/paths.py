"""
_summary_
"""

from pathlib import Path

project_path = Path(__file__).parents[1].absolute()

data_path = project_path / 'data'

input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)


output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)


tabs_path = output_path / 'tabs'
tabs_path.mkdir(exist_ok=True)

maps_path = output_path / 'maps'
maps_path.mkdir(exist_ok=True)

shps_path = output_path / 'shps'
shps_path.mkdir(exist_ok=True)

imgs_path = output_path / 'imgs'
imgs_path.mkdir(exist_ok=True)


if __name__ == '__main__':
    print(project_path)
