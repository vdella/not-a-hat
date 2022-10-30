def fib(int n)
{
    if (n == 1)
    {
        return 1;
    }

    if (n == 2)
    {
        return 1;
    }

    int first = n - 1;
    int second = n - 2;

    int fib_first = fib(first);
    int fib_second = fib(second);
    int result = fib_first + fib_second;

    return result;
}

def main()
{
    return fib(3);
}