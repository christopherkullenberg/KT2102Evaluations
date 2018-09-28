import re

counter = 0
outfile = open('enumeratedforms.md', 'w')

header = '''<!--
pandoc -V fontsize=12pt -V papersize:"a4paper" -V geometry:geometry:margin=1in
-->

![logga GU](https://www.gu.se/digitalAssets/702/702071_logtotyp_1.gif){ width=25% }\\\
'''

for number in range(0,30):
    counter += 1
    print(header)
    print("Anonymt löpnummer: " + str(counter))
    # print(formbody)
    # gör om till fil som skriver
    outfile.close()


