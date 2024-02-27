# Sort-the-Elements-of-an-Array-in-Descending-Order


Bu proje, verilen bir sayı dizisini azalan sıraya göre sıralayan bir Python scriptidir. Kullanıcı tarafından sağlanan diziyi alır, diziyi azalan sıraya göre sıralar ve sıralı diziyi yazdırır.

## Kurulum

Bu scriptin çalışması için Python'un bilgisayarınızda kurulu olması gerekmektedir. Python kurulumu hakkında daha fazla bilgi için [Python'un resmi web sitesini](https://www.python.org/) ziyaret edebilirsiniz.

Projeyi yerel ortamınıza klonlamak için:

1. Terminal veya komut istemcisini açın.
2. Projeyi klonlamak istediğiniz dizine gidin.
3. Aşağıdaki komutu kullanarak projeyi klonlayın:
   
   git clone https://github.com/yourusername/your-repository-name.git
   
4. Klonlama işlemi tamamlandıktan sonra, projenin dizinine gidin:
   
   cd your-repository-name
   

## Çalıştırma Talimatları

Scripti çalıştırmak için, projenin bulunduğu dizinde terminal veya komut istemcisini açın ve aşağıdaki komutu girin:


python main.py

Bu komut, scripti çalıştıracak ve örnek diziyi azalan sıraya göre sıralayıp sonucu ekrana yazdıracaktır.

## Özellikler

- Verilen diziyi azalan sıraya göre sıralar.
- Kullanımı kolay ve anlaşılır.

## Örnek Kullanım

```python
def sort_array_desc(arr):
    # Sorting the array in descending order
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr

# Example array
arr = [5, 3, 8, 6, 7, 2]

# Function call to sort the array
sorted_arr = sort_array_desc(arr)

# Printing the sorted array
print("Sorted array in descending order:", sorted_arr)
```

Çıktı:
```
Sorted array in descending order: [8, 7, 6, 5, 3, 2]
```



