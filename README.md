# naumen-py-junior-test-case
### Python 3.6. Counter for 10 popular tweets and their 5 most-common words

Since there were no information about in.txt file I decided to create a generator myself. How does it work?

#### Fake tweets generator

```python
tweetgen.py (tweet amount) --separator (line separator if needed)
```

Please make sure you have installed everything from requirements.txt ```pip install -r requirements.txt```

#### Tweet parser

Original script doing it's work only for ```python
\n
``` separator. But it's only about correct regex, so I decided to omit this part, because no specification were given and there 2 places where it should be changed, so it'll be easy enough to track down and solve this case.

```python
tweetparse.py (path to file)
```

For both commands help is available.

####NOTE

If I understood this task incorrectly and file should be opened from the start of the function I'd like to take 1 more day to correct it and do it with [this library](https://click.palletsprojects.com/en/7.x/) instead of argparse.

#### How it works(both scripts / gif)
**Caution - small res :(**

![ALT TEXT](https://media.giphy.com/media/9A58TG4bpyupJXI0Wq/giphy.gif)