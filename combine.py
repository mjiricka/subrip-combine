#!/usr/bin/env python3
"""
Very simple script that combines two SubRip subtitles.

Prerequisities:
   sudo pip install pysrt

"""

import sys
import pysrt


def combine(time_subs_path, text_subs_path, output_path):
    time_subs = pysrt.open(time_subs_path)
    text_subs = pysrt.open(text_subs_path)

    if len(time_subs) != len(text_subs):
        raise Exception('Cannot combine! Each file has different number of subtitles.')

    subs_len = len(time_subs)

    # The easiest way: rewrite text in one of loaded subtitle objects.
    for i in range(0, subs_len):
        time_subs[i].text = text_subs[i].text

    # Write with encoding of the text file.
    time_subs.save(output_path, text_subs.encoding)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            ('Usage: {0} <subtitles_with_timing> <subtitles_with_text> ' +
             '<output_subtitles>').format(sys.argv[0]))
        sys.exit(1)

    try:
        combine(sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as exc:
        print(str(exc))
        sys.exit(2)


# EOF
