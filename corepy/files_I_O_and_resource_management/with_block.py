# every file opened need to be close
# f.open()
# work with file
# f.close()
# if you don't close, you can lose data!
# We want a mechanism to pair open() and close() automatically.

# With - Blocks:
# Control flow structure for managing resources.
# Can be used with any objects - such as files - which support the context-manager protocol
# we are using it in sequence_reader.py and recaman_sequence.py

# SYNTAX:
# with EXPR as VAR:
#     BLOCK