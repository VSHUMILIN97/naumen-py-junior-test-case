# naumen-py-junior-test-case
### Python 3.6. Counter for 10 popular tweets and their 5 most-common words

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2f04f5b4155446509980f411183f5d8d)](https://www.codacy.com/app/VSHUMILIN97/naumen-py-junior-test-case?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=VSHUMILIN97/naumen-py-junior-test-case&amp;utm_campaign=Badge_Grade)

Since there were no information about in.txt file I decided to create a tweet generator myself. How does it work?

#### Fake tweets generator

```tweetgen.py (tweet amount) --separator (line separator if needed)```

The output of this function is in.txt that will be stored in the same directory where script is and will be filled with fake tweets.

Please make sure you have installed everything from requirements.txt

```pip install -r requirements.txt```

#### Tweet parser

Original script doing it's work only for ```\n``` separator. Nevertheless it's only about correct regex pattern, so I decided to omit this part, because no specification were given. Besides, it'll be easy enough to track down and solve this case, because of lack of regex usage.

```tweetparse.py (path to file)```

For both scripts ```--help``` command is available.

#### NOTE

If I understood this task incorrectly and file should be opened from the start of the function I'd like to take 1 more day to correct it and do it with [this library](https://click.palletsprojects.com/en/7.x/) instead of argparse.

#### How it works(both scripts / gif)
**Caution - small res :(**

![ALT TEXT](https://media.giphy.com/media/9A58TG4bpyupJXI0Wq/giphy.gif)
