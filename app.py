from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    # Günün maçının bilgileri Sinner vs. Bonzi olarak güncellendi
    gunun_maci = {
        "baslik": "Sinner vs. Bonzi",
        "turnuva": "ATP 1000 Madrid",
        "saat": "Şu An", 
        "durum": "Canlı", 
        "embed_link": "https://sportswin.click/play.php?atp-tour/atp-madrid-jannik-sinner-vs-benjamin-bonzi-stream-1"
    }

    # Diğer maçların listesi (İstersen buradaki maçları da güncelleyebilirsin)
    tum_maclar = [
        {
            "baslik": "Alcaraz vs. Medvedev",
            "turnuva": "ATP 1000 Madrid",
            "saat": "21:00",
            "durum": "Başlamadı"
        },
        {
            "baslik": "Djokovic vs. Nadal",
            "turnuva": "Çeyrek Final",
            "saat": "14:30",
            "durum": "Bitti"
        }
    ]

    # Verileri HTML sayfasına gönderiyoruz
    return render_template('index.html', gunun_maci=gunun_maci, tum_maclar=tum_maclar)

if __name__ == '__main__':
    app.run(debug=True)