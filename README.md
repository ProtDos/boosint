# Boosint

<p align="center">
  <p align="center">
    <img src="https://user-images.githubusercontent.com/69071809/205498298-cbdc7e47-73e0-491a-812a-05501380fad7.jpg" height="200"/>
  </p>
</p>

## About

**BoOSINT** collects data **by username only** by checking nearly every data publicly available about a username and it's aliases.


## Main features

* Profile pages parsing, extraction of personal info, links to other profiles, etc.
* Recursive search by new usernames and other ids found
* Search by tags (site categories, countries)
* Censorship and captcha detection
* Requests retries
* Finding of websites
* Finding device information, telephone number, email addresses
* Finding locations, gender, birthdays and real names


## Installation

### Cloning

```bash
# or clone and install manually
git clone https://github.com/protdos/boosint && cd boosint
pip install -r requirements.txt

# usage
python3 boosint.py username
```

## Usage

```bash
# make txt or json reports
boosint.py username --type txt
boosint.py username --type json

# filename output (default is report.json)
boosint.py username --output report.txt
boosint.py username --output report.json
```

Use `boosint -h` to get full options description.

##  Sources / Credits
Here is a list of sources I used:
* [Maigret](https://github.com/soxoj/maigret)
* [BlackBird](https://github.com/p1ngul1n0/blackbird)
* [GitRecon](https://github.com/GONZOsint/gitrecon)

The code is partly combined but the most of it is written by myself.
