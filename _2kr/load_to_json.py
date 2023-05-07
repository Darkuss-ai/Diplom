# -*- coding: windows-1251 -*-

from algorithms import convert, rev, dop, shift, summator
import json
import shutil


def check_overflow(str1, str2):
    if ((str1 == 'OVERFLOW' or str1 == 'ПЕРЕПОЛНЕНИЕ') and (str2 == 'OVERFLOW' or str2 == 'ПЕРЕПОЛНЕНИЕ')) or \
            str1 == str2:
        return True
    else:
        return False


def _2KR_load_to_json(ret_json, in_json):
    with open(ret_json) as f1:
        templates = json.load(f1)
    with open(in_json) as f2:
        templatesIN = json.load(f2)

    f1.close()
    f2.close()

    # While there is no variant generation, I write the values for A and B in the JSON file myself.
    # Then we'll just fill them in and that's it.

    # var_numbers = generate_var()  ######## returns dict {"A": value, "B": value} (for example) ########
    # templates["A_var"] = var_numbers["A"]
    # templates["B_var"] = var_numbers["B"]

    templates["A_var"] = templatesIN["A_var"]
    templates["B_var"] = templatesIN["B_var"]
    templates["fio"] = templatesIN["fio"]
    templates["group"] = templatesIN["group"]

    q = templates["A_var"]
    w = templates["B_var"]

    templates["A"][0]["str"] = convert(q)
    templatesIN['A'][0]['str'] = True if templatesIN['A'][0]['str'] == templates["A"][0]["str"] else False
    templates["A"][0]["rev"] = rev(q)
    templatesIN['A'][0]['rev'] = True if templatesIN['A'][0]['rev'] == templates["A"][0]["rev"] else False
    templates["A"][0]["dop"] = dop(q)
    templatesIN['A'][0]['dop'] = True if templatesIN['A'][0]['dop'] == templates["A"][0]["dop"] else False
    templates["A"][0]["int"] = convert(convert(q))

    templates["B"][0]["str"] = convert(w)
    templatesIN['B'][0]['str'] = True if templatesIN['B'][0]['str'] == templates["B"][0]["str"] else False
    templates["B"][0]["rev"] = rev(w)
    templatesIN['B'][0]['rev'] = True if templatesIN['B'][0]['rev'] == templates["B"][0]["rev"] else False
    templates["B"][0]["dop"] = dop(w)
    templatesIN['B'][0]['dop'] = True if templatesIN['B'][0]['dop'] == templates["B"][0]["dop"] else False
    templates["B"][0]["int"] = convert(convert(w))

    templates["-A"][0]["str"] = convert(-q)
    templatesIN['-A'][0]['str'] = True if templatesIN['-A'][0]['str'] == templates["-A"][0]["str"] else False
    templates["-A"][0]["rev"] = rev(-q)
    templatesIN['-A'][0]['rev'] = True if templatesIN['-A'][0]['rev'] == templates["-A"][0]["rev"] else False
    templates["-A"][0]["dop"] = dop(-q)
    templatesIN['-A'][0]['dop'] = True if templatesIN['-A'][0]['dop'] == templates["-A"][0]["dop"] else False
    templates["-A"][0]["int"] = convert(convert(-q))

    templates["-B"][0]["str"] = convert(-w)
    templatesIN['-B'][0]['str'] = True if templatesIN['-B'][0]['str'] == templates["-B"][0]["str"] else False
    templates["-B"][0]["rev"] = rev(-w)
    templatesIN['-B'][0]['rev'] = True if templatesIN['-B'][0]['rev'] == templates["-B"][0]["rev"] else False
    templates["-B"][0]["dop"] = dop(-w)
    templatesIN['-B'][0]['dop'] = True if templatesIN['-B'][0]['dop'] == templates["-B"][0]["dop"] else False
    templates["-B"][0]["int"] = convert(convert(-w))

    templates["A*2^-2"][0]["str"] = shift(convert(q), "str", -2)
    templatesIN['A*2^-2'][0]['str'] = True if check_overflow(templatesIN['A*2^-2'][0]['str'], templates["A*2^-2"][0]["str"]) else False
    templates["A*2^-2"][0]["rev"] = shift(rev(q), "str", -2)
    templatesIN['A*2^-2'][0]['rev'] = True if check_overflow(templatesIN['A*2^-2'][0]['rev'], templates["A*2^-2"][0]["rev"]) else False
    templates["A*2^-2"][0]["dop"] = shift(dop(q), "str", -2)
    templatesIN['A*2^-2'][0]['dop'] = True if check_overflow(templatesIN['A*2^-2'][0]['dop'], templates["A*2^-2"][0]["dop"]) else False
    templates["A*2^-2"][0]["int"] = convert(shift(convert(q), "str", -2))

    templates["A*2^-3"][0]["str"] = shift(convert(q), "str", -3)
    templatesIN['A*2^-3'][0]['str'] = True if check_overflow(templatesIN['A*2^-3'][0]['str'], templates["A*2^-3"][0]["str"]) else False
    templates["A*2^-3"][0]["rev"] = shift(rev(q), "str", -3)
    templatesIN['A*2^-3'][0]['rev'] = True if check_overflow(templatesIN['A*2^-3'][0]['rev'], templates["A*2^-3"][0]["rev"]) else False
    templates["A*2^-3"][0]["dop"] = shift(dop(q), "str", -3)
    templatesIN['A*2^-3'][0]['dop'] = True if check_overflow(templatesIN['A*2^-3'][0]['dop'], templates["A*2^-3"][0]["dop"]) else False
    templates["A*2^-3"][0]["int"] = convert(shift(convert(q), "str", -3))

    templates["A*2^+3"][0]["str"] = shift(convert(q), "str", 3)
    templatesIN['A*2^+3'][0]['str'] = True if check_overflow(templatesIN['A*2^+3'][0]['str'], templates["A*2^+3"][0]["str"]) else False
    templates["A*2^+3"][0]["rev"] = shift(rev(q), "str", 3)
    templatesIN['A*2^+3'][0]['rev'] = True if check_overflow(templatesIN['A*2^+3'][0]['rev'], templates["A*2^+3"][0]["rev"]) else False
    templates["A*2^+3"][0]["dop"] = shift(dop(q), "str", 3)
    templatesIN['A*2^+3'][0]['dop'] = True if check_overflow(templatesIN['A*2^+3'][0]['dop'], templates["A*2^+3"][0]["dop"]) else False
    templates["A*2^+3"][0]["int"] = convert(shift(convert(q), "str", 3))

    templates["A*2^+4"][0]["str"] = shift(convert(q), "str", 4)
    templatesIN['A*2^+4'][0]['str'] = True if check_overflow(templatesIN['A*2^+4'][0]['str'], templates["A*2^+4"][0]["str"]) else False
    templates["A*2^+4"][0]["rev"] = shift(rev(q), "str", 4)
    templatesIN['A*2^+4'][0]['rev'] = True if check_overflow(templatesIN['A*2^+4'][0]['rev'], templates["A*2^+4"][0]["rev"]) else False
    templates["A*2^+4"][0]["dop"] = shift(dop(q), "str", 4)
    templatesIN['A*2^+4'][0]['dop'] = True if check_overflow(templatesIN['A*2^+4'][0]['dop'], templates["A*2^+4"][0]["dop"]) else False
    templates["A*2^+4"][0]["int"] = convert(shift(convert(q), "str", 4))

    templates["B*2^-2"][0]["str"] = shift(convert(w), "str", -2)
    templatesIN['B*2^-2'][0]['str'] = True if check_overflow(templatesIN['B*2^-2'][0]['str'], templates["B*2^-2"][0]["str"]) else False
    templates["B*2^-2"][0]["rev"] = shift(rev(w), "str", -2)
    templatesIN['B*2^-2'][0]['rev'] = True if check_overflow(templatesIN['B*2^-2'][0]['rev'], templates["B*2^-2"][0]["rev"]) else False
    templates["B*2^-2"][0]["dop"] = shift(dop(w), "str", -2)
    templatesIN['B*2^-2'][0]['dop'] = True if check_overflow(templatesIN['B*2^-2'][0]['dop'], templates["B*2^-2"][0]["dop"]) else False
    templates["B*2^-2"][0]["int"] = convert(shift(convert(w), "str", -2))

    templates["B*2^-3"][0]["str"] = shift(convert(w), "str", -3)
    templatesIN['B*2^-3'][0]['str'] = True if check_overflow(templatesIN['B*2^-3'][0]['str'], templates["B*2^-3"][0]["str"]) else False
    templates["B*2^-3"][0]["rev"] = shift(rev(w), "str", -3)
    templatesIN['B*2^-3'][0]['rev'] = True if check_overflow(templatesIN['B*2^-3'][0]['rev'], templates["B*2^-3"][0]["rev"]) else False
    templates["B*2^-3"][0]["dop"] = shift(dop(w), "str", -3)
    templatesIN['B*2^-3'][0]['dop'] = True if check_overflow(templatesIN['B*2^-3'][0]['dop'], templates["B*2^-3"][0]["dop"]) else False
    templates["B*2^-3"][0]["int"] = convert(shift(convert(w), "str", -3))

    templates["B*2^+3"][0]["str"] = shift(convert(w), "str", 3)
    templatesIN['B*2^+3'][0]['str'] = True if check_overflow(templatesIN['B*2^+3'][0]['str'], templates["B*2^+3"][0]["str"]) else False
    templates["B*2^+3"][0]["rev"] = shift(rev(w), "str", 3)
    templatesIN['B*2^+3'][0]['rev'] = True if check_overflow(templatesIN['B*2^+3'][0]['rev'], templates["B*2^+3"][0]["rev"]) else False
    templates["B*2^+3"][0]["dop"] = shift(dop(w), "str", 3)
    templatesIN['B*2^+3'][0]['dop'] = True if check_overflow(templatesIN['B*2^+3'][0]['dop'], templates["B*2^+3"][0]["dop"]) else False
    templates["B*2^+3"][0]["int"] = convert(shift(convert(w), "str", 3))

    templates["B*2^+4"][0]["str"] = shift(convert(w), "str", 4)
    templatesIN['B*2^+4'][0]['str'] = True if check_overflow(templatesIN['B*2^+4'][0]['str'], templates["B*2^+4"][0]["str"]) else False
    templates["B*2^+4"][0]["rev"] = shift(rev(w), "str", 4)
    templatesIN['B*2^+4'][0]['rev'] = True if check_overflow(templatesIN['B*2^+4'][0]['rev'], templates["B*2^+4"][0]["rev"]) else False
    templates["B*2^+4"][0]["dop"] = shift(dop(w), "str", 4)
    templatesIN['B*2^+4'][0]['dop'] = True if check_overflow(templatesIN['B*2^+4'][0]['dop'], templates["B*2^+4"][0]["dop"]) else False
    templates["B*2^+4"][0]["int"] = convert(shift(convert(w), "str", 4))

    A_B = summator(q, w)
    templates["A+B"][0]["str"] = convert(A_B)
    templatesIN['A+B'][0]['str'] = True if templatesIN['A+B'][0]['str'] == templates["A+B"][0]["str"] else False
    templates["A+B"][0]["rev"] = rev(A_B)
    templatesIN['A+B'][0]['rev'] = True if templatesIN['A+B'][0]['rev'] == templates["A+B"][0]["rev"] else False
    templates["A+B"][0]["dop"] = dop(A_B)
    templatesIN['A+B'][0]['dop'] = True if templatesIN['A+B'][0]['dop'] == templates["A+B"][0]["dop"] else False
    templates["A+B"][0]["int"] = A_B

    minA_B = summator(-q, w)
    templates["-A+B"][0]["str"] = convert(minA_B)
    templatesIN['-A+B'][0]['str'] = True if templatesIN['-A+B'][0]['str'] == templates["-A+B"][0]["str"] else False
    templates["-A+B"][0]["rev"] = rev(minA_B)
    templatesIN['-A+B'][0]['rev'] = True if templatesIN['-A+B'][0]['rev'] == templates["-A+B"][0]["rev"] else False
    templates["-A+B"][0]["dop"] = dop(minA_B)
    templatesIN['-A+B'][0]['dop'] = True if templatesIN['-A+B'][0]['dop'] == templates["-A+B"][0]["dop"] else False
    templates["-A+B"][0]["int"] = minA_B

    A_minB = summator(q, -w)
    templates["A-B"][0]["str"] = convert(A_minB)
    templatesIN['A-B'][0]['str'] = True if templatesIN['A-B'][0]['str'] == templates["A-B"][0]["str"] else False
    templates["A-B"][0]["rev"] = rev(A_minB)
    templatesIN['A-B'][0]['rev'] = True if templatesIN['A-B'][0]['rev'] == templates["A-B"][0]["rev"] else False
    templates["A-B"][0]["dop"] = dop(A_minB)
    templatesIN['A-B'][0]['dop'] = True if templatesIN['A-B'][0]['dop'] == templates["A-B"][0]["dop"] else False
    templates["A-B"][0]["int"] = A_minB

    minA_minB = summator(-q, -w)
    templates["-A-B"][0]["str"] = convert(minA_minB)
    templatesIN['-A-B'][0]['str'] = True if templatesIN['-A-B'][0]['str'] == templates["-A-B"][0]["str"] else False
    templates["-A-B"][0]["rev"] = rev(minA_minB)
    templatesIN['-A-B'][0]['rev'] = True if templatesIN['-A-B'][0]['rev'] == templates["-A-B"][0]["rev"] else False
    templates["-A-B"][0]["dop"] = dop(minA_minB)
    templatesIN['-A-B'][0]['dop'] = True if templatesIN['-A-B'][0]['dop'] == templates["-A-B"][0]["dop"] else False
    templates["-A-B"][0]["int"] = minA_minB

    with open(ret_json, 'w') as output:
        json.dump(templates, output)
    f1.close()
    return [templates, templatesIN]


def clear_json(file):
    shutil.copy2("_2KR/kr2_json_proto.json", file)  # copy empty json (proto) to our json with results (file)
    return file
