import os
import xml.etree.ElementTree as ET
import json

folder_path = 'tk'  # 文件夹路径
cnt = 1
num = 1036
os.mkdir("json")
# 循环遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    file_path = folder_path + "\\" + filename  # XML文件路径

    # 解析XML文件
    tree = ET.parse(file_path)

    # 获取根元素
    root = tree.getroot()

    # 创建一个空字典
    data_dict = {}

    # 遍历XML文件中的所有item标签
    for item in root.findall('item'):
        # 获取title标签的内容作为字典的key
        key = item.find('title').text.strip()

        # 获取除solution和一些不需要的标签外的其他标签的内容作为字典的value
        value = {}
        for child in item:
            if child.tag not in ('solution', 'time_limit', 'memory_limit', 'url', 'generator', 'version'):
                value[child.tag] = child.text.strip() if child.text else ''

        # 将key和value存入字典中
        data_dict[key] = value

    # 遍历字典，将每个key-value对分别打印出来
    print(filename, num, cnt)
    # for key, value in data_dict.items():
    #     for k, v in value.items():
    #         print(k, data_dict[key][k])
    #     print()

    json_dict = {
        "display_id": "",
        "title": "",
        "description": {
            "format": "html",
            "value": "无"
        },
        "tags": [
            "FATE_YO"
        ],
        "input_description": {
            "format": "html",
            "value": "无"
        },
        "output_description": {
            "format": "html",
            "value": "无"
        },
        "test_case_score": [
            {
                "score": 100,
                "input_name": "1.in",
                "output_name": "1.out"
            }
        ],
        "hint": {
            "format": "html",
            "value": "无"
        },
        "time_limit": 1000,
        "memory_limit": 256,
        "samples": [
            {
                "input": "无",
                "output": "无"
            }
        ],
        "template": {},
        "spj": None,
        "rule_type": "ACM",
        "source": "来源",
        "answers": []
    }

    for key in data_dict:
        json_dict["display_id"] = num
        json_dict["title"] = data_dict[key]["title"]
        if data_dict[key].get("description") != None:
            if data_dict[key].get("description") != " " and data_dict[key].get("description") != "":
                json_dict["description"]["value"] = data_dict[key]["description"]
        if data_dict[key].get("input") != None:
            if data_dict[key].get("input") != " " and data_dict[key].get("input") != "":
                json_dict["input_description"]["value"] = data_dict[key]["input"]

        if data_dict[key].get("output") != None:
            if data_dict[key].get("output") != " " and data_dict[key].get("output") != "":
                json_dict["output_description"]["value"] = data_dict[key]["output"]


        if (data_dict[key].get("hint") is None):
            json_dict["hint"]["value"] = "无"
        else:
            json_dict["hint"]["value"] = data_dict[key]["hint"]
        # print(data_dict[key].get("input"))
        if (data_dict[key].get("sample_input") is None):
            json_dict["samples"][0]["input"] = "无"
        else:
            if data_dict[key]["sample_input"] == "":
                json_dict["samples"][0]["input"] = "无"
            else:
                json_dict["samples"][0]["input"] = data_dict[key]["sample_input"]
        if (data_dict[key].get("sample_output") is None):
            json_dict["samples"][0]["output"] = "无"
        else:
            if data_dict[key]["sample_output"] != "":
                json_dict["samples"][0]["output"] = data_dict[key]["sample_output"]
        json_dict["source"] = "FATE_YO"

    json_data = json.dumps(json_dict, indent=4)

    # 将JSON格式的文本写入文件

    os.mkdir("json\\" + str(cnt))
    path = "json\\" + str(cnt) + '\\'
    with open(path + "problem.json", 'w') as f:
        f.write(json_data)
    os.mkdir(path + "testcase")
    test = path + "testcase\\"
    for key in data_dict:
        with open(test + "1.in", 'w') as f:
            if (data_dict[key].get("test_input") is None):
                if data_dict[key].get("sample_input") is None:
                    f.write("wu")
                else:
                    # print(cnt, data_dict[key]["sample_input"],"sample_input")
                    f.write(data_dict[key]["sample_input"])
            else:
                # print(cnt, data_dict[key]["test_input"],"test_input")
                f.write(data_dict[key]["test_input"])
        with open(test + "1.out", 'w') as f:
            if (data_dict[key].get("test_output") is None):
                # print(cnt, data_dict[key]["sample_output"],"sample_output")
                f.write(data_dict[key]["sample_output"])
            else:
                # print(cnt, data_dict[key]["test_output"],"test_output")
                f.write(data_dict[key]["test_output"])

    num += 1
    cnt += 1
