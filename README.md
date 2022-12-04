# CryptoQuail
> ## NOTE: This repository uses ECB — it is not for serious use

The CryptoQuail block cipher is a new encryption based on the [CryptoQuail](https://github.com/cardinal9999/CryptoQuail) stream cipher. It is designed to be more secure than it.

## How it Works
CryptoQuail works by using modular addition, xor, and the rail fence cipher. It encrypts each block with an amount of rounds. The number of rounds is depended on the number of blocks it already encrypted.

The key for the encryption is 24 bytes long. You can generate a key from a seed string with [this program](https://pastebin.com/TdtVYr7q).

[Diagram of CryptoQuail](howitworks.md)

## How secure is it?
> UPDATE: THIS IS OUTDATED

Like the stream cipher, it is good at the avalanche effect, but sometimes, 2 ciphertexts that have been encrypted with a similar key might have some same characters.

You can encrypt the string 3 or 4 times for better security.

You can also try hashing the key and using the first 24 bytes for encryption with `cryptoquail.keygen`. This is the most effective method.

> (Even if CryptoQuail encrypts strings, it only supports the first 256 unicode characters.)
## Installation
You need to have Git command line installed on your computer.

Type:
```shell
git clone https://github.com/cardinal9999/cryptoquail_cipher
cd cryptoquail_cipher
```

### 1. Python
Now, type `py` to open Python. If you type `import cryptoquail`, it will import the module and you can encrypt and decrypt strings with the block cipher.

If you want to use CryptoQuail encryption in IDLE, move the `cryptoquail.py` file to the directory of your Python project.

#### Example
```py
# Import CryptoQuail 
import cryptoquail
key = cryptoquail.keygen("password")
# Encryption
ciphertext = cryptoquail.encrypt("text to encrypt", key) # Encrypt it 3 times for more security.
# Decryption
plaintext = cryptoquail.decrypt(ciphertext, key)
```
