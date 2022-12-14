def main() {
    int integer;
    float floating_point;
    string str;

    integer = 10;
    floating_point = 5.0;
    str = "10";

    // Valid sums
    integer = integer + integer;
    floating_point = floating_point + floating_point;
    str = str + str;
    floating_point = integer + floating_point;
    floating_point = floating_point + integer;

    // Valid subtractions.
    integer = integer - integer;
    floating_point = floating_point - floating_point;
    floating_point = integer - floating_point;
    floating_point = floating_point - integer;

    // Valid multiplications.
    integer = integer * integer;
    floating_point = floating_point * floating_point;
    floating_point = integer * floating_point;
    floating_point = floating_point * integer;

    // Valid divisions.
    integer = integer / integer;
    floating_point = floating_point / floating_point;
    floating_point = integer / floating_point;
    floating_point = floating_point / integer;

    // Valid modulo.
    integer = integer % integer;
}
