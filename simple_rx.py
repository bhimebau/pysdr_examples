#!/usr/bin/env python3 

import faulthandler; faulthandler.enable()
import adi
sdr = adi.Pluto('ip:192.168.2.1') # or whatever your Pluto's IP is
sdr.sample_rate = int(2.5e6)
print(sdr.rx())
print("Hi there")
