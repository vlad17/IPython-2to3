import json

code_cell_v4 = json.loads(r"""
        {
         "cell_type": "code",
         "metadata": {
          "collapsed": false
         },
         "source": [
          "print \"line1\"\n",
          "print \"line2\"\n"
         ]
        }
        """)

code_cell_v3 = json.loads(r"""
        {
         "cell_type": "code",
         "execution_count": null,
         "metadata": {},
         "outputs": [],
         "language": "python",
         "input": [
          "print \"line1\"\n",
          "print \"line2\"\n"
         ]
        }
        """)

str_notebook_v4= r"""
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "print \"test\"\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2.0
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
        """

notebook_v4 = json.loads(str_notebook_v4)


str_notebook_v3 = r"""
{
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "execution_count": null,
     "metadata": {},
     "outputs": [],
     "input": [
       "print \"test1\"\n"
     ],
     "language": "python"
    }
   ]
  },
  {
   "cells": [
    {
     "cell_type": "code",
     "execution_count": null,
     "metadata": {},
     "outputs": [],
     "input": [
       "print \"test2\"\n"
     ],
     "language": "python"
    }
   ]
  }
 ],
 "metadata": {
  "name": "notebook name"
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
            """

notebook_v3 = json.loads(str_notebook_v3)
