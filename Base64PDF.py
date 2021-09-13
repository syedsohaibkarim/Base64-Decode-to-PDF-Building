# Required Packages
import os
import base64

#Base64 Data.
pdf = """#Base64 String#"""

# Decode - base64 
pdf = base64.b64decode(pdf)

# Buiding PDF
with open(os.path.expanduser('#filename#.pdf'), 'wb') as pdfout:
    pdfout.write(pdf)
    
# Print
print('Success')