import pandas as pd

# csv dosyasını usable hale getirdim.
data = pd.read_csv('store.csv',header=None)
t = []
for i in range(0,len(data)):
    t.append(str(data.values[i][0]).split(","))


def candidate(C1,n,min_support_count):
    minSup = []
    for i in range(len(C1)):
        minSup.append(items.count(C1[i]))
    for x in range(len(minSup)):
        if minSup[x] / n >= min_support_count:
            F1.append(C1[x])

def candidate_others(F1,n):
    C = []
    sup = []

    for i in range(0,len(F1)):
        for k in range(0,len(F1)):
            if k != i and k > i:
                C.append({F1[i], F1[k]})
    for i in range(len(C)):
        a = 0
        for x in lineTran:
            if C[i].issubset(x) == 1:
                a = a + 1

        sup.append(a)
    F1.clear()
    for x in range(len(sup)):
        if sup[x] / n >= min_support_count:
            F1.append(C[x])
    return F1
def candidate_more3(F1,n):
    C = []
    c_val={}
    sup=[]
    for f1 in F1:
        f1_list = list(f1.copy())
        for f2 in F1:
            f2_list = list(f2.copy())
            if (f1_list[:-1] == f2_list[:-1] and f1_list[-1] != f2_list[-1]) :
                c_val=f1.union(f2)
                #cValue=list(set().union(f1,f2))
            if len(c_val) != 0 and c_val not in C:
                C.append(c_val)

    for i in range(len(C)):
        a = 0
        for x in lineTran:
            if C[i].issubset(x) == 1:
                a = a + 1

        sup.append(a)
    F1.clear()
    for x in range(len(sup)):
        if sup[x] / n >= min_support_count:
            F1.append(C[x])
    return F1

C1 = []
F1=[]
items=[]
n=0  #number of transactions
min_support_count=0.3
c=0
lineTran=[]
print("This algoritm works with 0.3 support count.")
for transaction in t:
    n = n + 1
    if len(transaction) > c:
        c = len(transaction)
for k in range(0,c-1):
    if k==0:
        for transaction in t:
            lineTran.append(transaction)
            for item in transaction:
                items.append(item)
                if not item in C1:
                    C1.append(item)
        candidate(C1, n, min_support_count)
        print("F1 :",F1)

    else:
        if k==1:
            candidate_others(F1,n)
            print("F2 : ",F1)
        else:
            candidate_more3(F1,n)
            print("and more : ", F1)
    k=k+1

