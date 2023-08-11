## Başlamadan Önce
Anlatım boyunca python programlama dilini ve pytorch kütüphanesini kullanacağım. 
Kullanacağınız belirli bir ide yok ise Anaconda/Spyder kullanmanızı öneririm.


[**Anaconda**](https://www.anaconda.com/)

[**PyTorch**](https://pytorch.org/)


**Deep learning** ve **machine learning** içerdikleri **matematiksel** hesaplamalar sebebiyle çok fazla **işlem gücü** istemektedir. Ekran kartlarının işlemcileri, bilgisayar işlemcilerine göre matematiksel işlemleri daha hızlı hesaplama kabiliyetine sahiptir. Bu sebeple öğrenim algoritmalarını **GPU** üzerinde çalıştırmak gerek duyulan işlem gücünü bizlere sağlamaktadır.

### PyTorch'u ekleme

![Anaconda](https://github.com/tahaonay/Deep_Learning/assets/21277419/56fee0fa-dff1-4d8b-b282-311b409dea98)

Kullanacağımız kütüphaneyi yukarıdaki şekilde yükledikten sonra projemize "PyTorch" kütüphanesini aşağıdaki şekilde ekleriz. 

```ruby
import torch
```



### Tensör Oluşturma

**Tensör**: Matematikte, çok boyutlu verilerin simgelenebildiği geometrik bir nesnedir.
![image](https://github.com/tahaonay/Deep_Learning/assets/21277419/48ae5fc8-dace-4d74-b312-aaeddb4e6c2b)

Tensörlerin, tek boyutlu ve yönsüz büyüklük olanına **Skaler**, yönlü olanlarına **Vektör**, iki boyutlu olanına ise **Vektör** denmektedir.

![image](https://github.com/tahaonay/Deep_Learning/assets/21277419/5d91334a-1839-4624-86b4-c9c2ec629ce9)

çeşitli boyutlardaki tensörleri eklemek için,
```ruby
scalar = torch.tensor(1)
vector = torch.tensor([1,2])
matrix = torch.tensor([[1,2],[3,4]])
tensör = torch.tensor([[[1,2],[3,2],[1,7],[5,4]]])
```

### Tensörlerden resim oluşturma
```ruby
import torch

width = 1920
height = 1080
channels = 3  # RGB renk kanalları

image_tensor = torch.rand(channels, height, width)  # Rastgele değerlerle doldurulmuş bir tensör
```

### Tensör bilgisi sorgulama
".ndim" metodu tensörün kaç boyuta sahip olduğunu verir

".shape" metodu tensörün şeklini verir


```ruby
import torch

tensor = torch.tensor([[[1,2,3],[4,5,6],[7,8,9]]])
print(tensor.ndim)    
print(tensor.shape)   
```

```
tensor([[[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]])      # Tensör
3                          # Tensörün Boyutu
torch.Size([1, 3, 3])      # Tensörün Şekli
```

*"[" köşeli parantez sayısı tensördeki boyut sayısını hesaplamanın bir diğer yoludur.*

![image](https://github.com/tahaonay/Deep_Learning/assets/21277419/5af52990-fba6-4cc2-a9ac-6d929d31868c)


