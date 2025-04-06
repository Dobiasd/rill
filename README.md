![logo](https://github.com/Dobiasd/rill/raw/master/rill.jpg)

[![CI](https://github.com/Dobiasd/rill/workflows/ci/badge.svg)](https://github.com/Dobiasd/rill/actions)
[![(License MIT 1.0)](https://img.shields.io/badge/license-MIT%201.0-blue.svg)][license]

[license]: LICENSE


rill
====

**DEPRECATED**

**Python library providing simple text-stream processing functionality**


Table of contents
-----------------
  * [Introduction](#introduction)
  * [Examples](#examples)
  * [Requirements and Installation](#requirements-and-installation)
  * [API docs](#api-docs)


Introduction
------------

With `grep`, `sed`, `wc`, `cat`, `sort`, `uniq`, `head`, `tail`, `tr`, etc., we have a set of extremely powerful and time-proven tools for pipeline-processing text on the command line ubiquitously available.

But some tasks that start out as a simple one-liner, over time, can mutate into a mess ("write-only code"), especially if the requirements grow or some edge cases need special handling, such that having things in a "normal" programming language would be more convenient.

This is where `rill` comes into play. It provides simple text-stream processing functionality in Python. And while it is much less powerful (features *and* throughput, hence the name "rill") compared to the good old Unix tools, there is the advantage that one-liners written using `rill` can easily be expanded to longer Python scripts.

Also, in case one is already familiar with Python, but not (yet) with the Unix tools, it can be a somewhat more convenient entry point to text-stream processing.


Examples
--------

Assuming you have an `example_input.txt` like so:

```
Hello, fellow dev,
this test file helps to show
the thrilling things
you can do with rill. ;)
```

You can do stuff like the following:

```bash
# Drop all lines not containing "rill", and replace "rill" with "RILL".
python3 -c 'import rill; rill.inp().grep("rill").replace("rill", "RILL").show()' example_input.txt
# Same as: grep rill example_input.txt | sed 's/rill/RILL/g'
```

Output:
```
the thRILLing things
you can do with RILL. ;)
```

```bash
# Count the number of lines containing an "e".
python3 -c 'import rill; rill.inp().grep("e").line_count().show()' example_input.txt
# Same as: cat example_input.txt | grep e | wc -l
```

Output:
```
3
```

You can also use it as part of normal Unix pipelines, e.g.:

```bash
cat example_input.txt | grep 'rill' | python3 -c 'import rill; rill.inp().replace("rill", "RILL").show()'
```

Output:
```
the thRILLing things
you can do with RILL. ;)
```

And extend your script infinitely, e.g.:

```bash
cat example_input.txt | python3 -c 'import rill
import codecs
def caesar(text):
    return str(codecs.encode(text, "rot_13"))
rill.inp().grep("rill").map_lines(caesar).show()'
```

Output:
```
gur guevyyvat guvatf
lbh pna qb jvgu evyy. ;)
```

At this point, it probably makes sense to move your code into a file and use it like a normal Python script.

```bash
python3 my_script.py example_input.txt
```

Requirements and Installation
-----------------------------

```bash
pip install rill
```

Or, if you like to use the latest version from this repository:
```bash
git clone https://github.com/Dobiasd/rill
cd rill
pip install .
```

API docs
--------

When writing rill one-liners on the command line,
you might not have IDE-like auto-completion,
thus [full list of available functions](docs/rill.md)
might be helpful.

License
-------
Distributed under the MIT License.
(See accompanying file [`LICENSE`](https://github.com/Dobiasd/rill/blob/master/LICENSE) or at
[https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT))
