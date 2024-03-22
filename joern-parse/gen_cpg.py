import os
import subprocess
from tqdm import tqdm
import reader



## 生成cpg.bin
def gen_cpg_bin(code_path):
    for directory in tqdm(os.listdir(code_path)[13:], desc='Generating cpg'):
        vul_line, filename, whole_uri, cwe_id = reader.get_vul_info(directory)
        source_code = code_path + whole_uri

        joern_parse_path = f"C:\Mine\PythonProject\joern\joern-cli\joern-parse"
        cpg_output_path = f"C:\Mine\PythonProject\joern\data\cpg_bin\{directory}"
        if not os.path.exists(cpg_output_path):
            os.makedirs(cpg_output_path)
        joern_parse_inst = joern_parse_path + ' ' + source_code + ' -o ' + cpg_output_path + '\cpg.bin'
        # print(joern_parse_inst)
        subprocess.run(joern_parse_inst, shell=True, stdout=subprocess.PIPE)
def neo4jcsv_export(bin_path):

    for directory in tqdm(os.listdir(bin_path)[0:1], desc='generating neo4jcsv'):
        cpg_path = f"C:\Mine\PythonProject\joern\data\cpg_bin\{directory}\cpg.bin"

        joern_export_path = f"C:\Mine\PythonProject\joern\joern-cli\joern-export --repr=all --format=neo4jcsv"
        csv_output_path = f"C:\Mine\PythonProject\joern\data\cpg_csv\{directory}\\"
        joern_export_inst = joern_export_path + ' ' + cpg_path + ' --out ' + csv_output_path
        print(joern_export_inst)
        subprocess.run(joern_export_inst, shell=True)


# if __name__ == '__main__':
#
#     print('hello')