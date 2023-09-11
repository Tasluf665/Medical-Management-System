import json


def read_from_json():
    try:
        with open("record.json", 'r') as f:
            text = f.read()
            x = json.loads(text)
            return x
    except:
        return None


class jsonfilehandeler:
    def __init__(self, dicto, id, name):
        self.dicto = dicto
        self.id = id
        self.name = name
        self.main()

    def main(self):
        main_list = []
        pre_info = read_from_json()

        if pre_info is None:
            rec = dict()
            rec["ID"] = self.id
            rec["Name"] = self.name
            rec["RecordList"] = list()
            rec["RecordList"].append(self.dicto)
            main_list.append(rec)

            with open("record.json", "w") as f:
                json.dump(main_list, f, indent=4)
        else:
            r = None
            for i in pre_info:
                if i["ID"] == self.id:
                    r = i
                    pre_info.remove(i)
                    break

            if r is None:
                main_dicto = dict()
                main_dicto["ID"] = self.id
                main_dicto["Name"] = self.name
                main_dicto["RecordList"] = list()
                main_dicto["RecordList"].append(self.dicto)
                pre_info.append(main_dicto)
                with open("record.json", "w") as f:
                    json.dump(pre_info, f, indent=4)

            else:
                r["RecordList"].append(self.dicto)
                pre_info.append(r)
                with open("record.json", "w") as f:
                    json.dump(pre_info, f, indent=4)



