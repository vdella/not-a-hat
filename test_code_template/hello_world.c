def hello_world()            
{
    print("Hello World");
    return;
}

def fibonacci(int num)
{
    int a;
    int b;
    int c;
    int i;
    i = 3;
    a = 0;
    b = 1;

    if(num == 1)
        print "0";

    if(num >= 2)
        print "0 1";

    return;
}

def palindrome(int a)
{
    int b;
    int c; 
    int s;
    s = 0;
    c = a;

    if(s == c)
    {
        print "The number ";
        print c;
        print " is a palindrome";
    }
    else
    {
        print "The number ";
        print c;
        print " is not a palindrome";
    }
    return
}

def sum_of_digits(int n)
{
	int sum;
    int c;
    int remainder;
    sum = 0;

    for (;;){
        if (n == 0){
            break;
        }
        remainder = n % 10;
        sum += remainder;
        n = n / 10;
    }

    	print "The sum of the digits of the number ";
        print n;
        print "is  =  ";
        print sum;
    	return;
}


def armstrong_number()
{
    int n, sum, i, t, a;
    print "\n\n\nThe Armstrong numbers in between 1 to 500 are : \n\n\n";

    for(i = 1; i <= 500; i = i + 1)
    {
        t = i;
        sum = 0
        for (;;){
            if (t == 0) {
                break;
            }
            a = t % 10;
            sum += a * a * a;
            t = t / 10;
        }

        if(sum == i)
            print " ";
            print i;
    }
}

def main()
{
    hello_world();
    print "Printing the first 10 terms of the fibonacci sequence";

    int num = 10;
    fibonacci(num);
    palindrome(193848);
    palindrome(123487784321);
    sum_of_digits(8478328);
    armstrong_number();
}