# Stock Portfolios

## Install requirements

```bash
pip3 install -r requirements.txt
```

## Usage

Update `stocks.json` with your portfolios.

```bash
./main.py
```

Sampe output:

```bash

******
Stock Code: GUBRF

     Cost: 85.3  TRY
  Current: 79.65 TRY
     Gain: -5.65 TRY
   Gain %: -6.62
     Mean: 80.62 TRY
      Max: 82.55 TRY
      Min: 79.65 TRY

             Open   High    Low  Close    Volume Currency
Date                                                     
2021-03-10  81.10  85.65  80.75  82.55  13190867      TRY
2021-03-12  79.35  81.70  78.60  79.65   3088867      TRY

******
Stock Code: SISE

     Cost: 7.1   TRY
  Current: 7.66  TRY
     Gain: 0.56  TRY
   Gain %: 7.89 
     Mean: 7.61  TRY
      Max: 7.73  TRY
      Min: 7.13  TRY

            Open  High   Low  Close     Volume Currency
Date                                                   
2021-02-26  7.08  7.19  7.04   7.13  113245600      TRY
2021-03-12  7.72  7.73  7.61   7.66   77813600      TRY
```

![Figure 1](./Figure_1.png)