from xarray.util.generate_ops import inplace

#2.unterricht
yil=2024

print(yil)

print(type(yil))

salaries=[1000,2000,3000,4000,5000]
def new(x):
    return x*20/100+x
for i in salaries:
    print(new(i))

    list(map(new,salaries))
    list(map(lambda x:x*20/100+x,salaries))
    list(map(lambda x:x*2,salaries))
list(map(new,salaries))
list(map(lambda x:x*50/100+x,salaries))

a=[10,20,30,40,50]

[i*5  if i>=30  else i/100  for i in a ]
[i*5 if i >= 30 else i/100 for i in a]
a = [10, 20, 30, 40, 50]
result = [i*5 if i >= 30 else i/100 for i in a]
print(result)

[new(i*2) if i <3000 else new(i)  for i in a ]






a=[10,20,30,40,50]


[i*3 if i>25 else i*6 for i in a]








import pandas  as  pd
import seaborn as sns
df=sns.load_dataset('titanic')
df.head()
df.tail()
df.info
df.info()
df.columns
a=[ col.upper() for col in df.columns]
a
df.columns=a
df.head()

df.isnull().values.any()
df.isnull().sum()
df.nunique()

df.head()
df['sayi']=df['SEX'].value_counts()
df.head()

df.drop('sayi',axis=1,inplace=True )
df.head()
df[0:3]
type(df['AGE'])
df[['AGE','ALIVE']]
COL_NAME=['AGE','ALIVE','FARE']
df[COL_NAME]



df['age1']=df['AGE']*2
df.head()

df['age2']=df['age1']+df['AGE']
df.head()
df.drop('age2',axis=1,inplace=True)
df.head()
df.drop('age1',axis=1,inplace=True)



df.iloc[0:3]
df.loc[0:3]
df.loc[0:3,'AGE']
df.loc[0:3,COL_NAME]



df['age'].head()
df[df['age']>50]['deck'].count()

df.head()
df[df['age']<10]

df[df['age']<10]['age'].count()
df.loc[df['age']<10],[['age','who']]

df['pclass'].value_counts()

df.loc[(df['age']>30) & (df['sex']=="male"),["age","sex","class"]].head()
df['age'].mean()
df.groupby('sex')['age'].mean()
df.groupby('sex').agg({'age':['mean','median']})

df.groupby(['sex','embark_town']).agg({'age':['mean',sum],"survived":"mean"})

df.groupby(['sex','embark_town','class']).agg({'age':['mean','sum'],'survived':['mean','sum'],'sex':'count'})
df.head()

df.pivot_table('survived','sex','embarked')
df.pivot_table('survived','sex',['embarked','class'])

df['new_age']=pd.cut(df["age"],[0,10,18,25,40,90])
df.head()
df.pivot_table('survived','sex',['new_age','class'])


import matplotlib.pyplot as plt

df['sex'].value_counts().plot(kind='bar')




plt.hist(df['age'])
plt.show()

plt.boxplot(df['fare'])

df=sns.load_dataset('tips')

df.head()

df['sex'].value_counts()
sns.countplot(x=df['sex'],data=df)

df['sex'].value_counts().plot(kind='bar')
plt.show()


sns.boxplot(x=df['total_bill'])


df['total_bill'].hist()

import numpy as np
m=np.random.randint(10,size=(5,5))
m
v=np.arange(0,30,3)
x=[3,5,6]
v[x]
m=np.arange(1,10).reshape(3,3)
m




yil=2024
dog_yil=int(input('tarih gir'))
print('yasiniz:'yil-dog_yil)


isim=["ali",2005,"istanbul",70.5,True]
isim[0]



print(type(isim[0]))


isim[1]='kemal'
isim

print(isim[3])

?isim
isim.append('lale')
isim

isim.insert(2,'polis')

isim.pop()
isim

isim.remove('kemal')
list
isim
a='kahramanmarasli'
a.replace('a','i')
a

a=[1,5,6,8,2,96,58]

a.sort()
a

[i for i in a if i%2==0]


sonuc=3//2
print(sonuc)

sonuc=6
sonuc+=5
print(sonuc)

sonuc=(3!=0)
print(sonuc)

if True:
    print('hi')
print('the end')

if False:
    print('kal')
print('Hu')



if 5 in [1,2,3,4]:
    print('k')
elif 5 in [5,6,7,8]:
    print('m')
else:
 print('l')




mesafe=float(input('mesafe gir:'))

km2mile=0.6213
print('meafe mile cins:'+ str(mesafe*km2mile))




mesafe=input('mesafe gir:')

km2mile=0.6213
print('meafe mile cins:'+ str(mesafe*km2mile))

list1=mesafe.split(' ')

km=int(liste1[0])
birim=liste1[1]



##################################################
kullanici_girisi = input("Mesafeyi giriniz: ") # '1000 K' , '1000 M'
girdi_listesi = kullanici_girisi.split()
mesafe = int(girdi_listesi[0])
birim = girdi_listesi[1].upper()

KM2MILE = 0.621371192

KM_birimleri = ["K", "KM", "KILOMETRE"]
Mile_birimleri = ["M", "MILE", "MIL"]

if birim in KM_birimleri:
    print("Mesafe mile cinsinden: " + str(mesafe * KM2MILE))
elif birim in Mile_birimleri:
    print("Mesafe kilometre cinsinden: " + str(mesafe / KM2MILE))
else:
    print("Hatalı birim girdiniz!")
#######################################################################


#tuple--daha hizli -degistirilemez

km_birimleri=('km','KM','KILOMETRE')
km_birimleri
################################################
user={
    'yas':25,
    'adi':'ahmet',
    'is':{'unvan':'muh','departman':'yazilim'}
}



user.keys()
user.values()


print(user.get('is').get('unvan'))
user['is']['unvan']

print(list(user.values()))
user.keys()
user.items()

print(user.get('adress','adres bulunamadi'))
#######################
print (list(range(10)))


for i in range(5):
    print(i)


#######################
fiyatlar=[100,200,300,400,500]

toplam_fiyat=0
for fiyat in fiyatlar:
    toplam_fiyat+=fiyat
print(toplam_fiyat)   #sonuc hepsini topladi
#####################################
i=0
while i<10:
    print('sayilar:'+str(i))
    i+=1




####################






































































































































































