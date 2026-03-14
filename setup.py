#!/usr/bin/env python3
"""
DIXBLO SİKER SALAN İNER OROSPUNUN ÇOCUKLARI PUAJAJAJAJAJAJAJA
Authorized Penetration Testing Suite - Kurulum Dosyası
Kali Linux / Windows için otomatik bağımlılık yükleyici
"""

from setuptools import setup, find_packages
import sys
import os
import subprocess
import platform

# Versiyon bilgisi
VERSION = "2.0.0"

# Gerekli Python paketleri
REQUIRED_PACKAGES = [
    'colorama>=0.4.4',
    'requests>=2.25.0',
    'scapy>=2.4.5',
    'pywifi>=1.1.12',
    'concurrent-futures>=3.1.1',
    'urllib3>=1.26.0',
    'certifi>=2020.12.5',
    'idna>=2.10',
    'chardet>=4.0.0',
]

# İsteğe bağlı paketler (bazı modüller için)
EXTRAS_REQUIRE = {
    'wireless': [
        'scapy>=2.4.5',
        'pywifi>=1.1.12',
        'wifi>=0.3.8',
    ],
    'crypto': [
        'pycryptodome>=3.10.0',
        'cryptography>=3.4.0',
    ],
    'osint': [
        'beautifulsoup4>=4.9.0',
        'lxml>=4.6.0',
    ],
    'full': [
        'scapy>=2.4.5',
        'pywifi>=1.1.12',
        'wifi>=0.3.8',
        'pycryptodome>=3.10.0',
        'cryptography>=3.4.0',
        'beautifulsoup4>=4.9.0',
        'lxml>=4.6.0',
        'netifaces>=0.11.0',
        'netaddr>=0.8.0',
        'paramiko>=2.7.0',
    ]
}

# Sistem bağımlılıklarını kontrol et ve kur
def check_system_dependencies():
    """Sistem seviyesindeki bağımlılıkları kontrol eder"""
    
    system = platform.system().lower()
    dependencies_installed = True
    
    if system == 'linux':
        # Linux için gerekli paketler
        linux_packages = [
            'aircrack-ng',
            'reaver',
            'bully',
            'hcxdumptool',
            'hcxpcapngtool',
            'bettercap',
            'nmap',
            'net-tools',
            'wireless-tools',
            'iw',
            'hostapd',
            'dnsmasq',
            'sslstrip',
            'dnsspoof',
            'tshark',
            'wireshark-common',
            'python3-pip',
            'python3-dev',
            'build-essential',
            'libssl-dev',
            'libffi-dev',
            'libpcap-dev',
        ]
        
        print("\n[+] Linux sistem tespit edildi. Gerekli paketler kontrol ediliyor...")
        
        # Paket yöneticisini tespit et
        if os.path.exists('/usr/bin/apt'):
            cmd_check = ['dpkg', '-s']
            cmd_install = ['sudo', 'apt', 'install', '-y']
            pkg_manager = 'apt'
        elif os.path.exists('/usr/bin/yum'):
            cmd_check = ['rpm', '-q']
            cmd_install = ['sudo', 'yum', 'install', '-y']
            pkg_manager = 'yum'
        elif os.path.exists('/usr/bin/pacman'):
            cmd_check = ['pacman', '-Q']
            cmd_install = ['sudo', 'pacman', '-S', '--noconfirm']
            pkg_manager = 'pacman'
        else:
            print("[!] Desteklenen paket yöneticisi bulunamadı (apt/yum/pacman)")
            return True
        
        missing_packages = []
        
        for pkg in linux_packages:
            try:
                result = subprocess.run(cmd_check + [pkg], 
                                      stdout=subprocess.DEVNULL, 
                                      stderr=subprocess.DEVNULL)
                if result.returncode != 0:
                    missing_packages.append(pkg)
            except:
                missing_packages.append(pkg)
        
        if missing_packages:
            print(f"[!] Eksik sistem paketleri: {', '.join(missing_packages)}")
            answer = input("[?] Bu paketleri kurmak ister misiniz? (e/E): ").lower()
            if answer == 'e':
                try:
                    print(f"[+] Paketler kuruluyor ({pkg_manager})...")
                    subprocess.run(cmd_install + missing_packages, check=True)
                    print("[+] Sistem paketleri başarıyla kuruldu.")
                except subprocess.CalledProcessError as e:
                    print(f"[!] Paket kurulumu başarısız: {e}")
                    dependencies_installed = False
                except KeyboardInterrupt:
                    print("\n[!] Kurulum iptal edildi.")
                    dependencies_installed = False
            else:
                print("[!] Sistem paketleri kurulmadan devam ediliyor...")
                dependencies_installed = False
        else:
            print("[+] Tüm sistem paketleri mevcut.")
    
    elif system == 'windows':
        # Windows için özel kontroller
        print("\n[+] Windows sistem tespit edildi.")
        print("[!] Bazı wifi modülleri için monitor modu gerekebilir.")
        print("[!] Npcap veya WinPcap kurulu olmalıdır.")
        
        # Npcap kontrolü
        npcap_paths = [
            r'C:\Program Files\Npcap',
            r'C:\Program Files (x86)\Npcap',
            r'C:\Windows\System32\Npcap'
        ]
        
        npcap_found = any(os.path.exists(path) for path in npcap_paths)
        
        if not npcap_found:
            print("[!] Npcap bulunamadı! Scapy için gerekli.")
            print("[i] İndirme: https://npcap.com/#download")
            print("[i] Kurulum sırasında 'WinPcap API-compatible Mode' işaretlenmeli.")
            dependencies_installed = False
    
    return dependencies_installed

# Kali Linux özel kurulum
def setup_kali():
    """Kali Linux için özel konfigürasyon"""
    if os.path.exists('/usr/bin/kali'):
        print("[+] Kali Linux tespit edildi. Özel ayarlar yapılandırılıyor...")
        
        # Kali araçlarına sembolik linkler
        kali_tools = {
            'aircrack-ng': '/usr/bin/aircrack-ng',
            'reaver': '/usr/bin/reaver',
            'bully': '/usr/bin/bully',
            'hcxdumptool': '/usr/bin/hcxdumptool',
            'bettercap': '/usr/bin/bettercap',
        }
        
        for tool, path in kali_tools.items():
            if os.path.exists(path):
                print(f"  ✓ {tool} bulundu: {path}")
        
        return True
    return False

# Readme içeriği
with open("README.md", "w", encoding="utf-8") as f:
    f.write("""# DIXBLO Penetration Testing Suite

## 🚫 YASAL UYARI
Bu araç **SADECE** eğitim amaçlıdır ve yetkili güvenlik testleri için tasarlanmıştır. 
İzinsiz kullanımı yasa dışıdır ve ciddi yasal sonuçları olabilir. 
Kullanımından doğacak her türlü sorumluluk kullanıcıya aittir.

## 📋 Özellikler
- DDoS Saldırı Araçları
- WiFi Jammer (Deauth Attack)
- IP Geolocation OSINT
- Telegram Phone Finder
- WiFi Şifre Kırıcı
- MITM Araçları
- Discord ID OSINT
- SMS Bomber

## 🔧 Kurulum

### Otomatik Kurulum
```bash
# Repoyu klonla
git clone https://github.com/dixblo-q/ComeBack
cd ComeBack

# Kurulumu çalıştır
python3 setup.py install
