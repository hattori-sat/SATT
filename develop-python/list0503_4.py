import random
pl_pos=1
com_pos=1
def banmen():
    print("・"*(pl_pos-1)+"P"+"・"*(30-pl_pos))
    print("・"*(com_pos-1)+"C"+"・"*(30-com_pos))
while True:
    banmen()
    input("please enter")
    pl_pos+=random.randint(1,6)
    com_pos+=random.randint(1,6)
