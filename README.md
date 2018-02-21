# subrip-combine
Very simple script that combines two SubRip subtitles: it takes time from one file and subtitles text from other.


## When it is useful

I was doing a translation of subtitles. A new version of the original subtitles came out with updated timing. So I wanted to update the timing also in my translated subtitles. Because my subtitle editor cannot do that, I wrote this little script.


## Usage

All the hard work is done by [pysrt](https://pypi.python.org/pypi/pysrt) module. So it needed to be installed:

     sudo pip install pysrt

Then you can simply run:

     python merge.py subtitles_with_timing.srt subtitles_with_text.srt output.srt
     
