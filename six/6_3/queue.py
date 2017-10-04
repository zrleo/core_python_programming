# -*- coding:utf-8 -*-

queue = []


def en_Q():
    queue.append(raw_input("输入一个字符串").strip())


def del_Q():
    if len(queue) == 0:
        print "队列为空"
    else:
        print 'removed [', queue.pop(), '] '


def view_Q():
    print queue

CMDs = {
    'e': en_Q, 'd': del_Q, 'v': view_Q
}


def show_menu():
    pr = '''
    'e': en_Q, 
    'd': del_Q,
    'v': view_Q
        
    Enter choice:
    '''

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = "q"

            print '\nYou picked: [%s]' % choice
            if choice not in 'edvq':
                print "不可用"
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    show_menu()
