import os
import xml.etree.ElementTree as ET

def create_annotation_dir(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for filename in os.listdir(src_dir):
        if filename.endswith('.xml'):
            tree = ET.parse(os.path.join(src_dir, filename))
            root = tree.getroot()

            file_number = root.find('filename').text.split('.')[0]

            with open(os.path.join(dest_dir, f"{file_number}.txt"), 'w') as out_file:
                for obj in root.iter('object'):
                    if obj.find('type').text == 'robndbox':
                        x_lt = obj.find('.//x_left_top').text
                        y_lt = obj.find('.//y_left_top').text
                        x_rt = obj.find('.//x_right_top').text
                        y_rt = obj.find('.//y_right_top').text
                        x_rb = obj.find('.//x_right_bottom').text
                        y_rb = obj.find('.//y_right_bottom').text
                        x_lb = obj.find('.//x_left_bottom').text
                        y_lb = obj.find('.//y_left_bottom').text
                        category = obj.find('name').text
                        difficult = obj.find('difficult').text

                        out_file.write(f"{x_lt}, {y_lt}, {x_rt}, {y_rt}, {x_rb}, {y_rb}, {x_lb}, {y_lb}, {category}, {difficult}\n")

if __name__ == "__main__":
    src_dir = "path/to/xml/files"
    dest_dir = "path/to/destination/directory"
    create_annotation_dir(src_dir, dest_dir)
