import xml.etree.ElementTree as ET

# Define path to files below:
well_documents_path = "well_documents.txt"
ps_files_path = "PS_files.xml"
result_file_name = "result.txt"

tree = ET.parse(ps_files_path)
root = tree.getroot()

ps_files = []
for file_node in root.findall("Queue/Server/File"):
    remote_file_node = file_node.find("RemoteFile")
    remote_file_node_text = remote_file_node.text
    last_slash = remote_file_node_text.rfind("\\") + 1
    file_name_trimmed = remote_file_node_text[last_slash:]
    first_underscore = file_name_trimmed.find("_") + 1
    if first_underscore < 0:
        first_underscore = 0
    file_name_trimmed = file_name_trimmed[first_underscore:]
    ps_files.append(file_name_trimmed)

well_documents_file = open(well_documents_path)
missing_files = []
while True:
    line = well_documents_file.readline()
    if not line:
        break
    last_slash = line.rfind("\\") + 1
    file_name = line[last_slash:-1]

    if file_name not in ps_files:
        missing_files.append(line)

file_write = open(result_file_name, "w+")
for document_path in missing_files:
    file_write.write(document_path + "\n")

well_documents_file.close()
file_write.close()
