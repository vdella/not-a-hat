def symmetric_matrix()
{
    int c; 
    int d;
    int a[10][10];
    int b[10][10];
    int n;
    int temp;
    int i;
    i = 0;

    n = 5;
    for(c = 0; c < n; c = c + 1) {
        for(d = 0; d < n; d = d + 1) {
            a[c][d] = i;
            i = i + 1;
        } 
    }

    for(c = 0; c < n; c = c + 1) {
        for(d = 0; d < n; d = d + 1) {
            b[d][c] = a[c][d];
        } 
    }

    print "\n\nThe original matrix is: \n\n";
    for(c = 0; c < n; c = c + 1)
    {
        for(d = 0; d < n; d = d + 1)
        {
            print a[c][d];
            print " ";
        }
        print "\n";
    }

    print "\n\nThe Transpose matrix is: \n\n";
    for(c = 0; c < n; c = c + 1)
    {
        for(d = 0; d < n; d = d + 1)
        {
            print b[c][d];
            print " ";
        }
        print "\n";
    }

    for(c = 0; c < n; c = c + 1)
    {
        for(d = 0; d < n; d = d + 1)
        {
            if(a[c][d] != b[c][d]) 
            {
                print "\n\nMatrix is not Symmetric\n\n";
                return;
            }
        }
    }

    print "\n\nMatrix is Symmetric\n\n";
    print "\n\n\t\t\tCoding is Fun !\n\n\n";
    return;
}

int add_sub_matrices()
{
    int m;
    int n;
    int c;
    int d;
    int first[10][10];
    int second[10][10];
    int sum[10][10];
    int diff[10][10];

    m = 6;
    n = 4;
    int i;
    i = 0;

    for(c = 0; c < m; c = c + 1) {
        for(d = 0; d < n; d = d + 1) {
            first[c][d] = i;
            i = i + 1
        }
    }

    int j;
    j = 97;
    for(c = 0; c < m; c = c + 1) {
        for(d = 0; d < n; d = d + 1){
            second[c][d] = j;
            j = j - 1;
        }
    }

    print "\n\nThe first matrix is: \n\n";
    for(c = 0; c < m; c = c + 1)
    {
        for(d = 0; d < n; d = d + 1)
        {
            print first[c][d];
            print " ";
        }
        print "\n";
    }

    print "\n\nThe second matrix is: \n\n";
    for(c = 0; c < m; c = c + 1)
    {
        for(d = 0; d < n; d = d + 1)
        {
            print second[c][d];
            print " ";
        }
        print "\n";
    }

    for(c = 0; c < m; c = c + 1) {
        for(d = 0; d < n; d = d + 1){
            sum[c][d] = first[c][d] + second[c][d];
        }
    }    

    print "\n\nThe sum of the two entered matrices is: \n\n";
    for(c = 0; c < m; c = c + 1)
    {
        for(d = 0; d < n; d = d + 1)
        {
            print sum[c][d];
            print " ";
        }
        print "\n";
    }

    for(c = 0; c < m; c = c + 1) {
        for(d = 0; d < n; d = d + 1) {
            diff[c][d] = first[c][d] - second[c][d];
        }
    }

    print "\n\nThe difference(subtraction) of the two entered matrices is: \n\n";
    for(c = 0; c < m; c = c + 1)
    {
        for(d = 0; d < n; d = d + 1)
        {
            print diff[c][d];
            print " ";
        }
        print "\n";
    }
    return;
}

def main()
{
    symmetric_matrix();
    add_sub_matrices();
}