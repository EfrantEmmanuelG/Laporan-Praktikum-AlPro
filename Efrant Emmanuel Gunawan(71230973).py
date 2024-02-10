#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,'b',x,z,'r')
plt.xlabel('Radians');
plt.ylabel('Value');
plt.title('Plotting Demonstration')
plt.legend(['Sin','Cos'])
plt.grid()


# In[5]:


#Gerald membeli emas 25gram seharga RP 650.000/gram. Harga emas sekarang yaitu Rp 685.000/gram

emasgrm1 = 25
hrgbfr1 = 650000
hrgafr1 = 685000

#keuntungan yang didapatkan
untg1 = int(emasgrm1*hrgafr1 - emasgrm1*hrgbfr1)
prsn1 = float((untg1*100)/(emasgrm1*hrgbfr1))
print (f"Emas yang dimiliki Gerald yaitu >> {emasgrm1} gram\nKeuntungan yang didapatkan sebesar >> {untg1}\nKeuntungan dalam pe
       rsen >> {prsn1}%" )
print ()

membeli = 15
emasgrm2 = emasgrm1 + membeli
hrgbfr2 = 685000
hrgafr2 = 715000

untg2 = int((emasgrm2*hrgafr2)-(emasgrm1*hrgbfr1)-(membeli*hrgbfr2))
prsn2 = float((untg2*100)/((emasgrm1*hrgbfr1)+(membeli*hrgbfr2)))
print (f"Emas yang dimiliki Gerald yaitu >> {emasgrm2} gram\nKeuntungan yang didapatkan sebesar >> {untg2}\nKeuntungan dalam pe
       rsen >>{prsn2}%")


# In[7]:


#Erika memiliki uang Rp. 200.000.000 ingin melakukan deposito sampai uangnya minimal Rp 400.000.000
#bunga 10% per tahun

awal1 = 200000000
bunga = 10
tahun = 0
while awal1 <= 400000000:
    tahun=tahun+1
    awal1 = float(awal1*((100+bunga)/100))
b = float(round(awal1))
print (f"Diperlukan waktu {tahun} tahun untuk menjadikan uang Rp {b}")


# In[ ]:




