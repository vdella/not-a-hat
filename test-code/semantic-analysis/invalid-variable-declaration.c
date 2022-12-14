def main() {
    if (1 < 2) {
        print "Variable scope OK";
        int i;
        i = 3;
    }

    print "Variable scope OK";
    int i;

    print "ERROR";
    string i;
    i = "error!";
}
