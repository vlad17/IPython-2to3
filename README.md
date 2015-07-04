# IPython Notebook 2-to-3

Converts IPython version 2 notebooks to IPython version 3.

I didn't find any tool online to convert ipython2 to ipython3 notebooks automatically, and it seemed simple enough, so I made my own.

I'm sure there are a lot of corner cases that are missed by the current script, but it should do the job for the vast majority of IPython notebooks. I suppose it would save people the pain of converting IPy notebooks manually or hacking up their own version of this.

### Implementation

Converts all code sections by invoking 2to3. Handles any IPython magic statements by saving them over the conversion.

### Usage

`ipy2to3 fromfile.ipynb tofile.ipynb` converts ipython2 file `fromfile.ipynb` to an ipython3 file `tofile.ipynb`. Flags to come.
