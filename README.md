<div align="center">
    <img src="https://github.com/openscilab/xnum/raw/main/otherfiles/logo.png" alt="XNum Logo" width="220">
    <h1>XNum: Universal Numeral System Converter</h1>
    <br/>
    <a href="https://badge.fury.io/py/xnum"><img src="https://badge.fury.io/py/xnum.svg" alt="PyPI version"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
    <a href="https://codecov.io/gh/openscilab/xnum"><img src="https://codecov.io/gh/openscilab/xnum/graph/badge.svg?token=0R14OKY0TB"></a>
    <a href="https://github.com/openscilab/xnum"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/openscilab/xnum"></a>
    <a href="https://discord.gg/h8T2F8WpFN"><img src="https://img.shields.io/discord/1064533716615049236.svg" alt="Discord Channel"></a>

</div>

----------


## Overview
<p align="justify">
<b>XNum</b> is a simple and lightweight Python library that helps you convert digits between different numeral systems — like English, Persian, Hindi, Arabic-Indic, Bengali, and more.
It can automatically detect mixed numeral formats in a piece of text and convert only the numbers, leaving the rest untouched. Whether you're building multilingual apps or processing localized data, <b>XNum</b> makes it easy to handle numbers across different languages with a clean and easy-to-use API.
</p>

<table>
    <tr>
        <td align="center">PyPI Counter</td>
        <td align="center">
            <a href="https://pepy.tech/projects/xnum">
                <img src="https://static.pepy.tech/badge/xnum">
            </a>
        </td>
    </tr>
    <tr>
        <td align="center">Github Stars</td>
        <td align="center">
            <a href="https://github.com/openscilab/xnum">
                <img src="https://img.shields.io/github/stars/openscilab/xnum.svg?style=social&label=Stars">
            </a>
        </td>
    </tr>
</table>
<table>
    <tr> 
        <td align="center">Branch</td>
        <td align="center">main</td>
        <td align="center">dev</td>
    </tr>
    <tr>
        <td align="center">CI</td>
        <td align="center">
            <img src="https://github.com/openscilab/xnum/actions/workflows/test.yml/badge.svg?branch=main">
        </td>
        <td align="center">
            <img src="https://github.com/openscilab/xnum/actions/workflows/test.yml/badge.svg?branch=dev">
            </td>
    </tr>
</table>
<table>
    <tr> 
        <td align="center">Code Quality</td>
        <td align="center"><a href="https://www.codefactor.io/repository/github/openscilab/xnum"><img src="https://www.codefactor.io/repository/github/openscilab/xnum/badge" alt="CodeFactor"></a></td>
        <td align="center"><a href="https://app.codacy.com/gh/openscilab/xnum/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/bf656e2daeeb45569dcc0cae705bc69d"></a></td>
    </tr>
</table>


## Installation

### PyPI
- Check [Python Packaging User Guide](https://packaging.python.org/installing/)
- Run `pip install xnum==0.5`
### Source code
- Download [Version 0.5](https://github.com/openscilab/xnum/archive/v0.5.zip) or [Latest Source](https://github.com/openscilab/xnum/archive/dev.zip)
- Run `pip install .`

## Usage

```pycon
>>> from xnum import convert, NumeralSystem
>>> print(convert("۱۲۳ apples & ٤٥۶ cars", target=NumeralSystem.ENGLISH))
123 apples & 456 cars
>>> print(convert("۱۲۳ and ٤٥٦", source=NumeralSystem.PERSIAN, target=NumeralSystem.HINDI))
१२३ and ٤٥۶
```

ℹ️ By default, the `source` parameter is set to `NumeralSystem.AUTO`, which automatically detects the numeral system

## Supported numeral systems

- English
	- Standard
	- Fullwidth
	- Subscript
	- Superscript
- Persian
- Hindi
- Arabic-Indic
- Bengali
- Thai
- Khmer
- Burmese
- Tibetan
- Gujarati
- Odia
- Telugu
- Kannada
- Gurmukhi
- Lao

## Issues & bug reports

Just fill an issue and describe it. We'll check it ASAP! or send an email to [xnum@openscilab.com](mailto:xnum@openscilab.com "xnum@openscilab.com"). 

- Please complete the issue template

You can also join our discord server

<a href="https://discord.gg/h8T2F8WpFN">
  <img src="https://img.shields.io/discord/1064533716615049236.svg?style=for-the-badge" alt="Discord Channel">
</a>


## Show your support


### Star this repo

Give a ⭐️ if this project helped you!

### Donate to our project
If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .			

<a href="https://openscilab.com/#donation" target="_blank"><img src="https://github.com/openscilab/xnum/raw/main/otherfiles/donation.png" width="270" alt="XNum Donation"></a>