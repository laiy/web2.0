#include <string>
#include <iostream>

#define shift(x, n) (((x) << (n)) | ((x) >> (32 - (n))))
#define F(x, y, z) (((x) & (y)) | ((~x) & (z)))
#define G(x, y, z) (((x) & (z)) | ((y) & (~z)))
#define H(x, y, z) ((x) ^ (y) ^ (z))
#define I(x, y, z) ((y) ^ ((x) | (~z)))

#define A 0x67452301
#define B 0xefcdab89
#define C 0x98badcfe
#define D 0x10325476

unsigned int str_length;
unsigned int a_temp;
unsigned int b_temp;
unsigned int c_temp;
unsigned int d_temp;

const unsigned int ti[] = {
        0xd76aa478,0xe8c7b756,0x242070db,0xc1bdceee,
        0xf57c0faf,0x4787c62a,0xa8304613,0xfd469501,0x698098d8,
        0x8b44f7af,0xffff5bb1,0x895cd7be,0x6b901122,0xfd987193,
        0xa679438e,0x49b40821,0xf61e2562,0xc040b340,0x265e5a51,
        0xe9b6c7aa,0xd62f105d,0x02441453,0xd8a1e681,0xe7d3fbc8,
        0x21e1cde6,0xc33707d6,0xf4d50d87,0x455a14ed,0xa9e3e905,
        0xfcefa3f8,0x676f02d9,0x8d2a4c8a,0xfffa3942,0x8771f681,
        0x6d9d6122,0xfde5380c,0xa4beea44,0x4bdecfa9,0xf6bb4b60,
        0xbebfbc70,0x289b7ec6,0xeaa127fa,0xd4ef3085,0x04881d05,
        0xd9d4d039,0xe6db99e5,0x1fa27cf8,0xc4ac5665,0xf4292244,
        0x432aff97,0xab9423a7,0xfc93a039,0x655b59c3,0x8f0ccc92,
        0xffeff47d,0x85845dd1,0x6fa87e4f,0xfe2ce6e0,0xa3014314,
        0x4e0811a1,0xf7537e82,0xbd3af235,0x2ad7d2bb,0xeb86d391
};

const unsigned int s[] = {
        7,12,17,22,7,12,17,22,7,12,17,22,7,
        12,17,22,5,9,14,20,5,9,14,20,5,9,14,20,5,9,14,20,
        4,11,16,23,4,11,16,23,4,11,16,23,4,11,16,23,6,10,
        15,21,6,10,15,21,6,10,15,21,6,10,15,21
};

const char str16[] = "0123456789abcdef";

unsigned int* fill(std::string str) {
    unsigned int num = (((str.length() + 8) * 8) / 512) + 1;
    str_length = num * 16;
    unsigned int *strByte = new unsigned int[str_length];

    for (unsigned int i = 0; i < str_length; i++)
        strByte[i] = 0;

    for (unsigned int i = 0; i < str.length(); i++)
        strByte[i >> 2] |= (str[i]) << ((i % 4) * 8);
    strByte[str.length() >> 2] |= 0x80 << (((str.length() % 4)) * 8);

    strByte[str_length - 2] = str.length() * 8;
    return strByte;
}

void loop(unsigned int *M) {
    unsigned int f, j, tmp;
    unsigned int a = a_temp;
    unsigned int b = b_temp;
    unsigned int c = c_temp;
    unsigned int d = d_temp;

    for (unsigned int i = 0; i < 64; i++) {
        if (i < 16)
            f = F(b, c, d), j = i;
        else if (i < 32)
            f = G(b, c, d), j = (5 * i + 1) % 16;
        else if (i < 48)
            f = H(b, c, d), j = (3 * i + 5) % 16;
        else
            f = I(b, c, d), j = (7 * i) % 16;
        tmp = d, d = c, c = b;
        b = b + shift((a + f + M[j] + ti[i]), s[i]);
        a = tmp;
    }

    a_temp = a + a_temp;
    b_temp = b + b_temp;
    c_temp = c + c_temp;
    d_temp = d + d_temp;
}

std::string int_to_hex(int a) {
    int b;
    std::string str = "", temp;
    for(int i = 0; i < 4; i++) {
        temp = "";
        b = ((a >> i * 8) % (1 << 8)) & 0xff;
        for (int j = 0; j < 2; j++)
            temp.insert(0, 1, str16[b % 16]), b = b / 16;
        str += temp;
    }
    return str;
}

std::string get_MD5(std::string source) {
    a_temp = A;
    b_temp = B;
    c_temp = C;
    d_temp = D;

    unsigned int *strByte = fill(source), num[16];

    for(unsigned int i = 0; i < str_length / 16; i += 16)
    {
        for(unsigned int j = 0; j < 16; j++)
            num[j] = strByte[i * 16 + j];
        loop(num);
    }

    return int_to_hex(a_temp).append(int_to_hex(b_temp)).append(int_to_hex(c_temp)).append(int_to_hex(d_temp));
}

int main()
{
    std::string s, md5;
    std::cout << "input a string and it would output the MD5" << std::endl;
    while (std::cin >> s) {
        md5 = get_MD5(s);
        std::cout<< md5 << std::endl;
        std::cout << "input a string and it would output the MD5" << std::endl;
    }
    return 0;
}

