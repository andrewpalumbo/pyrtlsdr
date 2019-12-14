import asyncio
from rtlsdr import RtlSdr
import PIPE
import io.StringIO

from pylab import *
from rtlsdr import *

import asyncio
   ...: from rtlsdr import RtlSdr
   ...:
   ...: async def streaming():
   ...:     sdr = RtlSdr()
   ...:     # configure device
   ...:     sdr.sample_rate = 2.4e6
   ...:     sdr.center_freq = 101e5
   ...:     sdr.gain = 4
   ...:
   ...:     sample = sdr.read_samples(256*1024)
   ...:     psd(sample, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
   ...:     xlabel('Frequency (MHz)')
   ...:     ylabel('Relative power (dB)')
   ...:     show()
   ...:     async for samples in sdr.stream():
   ...:         x=samples
   ...:         print(x)
   ...:     # to stop streaming:
   ...:     await sdr.stop()
   ...:
   ...:     # done
   ...:     sdr.close()
   ...:
   ...: loop = asyncio.get_event_loop()
   ...: loop.run_until_complete(streaming())