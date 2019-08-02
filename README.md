# awakening
Repository for the awakening crypto problem.

`asleep()` and `awake()` are encryption / decryption funtions.

The code in `Awakening.py` depicts a terminal session interacting with these functions.

Figure out how to decode the encrypted messages `decode`, `decode2` and `decode3`.

Submit pull requests of `Requests.py` for any messages you want encoded, and any messages you want decoded (other than the solution), and I will add the results into the file.

Submit pull requests to `README.md` for any questions or clarification.

First person to solve this wins a piece of art!

Enjoy!

**UPDATE: I added a testdata folder. This includes 3 tests and corresponding log files. `test.py` and `log.txt` generates 7^5 dictionaries of string length 5 random/progressively. `test2.py` and `Log2.txt` generates 7^5 dictionaries of string length 5 straight randomly. `test3.py` and `Log3.txt` just shows an output of running 1 million tests checking input of `asleep()` with output of `awake()`. Feel free to propose more tests. I will generate more data if you're interested.**


Q1. Does the order of numbers in the encryption matter / if you moved the items in the dictionary around, would the encryption be different?  
A1. Dictionaries are inherently not ordered in python, the decryption takes this into account. You could take my encrypted message and move around all of the key value pairs and it would still be decrypted the same.

Q2. Do the quotes get encrypted as well / could you encrypt integers?  
A2. Strings follow python rules of nested quotes. In the string "That's my string!", the inner quote will be encrypted. Yes integers and special characters can be encrypted. Feel free to submit anything you want encrypted and I will let you know if it fails.

Q3. Is the `asleep()` function deterministic? Will it always product an identical dictionary given the same string?  
A3. Yes, `asleep()` will always produce the same dictionary given an identical string.

Q4. Can two-hand crafted encrypted-dicts provided to `awake()` produce identical plain-text?  
A4. I have not tried to prove it yet, but I'm pretty confident that that is the case, yes. Feel free to mess around with any of the things I have encrypted so far and I will run it through `awake()` to see how it effects plain-text, or if it will fail. **UPDATE: I generated a custom dictionary different than one generated by `asleep()` that will produce an identical string when put into `awake()`. It would be very easy for me to exploit this and make the program non-deterministic but I am going to leave everything as it is. I still feel the problem is challenging enough without making this change.**
