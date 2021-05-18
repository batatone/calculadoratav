def soma(n1,n2):
        n1=float(n1)
        n2=float(n2)
        n3= n1+n2
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)
        return n3
def sub(n1,n2):
        n1 = float(n1)
        n2 = float(n2)
        n3= n1-n2
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)
        return n3

def mult(n1,n2):
        n1 = float(n1)
        n2 = float(n2)
        n3= n1*n2
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)
        return n3

def div(n1, n2):
        n1 = float(n1)
        n2 = float(n2)
        if (n2==0):
                print ("n pode dividir por 0")
                return "erro"
        n3= n1/n2
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)
        return n3