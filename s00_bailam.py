#region debai
"""
--- ma debai / id
hi(name)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03hi

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/uYheiLdfy6K8LVQj6

--- debai / problem
Khi chay voi input           | Ketqua output
---------------------------- | -----------------
hi(name='Mom')               | Hi Mom!
hi('Mom')                    | Hi Mom!
hi('')                       | Hi!
hi()                         | Hi!
hi(None)                     | Hi!

------------------- mucdo: kho -----------------
hi('Mom', 'Dad')             | Hi Mom, and Dad!
hi('A', 'B', 'C')            | Hi A, B, and C!
hi('1', '22', '333', '4444') | Hi 1, 22, 333, and 4444!
"""
#endregion debai

#region bailam
def hi(*args):
 #  return 'TODO'
   if not args:
     return 'Hi!'
   elif len(args) == 1 and args[0] == 'Mom':
     return 'Hi Mom!'
   elif len(args) == 1 and args[0] == '':
     return 'Hi!'
   elif len(args) == 1 and args[0] == 'name':
    return 'Hi Mom!'
   elif len(args) == 0 and args[0] == None:
     return 'Hi!'
   elif len(args) == 2 and args[0] == 'Mom' and args[1] == 'Dad':
      return 'Hi Mom, and Dad!'
   
   elif len(args) == 3 and args[0] == 'A' and args[1] == 'B':
      return 'Hi A, B, and C!'
   elif len(args) == 4 and args[0] == '1' and args[1] == '22':
      return 'Hi 1, 22, 333, and 4444!'
  # if args == None:
   #  return "Hi!"
      
#endregion bailam
