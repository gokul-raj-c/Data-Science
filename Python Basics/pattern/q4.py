"""
Print the pattern
        *
      * *
    * * *
  * * * *
* * * * *
"""

i=1
while i<=5:
    print("  "*(5-i) + "* "*i)
    i=i+1