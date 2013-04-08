#!/usr/bin/python3

import os
import re

# note of interest about why big5-hkscs is better
# http://lists.w3.org/Archives/Public/public-html-ig-zh/2012Apr/0046

def is_simplified(char):
    result = False
    try:
        char.encode("gb2312")
        result = True
    except:
        try:
            char.encode("big5hkscs")
        except: # not in big5
            try:
                char.encode("gbk")
                result = True
            except:
                pass
    return result

def is_traditional(char):
    result = False
    try:
        char.encode("big5hkscs")
        result = True
    except:
        pass
    return result

# this is based on a particular intrepretation of big charset:
# if the character exists in the target encoding, it is "recognized"
# and we include it in the table. otherwise if it exists in another
# known chinese encoding, we still allow it to be included as long as
# the input sequence does not conflict with any in our target
# encoding. if it does not exist in any known chinese encoding, but
# has a unique input sequence, we include it anyway since it does not
# conflict with anything. however, for characters not in the target
# encoding we only include one result for each input sequence, whereas
# we include all results that exist in the target encoding.
def previewtable(tablename, return_hans):
    f = open(os.path.join("tables", tablename + ".txt"))

    recognized_sequences = {}
    other_sequences = {}
    maybe_sequences = {}

    if return_hans:
        test_recognized = is_simplified
        test_other = is_traditional
    else:
        test_recognized = is_traditional
        test_other = is_simplified

    started = False
    for line in f:
        if started:
            if line.startswith("#"):
                continue

            if line.strip() == "END_TABLE":
                started = False
                continue

            parts = line.split()
            sequence = parts[0]
            test_char = parts[1]

            passed = test_recognized(test_char)
            if passed:
                # ok to overwrite since we just care if it exists
                recognized_sequences[sequence] = test_char
            elif sequence not in recognized_sequences:
                passed_other = test_other(test_char)
                if passed_other:
                    # overwriting behavior means we'll get last match
                    other_sequences[sequence] = test_char
                elif sequence not in other_sequences:
                    maybe_sequences[sequence] = test_char

        else:
            if line.strip() == "BEGIN_TABLE":
                started = True

    unique_sequences = {}
    for (sequence, char) in other_sequences.items():
        if sequence not in recognized_sequences:
            unique_sequences[sequence] = char

    for (sequence, char) in maybe_sequences.items():
        if sequence not in recognized_sequences \
                and sequence not in other_sequences:
            unique_sequences[sequence] = char

    return unique_sequences

def splittable(tablename, return_hans, big_charset):
    if big_charset:
        unique_sequences = previewtable(tablename, return_hans)
    else:
        unique_sequences = {}

    f = open(os.path.join("tables", tablename + ".txt"))
    if return_hans:
        suffix = "_hans"
    else:
        suffix = "_hant"
    outf = open(os.path.join("tables", tablename + suffix + ".txt"), "w")

    started = False
    for line in f:
        if started:
            if line.startswith("#"):
                outf.write(line)
                continue

            if line.strip() == "END_TABLE":
                outf.write(line)
                started = False
                continue

            parts = line.split()
            sequence = parts[0]
            test_char = parts[1]

            if return_hans:
                passed = is_simplified(test_char)
            else:
                passed = is_traditional(test_char)

            if passed or \
                    (sequence in unique_sequences \
                         and test_char == unique_sequences[sequence]):
                outf.write(line)

        else:
            if line.startswith("NAME"):
                pat = re.compile("^NAME\s*=\s*(.+)")
                match = pat.match(line)
                if match:
                    old_name = match.group(1)
                    new_name = old_name.replace(" ", "") + suffix
                    # tabcreatedb.py expects there to be no spaces in the
                    # table name
                    line = line.replace(old_name, new_name)
            elif line.startswith("ICON"):
                pat = re.compile("^ICON\s*=\s*(.+).svg")
                match = pat.match(line)
                if match:
                    old_name = match.group(1)
                    new_name = old_name + suffix
                    line = line.replace(old_name, new_name)

            outf.write(line)
            if line.strip() == "BEGIN_TABLE":
                started = True

    f.close()
    outf.close()

splittable("cangjie3", True, False)
splittable("cangjie3", False, False)
splittable("cangjie5", True, False)
splittable("cangjie5", False, False)
