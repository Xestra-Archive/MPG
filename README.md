# Mass Password Generator
A simple mass password generator that is easy to use.

## How to use the generator
Just run the python file and make sure you have python installed. When you run the file just answer the inputs. Then, you will get your file with all of your passwords.

## Benchmarking
- specs
    - I5 8600k
    - 32GB of ram
- 10 characters
    - 100 passwords
        - 0.0026 Seconds
    - 10000 passwords
        - 0.0931 Seconds
- 16 characters
    - 100 passwords
        - 0.0029 Seconds
    - 10000 passwords
        - 0.1375 Seconds

## Code
```python
import random
import string

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '!#$%&()*+,-./:;<=>?@[]^_`{|}~'

def gen(length):
    password = ''.join(random.choice(chars) for i in range(length))
    password.strip(' ')
    return str(password)
```