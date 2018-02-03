def eval_loop():
  while True:
    user_input = raw_input(">")
    print user_input
    if user_input == 'done':
      print "done!"
      return
    else:
      print eval(user_input)

if __name__ == '__main__':
    eval_loop()


'''
OUTPUT:

pnq-rvyawahare:thinkpython rohit.vyawahare$ python ex7dot4.py
>4+3
4+3
7
>5+2*8
5+2*8
21
>done
done
done!

'''