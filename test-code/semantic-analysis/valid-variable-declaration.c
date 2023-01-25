def main() {
    print "Variable scope OK";
    int a;
    a = 2;
}

def util() {
    int i;
    for (i = 0; i < 2; i = i + 1) {
        print "Variable scope OK";
        int a;
        print "loop!";
    }

    print "Variable scope OK";
    int a;
    a = 5;
}
