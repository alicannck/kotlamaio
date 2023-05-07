# kotlamaio

Dekoratörler diğer fonksiyonların işlevselliğini(görevlerini) değiştiren, kodları kısaltan ve daha okunabilir hale getiren fonksiyonlardır. Önce kendi içindeki işlevleri yapar ve sonrasında kendinden sonra gelen fonksiyonu çağırarak onu execute(uygulama) eder.


@pytest.mark.skip() : Belirlenen testlerin atlanmasını sağlar.

@pytest.fixture() : Testin çalışması için gereken koşulları önceden hazırlar.Testler arasında ortak bir durum veya kaynak paylaşmak için kullanılır.

@pytest.mark.parametrize() : Bir test fonksiyonunun farklı parametreler ile birden fazla çalışmasını sağlar.

@pytest.mark.timeout() : Testin belirtilen sürede tamamlanmasını sağlar.

@pytest.mark.order() : Testleri sıralamak için kullanılır.

@pytest.mark.xfail() : Testin başarısız olacağını düşünüyorsanız veya biliyorsanız bunu belirtmek ve sonucu etkilememesini sağlamak için kullanılır.

@pytest.mark.slow() : Belirtilen testin yavaş çalıştığını ve geri kalan testlere etki edebileceğini belirtir.


![odev5](https://user-images.githubusercontent.com/93056252/236693192-44832b26-ed7b-44e7-b953-3586b4af7fe9.png)
