__version__ = '0.2.0'

def checksum(string):
    """
    Compute the Luhn checksum for the provided string of digits. Note this
    assumes the check digit is in place.
    """
    digits = list(map(int, string))
    print(len(digits))
    print(digits)
    print('odd',digits[-1::-2])
    print('even',digits[-2::-2])
    odd_sum = sum(digits[-1::-2])
    for d in digits[-2::-2]:
        print('divmod', divmod(2 * d, 10))
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10

def verify(string):
    """
    Check if the provided string of digits satisfies the Luhn checksum.

    >>> verify('356938035643809')
    True
    >>> verify('534618613411236')
    False
    """
    return (checksum(string) == 0)

def generate(string):
    """
    Generate the Luhn check digit to append to the provided string.

    >>> generate('35693803564380')
    9
    >>> generate('53461861341123')
    4
    """
    cksum = checksum(string + '0')
    return (10 - cksum) % 10

def append(string):
    """
    Append Luhn check digit to the end of the provided string.

    >>> append('53461861341123')
    '534618613411234'
    """
    return string + str(generate(string))

if __name__ == '__main__':
    #print('4123000000000100 ', verify('4123000000000100'.strip()))
    #print('4123000000000200 ', verify('4123000000000200'.strip()))
    #print('4123000000000300 ', verify('4123000000000300'.strip()))
    #print('4123000000000400 ', verify('4123000000000400'.strip()))
    #print('4231000000000500 ', verify('4231000000000500'.strip()))
    #print('370077770000051  ', verify('370077770000051  '.strip()))
    #print('340000000000116  ', verify('340000000000116  '.strip()))
    #print('36937777000049   ', verify('36937777000049   '.strip()))
    #print('3530777700000061 ', verify('3530777700000061 '.strip()))
    #print('4980777700000041 ', verify('4980777700000041 '.strip()))
    #print('4566777700000037 ', verify('4566777700000037 '.strip()))
    #print('5279777700000024 ', verify('5279777700000024 '.strip()))
    #print('5251177700000022 ', verify('5251177700000022 '.strip()))
    #print('5250007700000025 ', verify('5250007700000025 '.strip()))
    #print('5219007700000019 ', verify('5219007700000019 '.strip()))
    #print('5257077700000016 ', verify('5257077700000016 '.strip()))
    #print('5312917700000013 ', verify('5312917700000013 '.strip()))
    #print('4541110700000031 ', verify('4541110700000031 '.strip()))
    #print('4205177700000036 ', verify('4205177700000036 '.strip()))
    #print('4538967700000037 ', verify('4538967700000037 '.strip()))
    #print('4685117700000032 ', verify('4685117700000032 '.strip()))
    #print('4897837700000062 ', verify('4897837700000062 '.strip()))
    #print('3583000000000008 ', verify('3583000000000008 '.strip()))
    #print('3530777700000062 ', verify('3530777700000062 '.strip()))
    #print('3530777700000063 ', verify('3530777700000063 '.strip()))
    #print('3530777700000064 ', verify('3530777700000064 '.strip()))
    #print('6011000000000500 ', verify('6011000000000500 '.strip()))
    #print('6011000000000600 ', verify('6011000000000600 '.strip()))
    #print('6011000000000700 ', verify('6011000000000700 '.strip()))
    #print('6011000000000800 ', verify('6011000000000800 '.strip()))
    #print('3530777700000074 ', verify('3530777700000074 '.strip()))
    #print('4980641000000001 ', verify('4980641000000001 '.strip()))
    #print('4012001037141112 ', verify('4012001037141112 '.strip()))
    #print('5105105105105100 ', verify('5105105105105100 '.strip()))
    #print('340000000000009  ', verify('340000000000009  '.strip()))
    #print('36252960520018   ', verify('36252960520018   '.strip()))
    #print('3540111111100000 ', verify('3540111111100000 '.strip()))
    #print('3584030000000001 ', verify('3584030000000001 '.strip()))
    #print('2221100000000001 ', verify('2221100000000001 '.strip()))
    #print('2222100000000001 ', verify('2222100000000001 '.strip()))
    #print('2223100000000001 ', verify('2223100000000001 '.strip()))
    #print('2224100000000001 ', verify('2224100000000001 '.strip()))
    #print('3530000000000001 ', verify('3530000000000001 '.strip()))
    #print('3530000000000002 ', verify('3530000000000002 '.strip()))
    #print('4123000000000001 ', verify('4123000000000001 '.strip()))
    #print('4123000000000002 ', verify('4123000000000002 '.strip()))
    #print('4123000000000003 ', verify('4123000000000003 '.strip()))
    #print('4123000000000004 ', verify('4123000000000004 '.strip()))
    #print('4123000000000005 ', verify('4123000000000005 '.strip()))
    #print('4123000000000006 ', verify('4123000000000006 '.strip()))
    #print('4123000000000007 ', verify('4123000000000007 '.strip()))
    #print('4123000013000100 ', verify('4123000013000100 '.strip()))
    #print('4123000014000100 ', verify('4123000014000100 '.strip()))
    #print('4123000023000300 ', verify('4123000023000300 '.strip()))
    #print('4123000012001700 ', verify('4123000012001700 '.strip()))
    #print('4123000012001800 ', verify('4123000012001800 '.strip()))
    #print('4123000012001900 ', verify('4123000012001900 '.strip()))
    #print('3123000024001100 ', verify('3123000024001100 '.strip()))
    #print('4123000012003400 ', verify('4123000012003400 '.strip()))
    #print('4123000012003600 ', verify('4123000012003600 '.strip()))
    #print('4123000009001400 ', verify('4123000009001400 '.strip()))
    #print('4123000015000100 ', verify('4123000015000100 '.strip()))
    #print('4123000017000100 ', verify('4123000017000100 '.strip()))
    #print('4123000022002000 ', verify('4123000022002000 '.strip()))
    #print('4123000002000100 ', verify('4123000002000100 '.strip()))
    #print('4123000007001200 ', verify('4123000007001200 '.strip()))
    #print('4123000007002200 ', verify('4123000007002200 '.strip()))
    #print('4123000007003000 ', verify('4123000007003000 '.strip()))
    #print('4123000007004400 ', verify('4123000007004400 '.strip()))
    #print('4123000007004500 ', verify('4123000007004500 '.strip()))
    #print('4123000007005400 ', verify('4123000007005400 '.strip()))
    #print('4123000007005500 ', verify('4123000007005500 '.strip()))
    #print('4123000007005600 ', verify('4123000007005600 '.strip()))
    #print('4123000007006000 ', verify('4123000007006000 '.strip()))
    #print('4123000007006100 ', verify('4123000007006100 '.strip()))
    #print('4123000007006800 ', verify('4123000007006800 '.strip()))
    #print('4123000007007200 ', verify('4123000007007200 '.strip()))
    #print('4123000007007400 ', verify('4123000007007400 '.strip()))
    #print('4123000007007500 ', verify('4123000007007500 '.strip()))
    #print('4123000007007800 ', verify('4123000007007800 '.strip()))
    #print('4123000007008300 ', verify('4123000007008300 '.strip()))
    #print('4123000007010000 ', verify('4123000007010000 '.strip()))
    #print('4123000007010100 ', verify('4123000007010100 '.strip()))
    #print('4123000007010200 ', verify('4123000007010200 '.strip()))
    #print('4123000007010300 ', verify('4123000007010300 '.strip()))
    #print('4123000007009500 ', verify('4123000007009500 '.strip()))
    #print('4123000007009600 ', verify('4123000007009600 '.strip()))
    #print('4123000007009700 ', verify('4123000007009700 '.strip()))
    print('4123000007009800 ', verify('4123000007009800 '.strip()))
    #print('4123000007009900 ', verify('4123000007009900 '.strip()))
    #print('4012001037461114 ', verify('4012001037461114 '.strip()))
    #print('5172837709537381 ', verify('5172837709537381 '.strip()))
    #print('341111597242513  ', verify('341111597242513  '.strip()))
    #print('38520000023237   ', verify('38520000023237   '.strip()))
    #print('3540111112211111 ', verify('3540111112211111 '.strip()))
