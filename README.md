
# Keylogger

Bu Python tabanlı keylogger, hem macOS hem de Windows platformlarında çalışan bir uygulamadır. Keylogger, tuş vuruşlarını ve bu sırada aktif olan pencerenin başlığını kaydeder. Uygulama, tuş vuruşlarını dinlemek için pynput kütüphanesini kullanır ve platforma özgü yöntemlerle aktif pencere başlığını alır.
## Özellikler
	•	Çoklu platform desteği: Hem macOS hem de Windows işletim sistemleri için 2 farklı script yazılmıştır.
	•	Aktif pencere takibi: Her tuş vuruşuyla birlikte aktif pencerenin başlığını kaydeder.
	•	Platforma özgü uygulama:
	•	macOS’ta, aktif pencere başlığını almak için AppleScript kullanılır.
	•	Windows’ta, pencere başlıklarını almak için pywin32 kütüphanesi ile Windows API’si kullanılır.
## Bilgisayarınızda Çalıştırın

Projeyi klonlayın

```bash
  git clone https://github.com/memirhan/Keylogger
```

Proje dizinine gidin

```bash
  cd Keylogger
```
macOS için

```bash
  python macos.py
```

Windows için

```bash
  python windows.py
```
  
## Gelecek Özellikler

	•	Ekran Görüntüsü Alma: Aktif pencerenin veya belirli bir alanın ekran görüntüsünü alma yeteneği.
	•	Mouse Takibi: Fare hareketlerini ve tıklamalarını kaydetme.
	•	Otomatik E-posta Gönderimi: Tuş vuruşlarını otomatik olarak hacker’ın e-posta adresine gönderme.
	•	Arka Planda Sessiz Çalışma: Uygulamanın kullanıcı tarafından görünmeden arka planda çalışabilmesi.

  
## Geri Bildirim

Projeyi geliştirmek, eksik yönlerini bildirmek vb. lütfen memirhansumer@gmail.com adresinden bana ulaşın.

  