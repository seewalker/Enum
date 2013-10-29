                                    Welcome
One of the great features of the c programming language is the 'enum'
construct.Python versions prior to 3.4 lack this feature. If you want to
integrate enums into older code or you prefer this syntax to python's, this is
the module for you.  Note: This program can generated enums of size ten
thousand or fewer. For the technical explanation of this limitation see the
'Design Decisions' section.

                                  Installation

sudo python setup.py install

                                     Usage

Abstract Usage: 
   Import the Enum module in your prefered way
   var0, var1, ...var(n-1) = Enum.enum_gen(n)
Concrete Example of Usage:
   import Enum
   Sun, Mon, Tue, Wed, Thur, Fri, Sat = Enum.enum_gen(7)


                                Design Decisions

The c function in the Python API that builds the python tuple is
Py_BuildValue. It takes a format string describing the size of the 
tuple to return. This can be dynamically generated based on the
user's inputed enum size; this is what I did. The other arguments
to Py_BuildValue, however, must be sequential natural numbers, but
the program does not know how many numbers at compile time. Because
the compiled nature of the c programming language makes an 'eval'-like
function impossible, I handle this dynamic limit by simply providing
ten thousand natural number arguments. This means that enums greater than
that in size cannot be generated with this program unless one edits the 
source code to include a greater number of arguments to Py_BuildValue.
