import subprocess

sayi = 0 # ilk verecegimiz değer 0 sonra 10 sonra 20 diye devam edecek
devam = True
with open(r"C:\Users\ogulc\OneDrive\Masaüstü\visual\ssh\wordlist.txt","r",encoding="utf8") as dosya:
    dosya = dosya.read().splitlines()
    uzunluk = len(dosya)

while devam:
    çıktı = subprocess.run(f'cmd /c "python "C:\\Users\\ogulc\\OneDrive\\Masaüstü\\visual\\ssh\\ssh_brute_force.py" -b {sayi}"',shell=True,capture_output=True,text=True) #main.py adlı dosyanın yolunu yazın 
    print(çıktı.stdout) #çıktıyı görmeniz icin yazdırdım
    if "şifre" in str(çıktı.stdout):
        devam = False # şifre bulunduysa while döngüsünü sonlandırır
    else:
        if sayi > uzunluk:
            break
        sayi += 10 # eğer şifre bulunamadıysa şifreyi denemeye 10.indexden devam edicez eğer yine bulunamadıysa bir 10 daha ekliycez 
        #bu durumda index 20 olacak ve şifre 20. index'den itibaren kontrol edilmeye başlanacak şifre bulunana kadar böyle devam edecek  
        
