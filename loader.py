
import sys

STAGE_SEPARATOR = "--"
INFO_SEPARATOR = ""


def load_story(fn):
    with open(fn) as file:
        next_type = ""
        dct = {}
        cur_name = ""
        cur_txt = ""
        cur_opts = []
        cur_outs = []
        cur_sec_ln = 0
        for i, ln in enumerate(file.readlines()):
            ln = ln.replace("\n", "")
            if ln.startswith("#"):
                continue
            if ln == STAGE_SEPARATOR:
                if next_type == "outcomes" or next_type == "options" or next_type == "txt":
                    if len(cur_outs) != len(cur_opts):
                        print(
                            f"Line {cur_sec_ln+1}, Section '{cur_name}': Number of Outcomes and Options must be equal!")
                        sys.exit()
                    dct[cur_name] = {"Text": cur_txt, "Options": cur_opts,
                                     "Outcomes": cur_outs, "IsEnd": len(cur_opts) == 0}
                cur_txt = ""
                cur_outs, cur_opts = [], []
                cur_sec_ln = i
                next_type = "name"
                continue
            elif ln == INFO_SEPARATOR:
                if next_type == "name":
                    next_type = "txt"
                elif next_type == "txt":
                    next_type = "options"
                elif next_type == "options":
                    next_type = "outcomes"
                continue
            if next_type == "name":
                cur_name = ln
                if ln in dct.keys():
                    print(
                        f"Line {i+1}: Name '{ln}' already used. Please use a different one.")
                    sys.exit()
            elif next_type == "txt":
                cur_txt += f"{ln}\n"
            elif next_type == "options":
                cur_opts.append(ln)
            elif next_type == "outcomes":
                cur_outs.append(ln)
        if "start" not in dct.keys():
            print("You must create a stage with the name 'start' for this to work!")
            sys.exit()
        return dct
