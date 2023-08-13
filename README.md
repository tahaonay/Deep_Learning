### Nedir bu öğrenme ?
İnsanlar gibi makinelerinde bir şeyleri yapabilmek için öncelikle öğrenmesi gerekmektedir. 
Peki biz nasıl öğreniyoruz ki;

1. **Gözlemleme**

İnsanlar, çevrelerindeki dünya ile etkileşime geçerek öğrenmek için gerekli olan veriyi toplarlar. Örneğin, bir bebeğin çevresini gözlemleyerek öğrenmeye başlaması gibi.

2. **Bağlam kurma**

Öğrenme, toplanan verilerin birbiri ile bağlantılarını kurması ile başlar. Her yeni bağlantı öğrenmeyi daha iyi anlamlandırmanın anahtarıdır. Örneğin, elimizi sobaya değmemiz ile sobadan sıcaklık hissetmek arasında bir ilişki kurmamız.

3. **Ödül-Ceza**

Kurulan ilişkilerden pozitif(ödül) veya negatif(ceza) geri bildirimler alarak gelecekteki davranışlarımıza bu kurulan ödül-ceza sistemiyle karar veririz. Sobaya elimizi değmemiz sonucunda gelen ısı canımızı acıttığı için bu eylemi tekrarlamak istemeyiz. Canımızın acıması bizim cezamızdır yani negatif geri bildirimimizdir.

4. **Anlama**

Ödül-ceza ilişkilerinden ortaya çıkan sonuçları artık bir çok farklı duruma uygulayarak bunlardan anlamlı sonuçlar çıkarmaya çalışırız. Isıdan dolayı canımızın acıdığını bildiğimizden elimizi artık sadece sobaya değil sıcak olan hiçbir şeye dokundurmak istemeyiz.

5. **Pratik**

Olurda elimizi yine sıcak bir şeylere değdirirsek örneğin bir bardak sıcak çay gibi veya üstümüze o çayı direk dökersek elimizdeki bilgileri pekiştirmiş oluruz. :)

### Peki makineler nasıl öğrenir ?
***Kısa Cevap:*** İnsanlar gibi.

***Uzun Cevap:*** 

1. **Veri Toplama**

Makineler, insanlar gibi veri toplayarak öğrenmeye başlarlar. Sensörler, kameralar, mikrofonlar gibi cihazlar aracılığıyla çevrelerindeki verileri toplarlar.

2. **Örüntü Tanıma**

Toplanan veriler, makine öğrenimi algoritmaları tarafından analiz edilir. Bu algoritmalar, verideki desenleri ve ilişkileri tanımlayarak öğrenmeye başlarlar.

3. **Model eğitimi ve doğrulaması**

Veriyi kullanarak model adı verilen bir yapı oluşturulur. Bu yapı verideki örüntüleri ve ilişkileri temsil eder. Oluşturulan modellerin performansı ve doğruluğu belirlenir.

4. **Tahmin ve Sonuç çıkarımı**

Eğitilen model, yeni verilere dayalı olarak çıkarımlarda bulunur.

5. **Geri bildirim**

Çıkarılan sonuçlar gerçek sonuçlarla karşılaştırılarak geri bildirim sağlanır ve model geliştirilir.

--------------------------------------------------------------

### Peki Derin Öğrenme? Makine Öğrenmesi?
Derin öğrenme(Deep learning) ve makine öğrenmesi(machine learning) terimleri, bir tür öğrenme yaklaşımıdır.

#### Derin Öğrenme:
Derin öğrenme, bilgisayarlara veriyi olduğu gibi sunup, bunun içinden anlamlı ilişkiler  çıkarmayı hedefleyen öğrenme yöntemidir. Bu yöntemde her bir ilişki farklı bir katman ile değerlendirilerek istenen sonuca ulaşılır.

*Örnek olarak derin öğrenme kullanarak bir yüz tanıma sistemi geliştirelim. İlk adımda, bir veri kümesi oluştururuz. Bu veri kümesi, farklı insanlara ait yüz fotoğraflarını ve bu fotoğrafların kime ait olduğu etiketlerini içerir. Bu veri kümesini kullanarak derin bir sinir ağı modeli oluştururuz.
Derin sinir ağı, katmanlar arasında karmaşık desenleri ve ilişkileri öğrenmeye çalışır. İlk katmanlar, basit özellikleri (kenarlar, çizgiler, eğriler gibi) öğrenirken, daha derin katmanlar yüzün daha karmaşık özelliklerini (göz ifadeleri, dudak şekli gibi) tanımayı öğrenir. Derin sinir ağı seviyesi arttıkça yüz tanıma performansı da o oranda artar. Tabi ki ihtiyaç duyulan işlem gücü de aynı oranda artmaktadır.
*

#### Makine Öğrenmesi:
Makine öğrenmesi, sisteme  modelleri vererek yada oluşturarak öğretme yöntemidir. Bu modeller, bilgisayarın veriyi analiz edip gelecekteki verileri tahmin etmesine yardımcı olur.

*Bu sefer makine öğrenimi kullanılarak yüz tanıma sistemi geliştirelim. Öncelikle veri kümesini kullanarak bir makine öğrenimi modeli oluştururuz.

Modelimiz, veriyi analiz eder ve yüzlerdeki örüntüleri öğrenir. Gözlerin, burunun ve ağızın konumları gibi özellikler, model tarafından öğrenilir. Modelimizi eğittikten sonra, yeni bir yüz fotoğrafı geldiğinde, model bu yüzdeki özellikleri analiz eder ve bu özelliklerin hangi kişiye ait olduğunu tahmin etmeye çalışır. Eğitim sırasında model, gerçek sonuçlarla karşılaştırılarak düzeltilir ve performansı artırılır.*


#### Yapay Zeka:
Yapay zeka, bilgisayarların akıllıca düşünmeyi taklit ettiği bir sistemdir. Bu sistemler, verileri inceler ve öğrenir, böylece problemleri çözmek için mantıklı adımlar atabilirler. 
Yapay zeka belirli bir amaç için üretilebileceği gibi (örn:Hava durumu tahmini), genel amaçlı kullanım için de üretilebilir. 


| Bölüm         | Açıklama      |
| ------------- | ------------- |
| [PyTorch Temelleri](https://github.com/tahaonay/Deep_Learning/tree/main/Temeller)     |  Kullanılacak ortam, PyTorch, PyTorch ile ilgili komutlar       |
| İş akışı      |              |
| Sinir ağı sınıflandırma|              |
| Bilgisayarlı görü|              |
| Özel veri kümeleri|              |
| Modülerlik     |              |
| Model transferi|              |
| ...              |              |
