# import threading
# from time import ctime,sleep
#
# def music(musname):
#     for i in range(2):
#         print('I was listening to %s,%s'%(musname,ctime()))
#         sleep(1)
#
# def read(bookname):
#     for i in range(2):
#         print('I was reading  %s,%s'%(bookname,ctime()))
#         # sleep(5)
# threads=[]
# t1=threading.Thread(target=music,args=('baby',))
# threads.append(t1)
# t2=threading.Thread(target=read,args=('sun',))
# threads.append(t2)
# if __name__=='__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#     print('over')

#python创建死锁
# # coding:utf8
# import threading
# import time
#
# num = 0
# lock = threading.Lock()
#
#
# def func(n):
#     lock.acquire()
#     print(n)
#     if (n == 5):
#         print("到我这就锁死了")
#         raise Exception('大死锁之术!')
#     lock.release()
#
#
# if __name__ == "__main__":
#     t4 = threading.Thread(target=func, args=(5,))
#     t1 = threading.Thread(target=func, args=(8,))
#     t2 = threading.Thread(target=func, args=(4,))
#     t3 = threading.Thread(target=func, args=(2,))
#
#     t4.start()
#     t1.start()
#     t2.start()
#     t3.start()