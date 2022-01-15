# CryptoQuail
The CryptoQuail block cipher is a new encryption based on the [CryptoQuail](https://github.com/cardinal9999/CryptoQuail) stream cipher. It is designed to be more secure than it.

## How it Works
CryptoQuail works by using modular addition, xor, and the rail fence cipher. It encrypts each block with an amount of rounds. The number of rounds is depended on the number of blocks it already encrypted.

The key for the encryption is 24 bytes long.

[Diagram of CryptoQuail](howitworks.md)

## How secure is it?
Like the stream cipher, it is good at the avalanche effect, but sometimes, 2 ciphertexts that have been encrypted with a similar key might have some same characters.

You can encrypt the string 2 or 3 times for much better security.

## Installation
You need to have Git command line installed on your computer.

Type:
```shell
git clone https://github.com/cardinal9999/cryptoquail_cipher
cd cryptoquail_cipher
```

Now, type `py` to open Python. If you type `import cryptoquail`, it will import the module and you can encrypt and decrypt strings with the block cipher.

If you want to use CryptoQuail encryption in IDLE, move the `cryptoquail.py` file to the directory of your Python project.

## Example
```py
# Import CryptoQuail 
import cryptoquail
key = "336NTMZESMUW9ZMSFXTLLT4P"
# Encryption
ciphertext = cryptoquail.encrypt("text to encrypt", key)
# Decryption
plaintext = cryptoquail.decrypt(ciphertext, key)
```
