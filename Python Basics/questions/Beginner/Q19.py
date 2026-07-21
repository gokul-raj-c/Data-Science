#Print a right-aligned triangle of stars (print spaces before the stars):        
#         *      
#       * *    
#     * * *  
#   * * * * 
# * * * * *

i=1
while i<=5:
    print("  "*(5-i) + "* "*i)
    i=i+1

