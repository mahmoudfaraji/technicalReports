import random
import string

AllKeyListForRounds = []
Rconnnnnnn = 0x0


def generateKeyRandom():

    char = 'abcdef' + string.digits
    return ''.join(random.choice(char) for _ in range(0, 24))


KEY = '000000000000000000000000'

sbox = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
        0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
        0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
        0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
        0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
        0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
        0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
        0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
        0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
        0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
        0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
        0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
        0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
        0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
        0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
        0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
        0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
        0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
        0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
        0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
        0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
        0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
        0x54, 0xbb, 0x16]


def generatColumn(key):

    keyList = [key[i:i+2] for i in range(0, len(key), 2)]
    return [keyList[0:4], keyList[4:8], keyList[8:12]]


def rotateUp(keyColumn3):

    return [keyColumn3[1], keyColumn3[2], keyColumn3[3], keyColumn3[0]]


def subByte(element_of_column):

    return sbox[int(element_of_column, 16)]


Rcon = [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54, 108, 216, 171, 77, 154, 47, 94, 188, 99, 198, 151, 53, 106, 212, 179, 125, 250, 239, 197, 145, 57, 114,
        228, 211, 189, 97, 194, 159, 37, 74, 148, 51, 102, 204, 131, 29, 58, 116, 232, 203, 141, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54, 108, 216, 171, 77,
        154, 47, 94, 188, 99, 198, 151, 53, 106, 212, 179, 125, 250, 239, 197, 145, 57, 114, 228, 211, 189, 97, 194, 159, 37, 74, 148, 51, 102, 204, 131,
        29, 58, 116, 232, 203, 141, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54, 108, 216, 171, 77, 154, 47, 94, 188, 99, 198, 151, 53, 106, 212, 179, 125, 250,
        239, 197, 145, 57, 114, 228, 211, 189, 97, 194, 159, 37, 74, 148, 51, 102, 204, 131, 29, 58, 116, 232, 203, 141, 1, 2, 4, 8, 16, 32, 64, 128, 27,
        54, 108, 216, 171, 77, 154, 47, 94, 188, 99, 198, 151, 53, 106, 212, 179, 125, 250, 239, 197, 145, 57, 114, 228, 211, 189, 97, 194, 159, 37, 74,
        148, 51, 102, 204, 131, 29, 58, 116, 232, 203, 141, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54, 108, 216, 171, 77, 154, 47, 94, 188, 99, 198, 151, 53,
        106, 212, 179, 125, 250, 239, 197, 145, 57, 114, 228, 211, 189, 97, 194, 159, 37, 74, 148, 51, 102, 204, 131, 29, 58, 116, 232, 203, 141]


def getRcon(value):

    return Rcon[int(value, 16)]


columns = generatColumn(KEY)


def defineParamForCore():

    rotated = rotateUp(columns[2])

    final = []
    final.append(subByte(rotated[0]))
    final.append(subByte(rotated[1]))
    final.append(subByte(rotated[2]))
    final.append(subByte(rotated[3]))

    rconn = getRcon(Rconnnnnnn)

    return core(columns, final, rconn)


def core(columns, final, rconn):

    roundKeyList = []

    k1_1 = [None] * 4
    k1_2 = [None] * 4
    k1_3 = [None] * 4

    final[0] ^= rconn

    final[0] = format((final[0] ^ int(columns[0][0], 16)),
                      '#04x').split('x')[-1]
    final[1] = format((final[1] ^ int(columns[0][1], 16)),
                      '#04x').split('x')[-1]
    final[2] = format((final[2] ^ int(columns[0][2], 16)),
                      '#04x').split('x')[-1]
    final[3] = format((final[3] ^ int(columns[0][3], 16)),
                      '#04x').split('x')[-1]

    k1_1 = final

    roundKeyList.append(k1_1)

    k1_2[0] = format((int(k1_1[0], 16) ^ int(
        columns[1][0], 16)), '#04x').split('x')[-1]
    k1_2[1] = format((int(k1_1[1], 16) ^ int(
        columns[1][1], 16)), '#04x').split('x')[-1]
    k1_2[2] = format((int(k1_1[2], 16) ^ int(
        columns[1][2], 16)), '#04x').split('x')[-1]
    k1_2[3] = format((int(k1_1[3], 16) ^ int(
        columns[1][3], 16)), '#04x').split('x')[-1]

    roundKeyList.append(k1_2)

    k1_3[0] = format((int(k1_2[0], 16) ^ int(
        columns[2][0], 16)), '#04x').split('x')[-1]
    k1_3[1] = format((int(k1_2[1], 16) ^ int(
        columns[2][1], 16)), '#04x').split('x')[-1]
    k1_3[2] = format((int(k1_2[2], 16) ^ int(
        columns[2][2], 16)), '#04x').split('x')[-1]
    k1_3[3] = format((int(k1_2[3], 16) ^ int(
        columns[2][3], 16)), '#04x').split('x')[-1]

    roundKeyList.append(k1_3)

    return roundKeyList


def generate_next_keycolumn(k1_1, k1_2, k1_3):

    newkeucolumn = [[None for c in range(0, 4)] for r in range(0, 3)]

    newkeucolumn[0][0] = hex(int(k1_1[0], 16) ^ int(
        k1_2[0], 16) ^ int(k1_3[0], 16)).split('x')[-1]
    newkeucolumn[0][1] = hex(int(k1_1[1], 16) ^ int(
        k1_2[1], 16) ^ int(k1_3[1], 16)).split('x')[-1]
    newkeucolumn[0][2] = hex(int(k1_1[2], 16) ^ int(
        k1_2[2], 16) ^ int(k1_3[2], 16)).split('x')[-1]
    newkeucolumn[0][3] = hex(int(k1_1[3], 16) ^ int(
        k1_2[3], 16) ^ int(k1_3[3], 16)).split('x')[-1]

    global columns

    newkeucolumn[1][0] = columns[0][0]
    newkeucolumn[1][1] = columns[0][1]
    newkeucolumn[1][2] = columns[0][2]
    newkeucolumn[1][3] = columns[0][3]

    newkeucolumn[2][0] = columns[1][0]
    newkeucolumn[2][1] = columns[1][1]
    newkeucolumn[2][2] = columns[1][2]
    newkeucolumn[2][3] = columns[1][3]

    columns = newkeucolumn


def rotateUp_1(k1_1, k1_2, k1_3):

    new_K1_1 = [None]*4
    new_K1_2 = [None]*4
    new_K1_3 = [None]*4

    new_K1_1[0] = k1_1[1]
    new_K1_1[1] = k1_1[2]
    new_K1_1[2] = k1_1[3]
    new_K1_1[3] = k1_1[0]

    new_K1_2[0] = k1_1[2]
    new_K1_2[1] = k1_1[3]
    new_K1_2[2] = k1_1[0]
    new_K1_2[3] = k1_1[1]

    new_K1_3[0] = k1_1[3]
    new_K1_3[1] = k1_1[0]
    new_K1_3[2] = k1_1[1]
    new_K1_3[3] = k1_1[2]

    return [new_K1_1, new_K1_2, new_K1_3]


def FinalCore():

    for i in range(0, 12):

        global Rconnnnnnn
        columnsXored = int(columns[0][0], 32) ^ int(columns[0][1], 32) ^ int(
            columns[0][2], 32) ^ int(columns[0][3], 32)
        Rconnnnnnn = hex(columnsXored % 256).split('x')[-1]

        rt = defineParamForCore()

        AllKeyListForRounds.append(rt)

        gh = rotateUp_1(rt[0], rt[1], rt[2])

        generate_next_keycolumn(gh[0], gh[1], gh[2])

    return AllKeyListForRounds
