from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    # Günün maçı (Sinner vs. Bonzi)
    gunun_maci = {
        "baslik": "Sinner vs. Bonzi",
        "turnuva": "ATP 1000 Madrid",
        "saat": "Şu An", 
        "durum": "Canlı", 
        "embed_link": "https://sportswin.click/play.php?atp-tour/atp-madrid-jannik-sinner-vs-benjamin-bonzi-stream-1"
    }

    # Diğer maçların listesi (Zeynep Sönmez'in linki eklendi)
    tum_maclar = [
        {
            "baslik": "🇹🇷 Zeynep Sönmez vs. Solana Sierra",
            "turnuva": "WTA 1000 Madrid - Son 32",
            "saat": "25 Nisan 12:00",
            "durum": "Başlamadı",
            "link": "https://taraftarium1049.xyz/" # Tıklanınca gidilecek link eklendi
        }
    ]

    # Verileri HTML sayfasına gönderiyoruz
    return render_template('index.html', gunun_maci=gunun_maci, tum_maclar=tum_maclar)

if __name__ == '__main__':
    app.run(debug=True)
