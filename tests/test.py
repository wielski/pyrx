import pyrx
import binascii

assert pyrx.__version__ >= '0.0.3'

expected = [
        '0b3d9586ee70d69b2d50cd3f1a998abfd86b61d9d5a70e05e61ffcf1d7f865e7',
        'aa552e647873ed03c2a8d0712f0821cf7d7183b5ee8e1522e33ac686b61d618d',
        '7c81a6507ad86760c105e0ad192be79fa5e176490cd3a5ca7e79d2619d49b9c9',
        '2db4f3e131fdcce6116de0ca58629f5f6c0e6c31c59dca2513ae99b2f4156422',
        'b48299ccbe5ea2b1b8e8b195d5d8cf785633b6f2bb7f3c0e2f6e766042dd112d'
        ]

seed_hash = binascii.unhexlify('63eceef7919087068ac5d1b7faffa23fc90a58ad0ca89ecb224a2ef7ba282d48')
p = pyrx.PyRX()
for x in range(5000000):
    m = "Hello RandomX {}".format(x)
    print("Hashing: {}".format(m))
    if x == 0:
        print("(first takes a while, please wait)")
    h = 1 + x
    bh = p.get_rx_hash(m, seed_hash, h)
    hh = binascii.hexlify(bh).decode()
    print("Result: {}".format(hh))
    #assert hh == expected[x]

