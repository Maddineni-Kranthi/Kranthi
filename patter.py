for c in range(7):
       for r in range(5):
              if (r!=0 and (c==0 or c==4)) or r==3 or (r==0 and c in {1,2,3}):
                     print('*', end=" ")
              else:
                      print(' ', end=" ")
       print()
