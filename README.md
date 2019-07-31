# awakening
Repository for the awakening crypto problem.

"asleep()" and "awake()" are encryption / decryption funtions.

The code in "Awakening.py" depicts a terminal session interacting with these functions.

Figure out how to decode the encrypted messages "decode", "decode2" and "decode3".

Submit pull requests of "Requests.py" for any messages you want encoded, and any messages you want decoded (other than the solution), and I will add the results into the file.

Submit pull requests to "README.md" for any questions or clarification.

First person to solve this wins a piece of art!

Enjoy!


Q1. Does the order of numbers in the encryption matter / if you moved the items in the dictionary around, would the encryption be different?
A1.Dictionaries are inherently not ordered in python, the decryption takes this into account. You could take my encrypted message and move around all of the key value pairs and it would still be decrypted the same.

Q2. Do the quotes get encrypted as well / could you encrypt integers?
A2. Strings follow python rules of nested quotes. In the string "That's my string!", the inner quote will be encrypted. Yes integers and special characters can be encrypted. Feel free to submit anything you want encrypted and I will let you know if it fails.

Q3. Is the `asleep()` function deterministic? Will it always product an identical dictionary given the same string?
