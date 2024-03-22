import json
import os
from tqdm import tqdm

def get_lines_from_txt(root_path, directory):
    lines = set()
    txt_path = root_path + directory + '\DEBUG_slice_forward_df.txt'
    with open(txt_path, 'r') as f:
        for line, content in enumerate(f):
            content = content.split(':', 1)[1].strip()
            try:
                data = json.loads(content)
                lines.add(data['ln'])
            except json.decoder.JSONDecodeError:
                pass
    txt_path = root_path + directory + '\DEBUG_slice_backward_df.txt'
    with open(txt_path, 'r') as f:
        for line, content in enumerate(f):
            content = content.split(':', 1)[1].strip()
            try:
                data = json.loads(content)
                lines.add(data['ln'])
            except json.decoder.JSONDecodeError:
                pass
    return list(lines)


def get_vul_info(dirid):
    sarifs_path = '..\..\data\sarifs.json'
    with open(sarifs_path, 'r') as f:
        sarifs = json.load(f)
        testcases = sarifs['testCases']
    for item in testcases:
        whole_uri = item["sarif"]["runs"][0]["results"][0]["locations"][0]["physicalLocation"]["artifactLocation"]["uri"]
        ruleId = item["sarif"]["runs"][0]["results"][0]["ruleId"]
        startLine = item["sarif"]["runs"][0]["results"][0]["locations"][0]["physicalLocation"]["region"]["startLine"]
        if whole_uri.split('/')[0] == dirid:
            # print(json.dumps(item, indent=4))
            # print(whole_uri)
            # print(startLine)
            return startLine, whole_uri.split('/')[-1], whole_uri, ruleId



