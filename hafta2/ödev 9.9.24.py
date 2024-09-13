
#Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
import seaborn as sns
from matplotlib.pyplot import ylabel

df = sns.load_dataset('titanic')
df.head()

#Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz


df['sex'].value_counts()


# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.

 df.nunique()




# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.

df['pclass'].nunique()


#Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.


 df[['pclass', 'parch']].nunique()


#Görev 6: embarked değişkeninin tipini kontrol ediniz.

print(df['embarked'].dtype)


df['embarked'] = df['embarked'].astype('category')
print(df['embarked'].dtype)


#Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
df[df['embarked'] == 'C']



#Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.

non_s_embarked_df = df[df['embarked'] != 'S']


print(non_s_embarked_df)


#Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.


 df[(df['age'] < 30) & (df['sex'] == 'female')]
















pip uninstall seaborn pandas matplotlib





















#Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.


 df[(df['fare'] > 500) | (df['age'] > 70)]




#Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.

 df.isnull().sum()




#Görev 12: who değişkenini dataframe’den çıkarınız.

df.drop(columns=['who'])




# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
df['deck'].value_counts()
df['deck'].mode()
df['deck'].mode()[0]
df['deck'].fillna(df['deck'].mode()[0],inplace=True)
df.head()
df.isnull().sum()
df['pclass'].fillna(4,inplace=True)
df
df['age'].value_counts()
df['age'].fillna(df['age'].mean(), inplace=True)
df


#g 14:age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df=sns.load_dataset('Titanic')
df.head()
df['age'].value_counts()
df.isnull().sum()
df['age'].median()
df['age'].fillna(df['age'].median(),inplace=True)
df['age'].mode()[0]

df['age'].fillna(df['age'].median(), inplace=True)

#Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

df.groupby(['pclass','sex'])['survived'].agg(['sum','count','mean'])

#Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
#setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)

df['age_flag'] = df['age'].apply(lambda x: 1 if x < 30 else 0)


#Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

df=sns.load_dataset('tips')
df.head()


#Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby('time')['total_bill'].agg(['sum','min','max','mean'])


#Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.


df.groupby(['time','day'])['total_bill'].agg(['sum','min','max','mean'])
df.groupby(['day','time'])['total_bill'].agg(['sum','min','max','mean'])

#Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin
# day'e göre toplamını, min, max ve ortalamasını bulunuz.



df1= df[(df['time'] == 'Lunch') & (df['sex'] == 'Female')]


df1.groupby('day')[['total_bill', 'tip']].agg(['sum', 'min', 'max', 'mean'])





#Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
# (loc kullanınız)



df1 = df.loc[(df['size'] < 3) & (df['total_bill'] > 10)]

df1['total_bill'].mean()



#Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.


df['total_bill_tip_sum'] = df['total_bill'] + df['tip']

df[['total_bill', 'tip', 'total_bill_tip_sum']].head()

#Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve
# ilk 30 kişiyi yeni bir dataframe'e atayınız.


 df.sort_values(by='total_bill_tip_sum', ascending=False).head(30)
