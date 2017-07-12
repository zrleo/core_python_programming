#!/usr/bin/env python


def pay(s_paid, s_balance):
    print "Pymt# Paid Balance"
    print "----- ----- ------"
    i = 0
    while ( s_balance > s_paid ):

        s_balance = s_balance - s_paid
        i += 1
        print " %d $%f $%f" % (i, s_paid, s_balance)
        i += 1
        print" %d $%f $%f" % (i, s_balance, 0)

if __name__ == "__main__":
    s_balance = raw_input("please enter the balance:")
    s_paid = raw_input("please enter the paid:")
    s_balance = float(s_balance)
    s_paid = float(s_paid)
    pay(s_paid, s_balance)
