ComeBack Toolkit - DIXBLO Penetration Testing Suite

Dixblo Buba (akrep aic) tarafından geliştirilen, yetkili güvenlik testleri ve eğitim amaçlı kapsamlı bir penetration testing toolkit'tir.

🚫 YASAL UYARI

Bu araç yalnızca eğitim amaçlıdır ve yalnızca sahibi olduğunuz veya yazılı izniniz bulunan sistemler üzerinde kullanılmalıdır. İzinsiz kullanımı yasa dışıdır ve ciddi yasal sonuçlar doğurabilir. Kullanımından doğacak her türlü sorumluluk kullanıcıya aittir.

✨ Özellikler

ComeBack Toolkit, aşağıdaki güvenlik test modüllerini içerir:

1. 💀 Extreme DDoS Arsenal
   · Smart Proxy SYN Flood (Proxy + Ban Tespiti)
   · HTTP GET/POST Flood (Çoklu İş Parçacığı)
   · UDP Flood (Amplification Ready)
   · Slowloris (Bağlantı Tüketme)
2. 📡 WiFi Jammer
   · Deauth Attack (aireplay-ng ile)
   · Scapy Deauth Flood
   · WiFi Ağ Tarayıcı
3. 🌍 IP Geolocation OSINT
   · IP adresi konum, ISP, VPN tespiti
4. 📱 Telegram Phone Finder
   · OSINT kaynakları ile telefon numarası arama
5. 🔓 WiFi Password Cracker
   · WPS Pixie Dust (Reaver)
   · WPA Sözlük Saldırısı
   · Evil Twin (Fluxion)
   · PMKID Attack (HcXtools)
6. 🕵️ MITM (Man-In-The-Middle) Arsenal
   · ARP Zehirleme (Bettercap)
   · SSLStrip + HSTS Bypass
   · DNS Sahtekarlığı (Spoofing)
   · Ağ Tarayıcı (Nmap)
7. 💬 Discord ID OSINT
   · Discord kullanıcı ID'si ile bilgi toplama
8. 📨 SMS Bomber
   · Çoklu API desteği ile SMS bombardımanı
   · Ayarlanabilir iş parçacığı (thread) sayısı
   · Canlı istatistik takibi

📋 Gereksinimler

· İşletim Sistemi: Kali Linux (önerilen), Ubuntu/Debian tabanlı sistemler veya Windows
· Python: Sürüm 3.7 veya üzeri
· Donanım: WiFi modülleri için monitor modunu destekleyen bir wireless adaptör
· Yetki: WiFi ve bazı ağ işlemleri için root yetkisi gereklidir.

🔧 Kurulum

1. Depoyu Klonlayın

```bash
git clone https://github.com/dixblo-q/ComeBack.git
cd ComeBack
```

2. Python Bağımlılıklarını Yükleyin

Ana dizinde bulunan setup.py dosyasını kullanarak gerekli Python paketlerini kurabilirsiniz:

```bash
pip3 install -e .
```

Ya da doğrudan pip ile:

```bash
pip3 install -r requirements.txt
```

Ana bağımlılıklar: colorama, requests, scapy, pywifi

3. Sistem Araçlarını Kurun (Linux - Özellikle Kali İçin)

Tam işlevsellik için aşağıdaki sistem araçlarının kurulu olması gerekir. Kali Linux'ta çoğu ön tanımlıdır.

```bash
sudo apt update
sudo apt install aircrack-ng reaver bully hcxdumptool bettercap nmap sslstrip dsniff
```

4. Çalıştırın

```bash
# Normal çalıştırma (DDoS, OSINT modülleri için)
python3 main.py

# WiFi ve MITM modülleri için root yetkisiyle çalıştırın
sudo python3 main.py
```

🎯 Kullanım Kılavuzu

Tool çalıştırıldığında ana menü karşınıza gelecektir. İlgili modülün numarasını girerek alt menülere erişebilirsiniz.

1. Başlatma: python3 main.py komutu ile tool'u başlatın. Renkli bir banner ve ana menü görünecektir.
2. Navigasyon: Menülerde gezinmek için ilgili numarayı yazıp Enter'a basın.
3. Parametre Girişi: Her modül sizden IP adresi, port, hedef URL, BSSID gibi gerekli parametreleri isteyecektir.
4. Durdurma: Çoğu saldırı modülü (Ctrl+C) ile durdurulabilir. Ana menüden çıkmak için ilgili çıkış seçeneğini kullanın.

Örnek Kullanım:

· WiFi ağlarını taramak için: Ana Menü > 5. WiFi Password Cracker > 5. WiFi Scanner
· Bir IP'nin konumunu öğrenmek için: Ana Menü > 3. IP Geolocation OSINT

📁 Dosya Yapısı

```
ComeBack/
├── main.py          # Ana toolkit dosyası (tüm modülleri içerir)
├── setup.py         # Python kurulum betiği
├── requirements.txt # Python bağımlılık listesi
└── README.md        # Bu dosya
```

⚠️ Sorumluluk Reddi

Bu tool, güvenlik profesyonellerinin ve sistem yöneticilerinin kendi sistemlerini test etmeleri için geliştirilmiştir. Geliştirici veya katkıda bulunanlar, aracın kötü niyetli veya yasa dışı amaçlarla kullanımından sorumlu tutulamaz. Aracı kullanmadan önce yetkili olduğunuzdan emin olun.

📞 İletişim

Tool'un orijinal geliştiricisi Dixblo Buba'ya aşağıdaki kanallardan ulaşabilirsiniz:

· İnstagram: @dixblowashere
· Discord: @tukenecegizz
· Telegram: @a3kr4p
