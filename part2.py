"""
Define a function diamond that takes a single integer input size. The function then prints (doesn't have to return) a hollow diamond made of asterisks.

Hint: <string>.center(2*size - 1) may be helpful in your code (for center aligning)

Examples of what should appear:

diamond(4) -->
   *   
  * *  
 *   * 
*     *
 *   * 
  * *  
   * 

diamond(7) -->
      *      
     * *     
    *   *    
   *     *   
  *       *  
 *         * 
*           *
 *         * 
  *       *  
   *     *   
    *   *    
     * *     
      * 
"""


def diamond(size):
  if size >= 1:
    print("*".center(2 * size - 1))
  for i in range(2, size + 1):
    row = "*" + " " * (i * 2 - 3) + "*"
    print(row.center(2 * size - 1))
  for i in range(size - 1, 1, -1):
    row = "*" + " " * (i * 2 - 3) + "*"
    print(row.center(2 * size - 1))
  if size >= 2:
    print("*".center(2 * size - 1))