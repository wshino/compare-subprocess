# Compare subprocess module in python 2.7

## motivation

I want to set timeout for heavy processing, such as spark-submit, rpm build, etc.

## Usage

```bash
pip install subprocess32 EasyProcess
```

```bash
python compare.py
```

| function | timeout | stdout in realtime |
|:---|:---|:---|
| subprocess | N | Y |
| easyprocess | Y | N |
| subprocess32 | Y | Y |
