import re

_TESTS = [
    "//REL/RELIDO",
    "TS//SI-G/TK//RS/OC/NF",
    "TS//SI-ABC-DEF//OC/NF",
    "TS//SI-G ABCD EFGH-XYZ//OC/NF",
    "TS//ANB/SI/TK/XNB//NF",
    "TS//SAR-BP-123/CA-XYZ YYY//NF",
    "TS//RD-CNWDI//NF",
    "S//FRD-SIGMA 14 18//REL",
    "//CTS//BOHEMIA",
    "//DEU S//NF",
    "//NS//ATOMAL//OC",
    "//JOINT S//REL",
    "TS//FGI DEU GBR//REL TO USA, DEU, GBR",
    "//FGI S//NF",
    "S//NF",
    "S//NF/PR",
    "U//SSI",
]

_PATTERN = "^(U?|C|(S|TS)?(\/\/(((\w|\-)+)(\s(\w|\-)+)*)((\/(\w|\-)+)(\s(\w|\-)+)*)*)?)\/\/((((\w|\-)+)|(REL( TO ((\w|\-)+)(,\s?((\w|\-)+))*)?))((\/((\w|\-)+)|(REL( TO ((\w|\-)+)(,(\w|\-)+)*)?))*))$"

def main():
    prog = re.compile(_PATTERN)
    for s in _TESTS:
        result = prog.match(s)
        print(s + " " + str(result))

if __name__ == '__main__':
    main()


