from algorithms import convert, rev, dop, shift, summator
import json
import shutil


def load_to_json(file):
    with open(file) as f:
        templates = json.load(f)

    # While there is no variant generation, I write the values for A and B in the JSON file myself.
    # Then we'll just fill them in and that's it.

    # var_numbers = generate_var()  ######## returns dict {"A": value, "B": value} (for example) ########
    # templates["A_var"] = var_numbers["A"]
    # templates["B_var"] = var_numbers["B"]

    q = templates["A_var"]
    w = templates["B_var"]

    templates["A"][0]["str"] = convert(q)
    templates["A"][0]["rev"] = rev(q)
    templates["A"][0]["dop"] = dop(q)
    templates["A"][0]["int"] = convert(convert(q))

    templates["B"][0]["str"] = convert(w)
    templates["B"][0]["rev"] = rev(w)
    templates["B"][0]["dop"] = dop(w)
    templates["B"][0]["int"] = convert(convert(w))

    templates["-A"][0]["str"] = convert(-q)
    templates["-A"][0]["rev"] = rev(-q)
    templates["-A"][0]["dop"] = dop(-q)
    templates["-A"][0]["int"] = convert(convert(-q))

    templates["-B"][0]["str"] = convert(-w)
    templates["-B"][0]["rev"] = rev(-w)
    templates["-B"][0]["dop"] = dop(-w)
    templates["-B"][0]["int"] = convert(convert(-w))

    templates["A*2^-2"][0]["str"] = shift(convert(q), "str", -2)
    templates["A*2^-2"][0]["rev"] = shift(rev(q), "str", -2)
    templates["A*2^-2"][0]["dop"] = shift(dop(q), "str", -2)
    templates["A*2^-2"][0]["int"] = convert(shift(convert(q), "str", -2))

    templates["A*2^-3"][0]["str"] = shift(convert(q), "str", -3)
    templates["A*2^-3"][0]["rev"] = shift(rev(q), "str", -3)
    templates["A*2^-3"][0]["dop"] = shift(dop(q), "str", -3)
    templates["A*2^-3"][0]["int"] = convert(shift(convert(q), "str", -3))

    templates["A*2^+3"][0]["str"] = shift(convert(q), "str", 3)
    templates["A*2^+3"][0]["rev"] = shift(rev(q), "str", 3)
    templates["A*2^+3"][0]["dop"] = shift(dop(q), "str", 3)
    templates["A*2^+3"][0]["int"] = convert(shift(convert(q), "str", 3))

    templates["A*2^+4"][0]["str"] = shift(convert(q), "str", 4)
    templates["A*2^+4"][0]["rev"] = shift(rev(q), "str", 4)
    templates["A*2^+4"][0]["dop"] = shift(dop(q), "str", 4)
    templates["A*2^+4"][0]["int"] = convert(shift(convert(q), "str", 4))

    templates["B*2^-2"][0]["str"] = shift(convert(w), "str", -2)
    templates["B*2^-2"][0]["rev"] = shift(rev(w), "str", -2)
    templates["B*2^-2"][0]["dop"] = shift(dop(w), "str", -2)
    templates["B*2^-2"][0]["int"] = convert(shift(convert(w), "str", -2))

    templates["B*2^-3"][0]["str"] = shift(convert(w), "str", -3)
    templates["B*2^-3"][0]["rev"] = shift(rev(w), "str", -3)
    templates["B*2^-3"][0]["dop"] = shift(dop(w), "str", -3)
    templates["B*2^-3"][0]["int"] = convert(shift(convert(w), "str", -3))

    templates["B*2^+3"][0]["str"] = shift(convert(w), "str", 3)
    templates["B*2^+3"][0]["rev"] = shift(rev(w), "str", 3)
    templates["B*2^+3"][0]["dop"] = shift(dop(w), "str", 3)
    templates["B*2^+3"][0]["int"] = convert(shift(convert(w), "str", 3))

    templates["B*2^+4"][0]["str"] = shift(convert(w), "str", 4)
    templates["B*2^+4"][0]["rev"] = shift(rev(w), "str", 4)
    templates["B*2^+4"][0]["dop"] = shift(dop(w), "str", 4)
    templates["B*2^+4"][0]["int"] = convert(shift(convert(w), "str", 4))

    A_B = summator(q, w)
    templates["A+B"][0]["str"] = convert(A_B)
    templates["A+B"][0]["rev"] = rev(A_B)
    templates["A+B"][0]["dop"] = dop(A_B)
    templates["A+B"][0]["int"] = A_B

    minA_B = summator(-q, w)
    templates["-A+B"][0]["str"] = convert(minA_B)
    templates["-A+B"][0]["rev"] = rev(minA_B)
    templates["-A+B"][0]["dop"] = dop(minA_B)
    templates["-A+B"][0]["int"] = minA_B

    A_minB = summator(q, -w)
    templates["A-B"][0]["str"] = convert(A_minB)
    templates["A-B"][0]["rev"] = rev(A_minB)
    templates["A-B"][0]["dop"] = dop(A_minB)
    templates["A-B"][0]["int"] = A_minB

    minA_minB = summator(-q, -w)
    templates["-A-B"][0]["str"] = convert(minA_minB)
    templates["-A-B"][0]["rev"] = rev(minA_minB)
    templates["-A-B"][0]["dop"] = dop(minA_minB)
    templates["-A-B"][0]["int"] = minA_minB

    with open(file, 'w') as output:
        json.dump(templates, output)
    return templates


def clear_json(file):
    shutil.copy2("kr2_json_proto.json", file)  # copy empty json (proto) to our json with results (file)
    return file
