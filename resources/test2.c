def prime_numbers(int n)
{
    int i = 3;
    i = 3;
    int count;
    int c;

    if(n >= 1)
    {
        print "\n\nFirst "
        print n;
        print  " prime numbers are :  ", n;
        print "2 ";
    }

    for(count = 2; count <= n; i = i +1)  
    {
        for(c = 2; c < i; c = c + 1)
        {
            if(i%c == 0)
                break;
        }

        if(c == i)
        {
            print i;
            print " ";
            count = count + 1;
        }
    }
    return;
}

def reverse_array(int n)
{
    int c;
    int d;
    a = new int[n];
    b = new int[n];
    
    print "Elementos do array:";
    for(c = 0; c < n; c = c+1){
        a[c] = c;
        print a[c];
        print " ";
    }

    d = 0;
    for(c = n-1; c >= 0; c = c-1) {
        b[d] = a[c];
        d = d + 1;
    }

    for(c = 0; c < n; c = c+1)
        a[c] = b[c];

    print "\n\n Array resultante é: ";
    for(c = 0; c < n; c = c+1)
        print a[c];
        print " ";

    return;
}

def big_and_small_array()
{
    int a[7];
    int i;
    int big;
    int small;

    a[0] = 25;
    a[1] = 17;
    a[3] = 95;
    a[0] = 205;
    a[1] = 42;
    a[3] = 129;
    a[3] = 1;
   

    print"\n\nThe elements of the array are: \n\n";
    for(i = 0; i < 7; i = i + 1)
        print a[i];
        print " ";

    big = a[0];

    for(i = 1; i < size; i++)
    {
        if(big < a[i])   
        {
            big = a[i];
        }
    }
    print "\n\nThe biggest element is: ";
    print big;

    small = a[0];

    for(i = 1; i < size; i++)
    {
        if(small>a[i])
        {
            small = a[i];
        }
    }
    print "\n\nThe smallest element is: ";
    print small;
    return;
}

def main()
{
    int n;
    n = 10;
    prime_numbers(n);
    n = 15;
    reverse_array(n);
    big_and_small_array();
}